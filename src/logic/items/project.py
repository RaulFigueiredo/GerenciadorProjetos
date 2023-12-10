"""
This module defines the Project class, which implements the IItem interface.
It represents a project with various attributes and methods to manage its lifecycle.

Classes:
    Project: Represents a project with attributes such as name, label, end date,
    description, creation date, conclusion date, status, and associated tasks.
    It provides methods for project management including adding, deleting, updating
    tasks, and setting the project's conclusion status.

Exceptions:
    ItemDontHaveThisAttribute: Raised when trying to update an attribute that doesn't
                               exist in the Project class.
    NonChangeableProperty: Raised when attempting to change a property that is not
                           allowed to be modified.
"""

from datetime import date
from typing import List, Any
from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser
from src.logic.execeptions.exceptions_items import  ItemDontHaveThisAttribute,\
                                                    NonChangeableProperty
from src.logic.items.project_memento import ProjectMemento
from src.logic.orms.orm import ProjectORM
from src.db.database import Database
from sqlalchemy.orm import sessionmaker

class Project(IItem):
    """
    A class to represent a project, implementing the IItem interface.

    Attributes:
        _user (IUser): The user associated with the project.
        _name (str): The name of the project.
        _label (IItem): The label associated with the project. Default is None.
        _end_date (date): The projected end date of the project. Default is None.
        _description (str): A description of the project. Default is None.
        _creation_date (date): The date when the project was created.
        _conclusion_date (date): The date when the project was concluded. Default is None.
        _status (bool): The status of the project, indicating whether it is concluded.
                        Default is False.
        _tasks (List[IItem]): A list of tasks associated with the project.

    Methods:
        delete: Deletes the project and its associated tasks.
        update: Updates the project's attributes, except for user, creation_date, and tasks.
        add_task: Adds a task to the project.
        remove_task: Removes a task from the project.
        conclusion: Marks the project as concluded and sets the conclusion date.
        unconclusion: Reverts the project's status to unconcluded.
        Various property getters for accessing project attributes.
    """

    def __init__(self, user: IUser ,name: str, id_project: int = None, label: IItem = None,
                 end_date: date = None, description: str = None, conclusion_date: date = None,
                 status: bool = False, creation_date: date = None, id_label: int = None) -> None:
        """
        Initialize a new Project object with given parameters.

        Parameters:
            user (IUser): The user creating the project.
            name (str): The name of the project.
            label (IItem, optional): A label associated with the project. Defaults to None.
            end_date (date, optional): The anticipated end date of the project. Defaults to None.
            description (str, optional): A brief description of the project. Defaults to None.
        """
        self._user = user
        self._name = name
        self._id_label = id_label
        self._label = label
        self._end_date = end_date
        self._description = description
        self._creation_date = creation_date if creation_date else date.today()
        self._conclusion_date = conclusion_date
        self._status = status
        self._id_project = id_project
        
        self._tasks: List[IItem] = []
        self._mementos = []
        self._user.add_project(self)

        self.db = Database()
        self.SessionLocal = sessionmaker(bind=self.db.engine)

        if not self._id_project:
            self.save_to_db()

    def save_to_db(self):
        with self.SessionLocal() as session:
            new_project_orm = ProjectORM(id_user=self._user.id_user,
                                        id_label = self._label.id_label if self.label else None,
                                        name = self._name,
                                        status = self._status,
                                        creation_date = self._creation_date,
                                        end_date = self._end_date ,
                                        description = self._description 
                                        )
            
            session.add(new_project_orm)
            session.commit()
            self._id_project = new_project_orm.id_project


    def delete(self):
        """
        Delete the project and its associated tasks. Also, removes the project from the
        associated user.
        """
        for task in self._tasks[:]:
            task.delete()

        self._user.remove_project(self)
        with self.SessionLocal() as session:
            project_to_delete = session.query(ProjectORM).filter(ProjectORM.id_project == self._id_project).first()
            if project_to_delete:
                session.delete(project_to_delete)
                session.commit()

    def update(self, **kwargs: Any) -> None:
        """
        Update the project's attributes based on the provided keyword arguments.

        This method updates the project's attrion-changeable
        and attempting to update them will raise an excepbutes based on the provided
        keyword arguments. Some properties like 'user', 'creation_date' and 'tasks' are ntion.

        Parameters:
            **kwargs (Any): Variable keyword arguments. Only allows updating certain
                            attributes of the project.

        Raises:
            NonChangeableProperty: If an attempt is made to change a non-modifiable
                                   property.
            ItemDontHaveThisAttribute: If an attribute to update does not exist in
                                   the Project class.
        """
        user = kwargs.get("user")
        creation_date = kwargs.get("creation_date")
        tasks = kwargs.get("tasks")
        if user or creation_date or tasks:
            raise NonChangeableProperty("You requested an update for a non-changeable property.")
        
        self.save_to_memento()
        with self.SessionLocal() as session:
            project_to_update = session.query(ProjectORM).filter(ProjectORM.id_project == self._id_project).first()
            if project_to_update:
                for key, value in kwargs.items():
                    attr_name = f"_{key}"
                    if hasattr(self, attr_name):
                        setattr(self, attr_name, value)
                        setattr(project_to_update, key, value)
                    else:
                        raise ItemDontHaveThisAttribute(f"Project does not have the attribute {key}.")

            session.commit()

    def add_task(self, task: IItem) -> None:
        """
        Add a task to the project.

        Parameters:
            task (IItem): The task item to be added to the project.
        """
        self._tasks.insert(0, task)

    def remove_task(self, task: IItem) -> None:
        """
        Remove a task from the project.

        Parameters:
            task (IItem): The task item to be removed from the project.
        """
        self._tasks.remove(task)

    def conclusion(self) -> None:
        """
        Mark the project as concluded and set the current date as the conclusion date.
        """
        self.save_to_memento()
        self._status = True
        self._conclusion_date = date.today()
        with self.SessionLocal() as session:
            project_to_update = session.query(ProjectORM).filter(ProjectORM.id_project == self._id_project).first()
            if project_to_update:
                project_to_update.status = self._status
                project_to_update.conclusion_date = self._conclusion_date
                session.commit()

    def unconclusion(self) -> None:
        """
        Revert the project's status to unconcluded and reset the conclusion date to None.
        """
        self.save_to_memento()
        self._status = False
        self._conclusion_date = None
        with self.SessionLocal() as session:
            project_to_update = session.query(ProjectORM).filter(ProjectORM.id_project == self._id_project).first()
            if project_to_update:
                project_to_update.status = self._status
                project_to_update.conclusion_date = self._conclusion_date
                session.commit()

    def save_to_memento(self):
        memento = ProjectMemento(
            self._name, 
            self._label, 
            self._end_date, 
            self._description, 
            self._status, 
            self._conclusion_date
        )
        self._mementos.append(memento)

    def has_memento(self):
        return bool(len(self._mementos) > 0)
    
    def restore_from_memento(self):
        if self._mementos:
            memento = self._mementos.pop()
            state = memento.get_state()

            self._name, self._label, self._end_date, \
            self._description, self._status, self._conclusion_date = state

            with self.SessionLocal() as session:
                project_to_update = session.query(ProjectORM).filter(ProjectORM.id_project == self._id_project).first()
                if project_to_update:
                    project_to_update.name = self._name
                    project_to_update.label = self._label
                    project_to_update.end_date = self._end_date
                    project_to_update.description = self._description
                    project_to_update.status = self._status
                    project_to_update.conclusion_date = self._conclusion_date
                    session.commit()
        else:
            print("Sem mementos para restaurar")  
    
    @property
    def tasks(self) -> List[IItem]:
        """List[IItem]: The list of tasks associated with this project."""
        return self._tasks

    @property
    def name(self) -> str:
        """str: The name of the project."""
        return self._name

    @property
    def label(self) -> IItem:
        """IItem: The label associated with the project."""
        return self._label

    @property
    def end_date(self) -> date:
        """date: The anticipated end date of the project."""
        return self._end_date

    @property
    def creation_date(self) -> date:
        """date: The date when the project was created."""
        return self._creation_date

    @property
    def conclusion_date(self) -> date:
        """date: The date when the project was concluded."""
        return self._conclusion_date

    @property
    def description(self) -> str:
        """str: A brief description of the project."""
        return self._description

    @property
    def status(self) -> bool:
        """bool: The status of the project, indicating whether it is concluded or not."""
        return self._status
    
    @property
    def id_project(self) -> int:
        """int: The id of the project."""
        return self._id_project