"""
This module provides the `Task` class, an implementation of the `IItem`
interface. It is designed for managing tasks within a project management
context. The module offers functionalities to create, update, delete, and
track tasks, including their subtasks. Tasks have attributes like priority,
end date, and description, and maintain a completion status.

Classes:
    Task: Represents a task within a project, with methods for its lifecycle
    and properties.

Exceptions:
    ItemDontHaveThisAttribute: Exception for attribute errors in tasks.
    NonChangeableProperty: Exception for unmodifiable task properties.
"""

from typing import List, Any
from datetime import date
from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import  ItemDontHaveThisAttribute,\
                                                    NonChangeableProperty
from src.logic.orms.orm import TaskORM
from src.db.database import Database
from sqlalchemy.orm import sessionmaker
class Task(IItem):
    """
    Represents a task in a project management system.

    This class provides methods to create, delete, update, and manage tasks. Tasks can
    have attributes like priority, end dates, notifications, list of subtasks, description,
    and a status indicating completion.

    Attributes:
        _project (IItem): The project to which this task belongs.
        _name (str): The name of the task.
        _priority (str, optional): The priority of the task. Defaults to None.
        _end_date (date, optional): The date the task is expected to end. Defaults to None.
        _notification_date (date, optional): The date for sending a notification about the task.
                                             Defaults to None.
        _description (str, optional): A description of the task. Defaults to None.
        _creation_date (date): The date the task was created.
        _conclusion_date (date, optional): The date the task was concluded. Defaults to None.
        _status (bool): The status of the task, where False indicates incomplete and
                        Trueindicates complete.
        _subtasks (List[IItem]): A list of subtasks under this task.

    Methods:
        delete: Deletes the task and its subtasks from the project.
        update: Updates the task's attributes except for project, creation_date, and subtasks.
        add_subtask: Adds a subtask to the task.
        remove_subtask: Removes a subtask from the task.
        conclusion: Marks the task as concluded.
        unconclusion: Reverts the task to an unconcluded state.
        Various property getters for accessing task attributes.
    """

    def __init__(self,  project: IItem, name: str, id_task: int = None, priority: str = None,
                 end_date: date = None, notification_date: date = None, description: str = None,
                 conclusion_date:date = None, status: bool = False, creation_date: date = None) -> None:
        """
        Initializes a new Task object with given parameters.

        Parameters:
            project (IItem): The project to which this task belongs.
            name (str): The name of the task.
            priority (str, optional): The priority of the task. Defaults to None.
            end_date (date, optional): The anticipated end date of the task. The default is None.
            notification_date (date, optional): The date for sending a notification about the task.
                                                Defaults to None.
            description (str, optional): A description of the task. Defaults to None.
        """
        self._project = project
        self._name = name
        self._priority = priority
        self._description = description
        self._end_date = end_date
        self._notification_date = notification_date
        self._id_task = id_task
        self._creation_date = creation_date if creation_date else date.today()
        self._conclusion_date = conclusion_date
        self._status = status
        self._subtasks: List[IItem] = []

        self._project.add_task(self)

        self.db = Database()
        self.SessionLocal = sessionmaker(bind=self.db.engine)

        if not self._id_task:
            self.save_to_db()

    def save_to_db(self):
        with self.SessionLocal() as session:
            new_task_orm = TaskORM( id_project=self._project.id_project,
                                    name = self._name,
                                    status = self._status,
                                    creation_date = self._creation_date,
                                    priority = self._priority,
                                    end_date = self._end_date,
                                    notification_date = self._notification_date,
                                    description = self._description
                                    )
            
            session.add(new_task_orm)
            session.commit()
            self._id_task = new_task_orm.id_task


    """
    - step 1 
    def delete(self):
        pass
        
    - step 2
    def delete(self):
        self._project.remove_task(self)
    
    - step 3
    def delete(self):
        self._subtasks.remove_subtask(subtask)
        self._project.remove_task(self)

    - step 4
    def delete(self):
        self._subtasks = []
        self._project.remove_task(self)

    - step 5
    def delete(self):
        self._subtasks[0].delete()
        self._subtasks[1].delete()
        self._project.remove_task(self)

    - step 6
    def delete(self):
        for subtask in self._subtasks[:]:
            subtask.delete()
        self._project.remove_task(self)
    """ 
    # refactor
    def delete(self) -> None:
        """
        Deletes the task and its subtasks from the project.
        """
        for subtask in self._subtasks[:]:
            subtask.delete()
        self._project.remove_task(self)
        with self.SessionLocal() as session:
            task_to_delete = session.query(TaskORM).filter(TaskORM.id_task == self._id_task).first()
            if task_to_delete:
                session.delete(task_to_delete)
                session.commit()
    """
    - step 1
    def update(self) -> None:
        pass
        
    - step 2
    def update(self, name, priority)-> None:
        self._name = name
        self._priority = priority

    - step 3
    def update(self, name, priority, end_date, notification_date, description,
            status) -> None:
        self._name = name
        self._priority = priority
        self._end_date = end_date
        self._notification_date = notification_date
        self._description = description
        self._status = status

    - step 4
    def update(self, name = None, priority = None, end_date = None,
            notification_date = None, description = None, status= None) -> None:
        if name:
            self._name = name
        if priority:
            self._priority = priority
        if end_date:
            self._end_date = end_date
        if notification_date:
            self._notification_date = notification_date
        if description:
            self._description = description
        if status:
            self._status = status
    """

    # refactor
    def update(self, **kwargs: Any) -> None:
        """
        Updates the task's attributes.

        This method updates the task's attrion-changeable
        and attempting to update them will raise an excepbutes based on the provided keyword
        arguments. Some properties like 'project', 'creation_date', and 'subtasks' are ntion.

        Parameters:
            kwargs (Any): Keyword arguments representing the attributes to update.

        Raises:
            NonChangeableProperty: If an attempt is made to update a non-changeable property.
            ItemDontHaveThisAttribute: If an attribute to update does not exist in the Task.
        """
        project = kwargs.get("project", None)
        creation_date = kwargs.get("creation_date", None)
        subtasks = kwargs.get("subtasks", None)

        if project or creation_date or subtasks:
            raise NonChangeableProperty('You requested an update for a non-changeable property.')

        with self.SessionLocal() as session:
            task_to_update = session.query(TaskORM).filter(TaskORM.id_task == self._id_task).first()
            if task_to_update:
                for key, value in kwargs.items():
                    attr_name = f"_{key}"
                    if hasattr(self, attr_name):
                        setattr(self, attr_name, value)
                        setattr(task_to_update, key, value)
                    else:
                        raise ItemDontHaveThisAttribute(f"Task does not have the attribute {key}.")
            session.commit()

    def add_subtask(self, subtask: IItem) -> None:
        """
        Adds a subtask to this task.

        Args:
            subtask (IItem): The subtask to be added.
        """
        self._subtasks.insert(0, subtask)

    def remove_subtask(self, subtask: IItem) -> None:
        """
        Removes a subtask from this task.

        Args:
            subtask (IItem): The subtask to be removed.
        """
        self._subtasks.remove(subtask)

    def conclusion(self) -> None:
        """
        Marks the task as concluded.

        Sets the task's status to True and records the conclusion date.
        """
        self._status = True
        self._conclusion_date = date.today()
        with self.SessionLocal() as session:
            task_to_update = session.query(TaskORM).filter(TaskORM.id_task == self._id_task).first()
            if task_to_update:
                task_to_update.status = self._status
                task_to_update.conclusion_date = self._conclusion_date
                session.commit()

    def unconclusion(self) -> None:
        """
        Reverts the task to an unconcluded state.

        Sets the task's status to False and resets the conclusion date.
        """
        self._status = False
        self._conclusion_date = None
        with self.SessionLocal() as session:
            task_to_update = session.query(TaskORM).filter(TaskORM.id_task == self._id_task).first()
            if task_to_update:
                task_to_update.status = self._status
                task_to_update.conclusion_date = self._conclusion_date
                session.commit()

    @property
    def subtasks(self) -> List[IItem]:
        """List[IItem]: The list of subtasks associated with this task."""
        return self._subtasks

    @property
    def name(self) -> str:
        """str: The name of the task."""
        return self._name

    @property
    def priority(self) -> str:
        """str: The priority of the task."""
        return self._priority

    @property
    def end_date(self) -> date:
        """date: The date marked as the end of the task."""
        return self._end_date

    @property
    def creation_date(self) -> date:
        """date: The date when the task was created."""
        return self._creation_date

    @property
    def conclusion_date(self) -> date:
        """date: The date when the task was concluded."""
        return self._conclusion_date

    @property
    def description(self) -> str:
        """str: A description of the task."""
        return self._description

    @property
    def status(self) -> bool:
        """bool: The completion status of the task."""
        return self._status

    @property
    def project(self) -> IItem:
        """IItem: The project associated with this task."""
        return self._project

    @property
    def notification_date(self) -> date:
        """date: The date when a notification for this task should be sent."""
        return self._notification_date

    @property
    def id_task(self) -> int:
        """int: The id of the task."""
        return self._id_task