"""
This module defines the Subtask class which extends functionalities from the IItem interface.
Subtasks are components of larger tasks and can be managed independently. The module includes
methods for creating, updating, deleting, and managing the status of a subtask. It also handles
exceptions specific to operations on subtasks.

Classes:
    Subtask: Represents a subtask, with methods for management and status update.

Exceptions:
    ItemDontHaveThisAttribute: Raised when an attribute is not found in the subtask.
    NonChangeableProperty: Raised when there's an attempt to change a non-changeable property.
"""

from src.logic.items.item_interface import IItem
from src.logic.items.subtask_memento import SubtaskMemento
from src.logic.execeptions.exceptions_items import ItemDontHaveThisAttribute, NonChangeableProperty
from datetime import date
from src.logic.orms.orm import SubtaskORM
from src.db.database import Database
from sqlalchemy.orm import sessionmaker


class Subtask(IItem):
    """
    Class for creating and managing subtasks.

    Attributes:
        task (IItem): The parent task this subtask is associated with.
        name (str): Name of the subtask.
        status (bool): Indicates whether the subtask is completed or not.

    Methods:
        delete(): Remove the subtask from its parent task.
        update(**kwargs): Update attributes of the subtask.
        conclusion(): Mark the subtask as completed.
        unconclusion(): Mark the subtask as not completed.
    """

    def __init__(self, task: IItem ,name: str, id_subtask: int = None,
                 status: bool = False, conclusion_date:date = None) -> None:
        """
        Initialize a Subtask instance.

        Args:
            task (IItem): The parent task to which the subtask belongs.
            name (str): The name of the subtask.
        """
        self._task = task
        self._name = name
        self._id_subtask = id_subtask
        self._status = status
        self._conclusion_date = conclusion_date
        self._mementos = []

        self._task.add_subtask(self)

        self.db = Database()
        self.SessionLocal = sessionmaker(bind=self.db.engine)

        if self._id_subtask == None:
            self.save_to_db()

    def save_to_db(self):
        with self.SessionLocal() as session:
            new_subtask_orm = SubtaskORM(id_task=self._task.id_task,
                                         name = self._name,
                                         status = self._status)
            session.add(new_subtask_orm)
            session.commit()
            self._id_subtask = new_subtask_orm.id_subtask

    def delete(self) -> None:
        """Remove the subtask from its parent task."""
        self._task.remove_subtask(self)
        with self.SessionLocal() as session:
            subtask_to_delete = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self._id_subtask).first()
            if subtask_to_delete:
                session.delete(subtask_to_delete)
                session.commit()

    def update(self, **kwargs) -> None:
        """
        Update attributes of the subtask.

        Args:
            **kwargs: Keyword arguments representing attributes to be updated.

        Raises:
            NonChangeableProperty: If an attempt is made to change a non-changeable attribute.
            ItemDontHaveThisAttribute: If the specified attribute does not exist.
        """
        task = kwargs.get("task")
        if task:
            raise NonChangeableProperty("You requested an update for a non-changeable property.")

        self.save_to_memento()
        
        with self.SessionLocal() as session:
            subtask_to_update = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self._id_subtask).first()
            if subtask_to_update:
                for key, value in kwargs.items():
                    attr_name = f"_{key}"
                    if hasattr(self, attr_name):
                        setattr(self, attr_name, value)
                        setattr(subtask_to_update, key, value)
                    else:
                        raise ItemDontHaveThisAttribute(f"Subtask does not have the attribute {key}.")
                session.commit()

    def conclusion(self) -> None:
        """Mark the subtask as completed."""
        self._status = True
        self._conclusion_date = date.today()
        with self.SessionLocal() as session:
            subtask_to_update = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self._id_subtask).first()
            if subtask_to_update:
                subtask_to_update.status = self._status
                subtask_to_update.conclusion_date = self._conclusion_date
                session.commit()
                
    def unconclusion(self) -> None:
        """Mark the subtask as not completed."""
        self._status = False
        self._conclusion_date = None
        with self.SessionLocal() as session:
            subtask_to_update = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self._id_subtask).first()
            if subtask_to_update:
                subtask_to_update.status = self._status
                subtask_to_update.conclusion_date = self._conclusion_date
                session.commit()

    def save_to_memento(self):
        memento = SubtaskMemento(self._name, self._status, self._conclusion_date)
        self._mementos.append(memento)

    # funçao para ver se existe algum memento
    def has_memento(self):
        return bool(len(self._mementos) > 0)
    
    def restore_from_memento(self):
        if self._mementos:
            name, status, conclusion_date = self._mementos.pop().get_state()
            self._name = name
            self._status = status
            self._conclusion_date = conclusion_date
            with self.SessionLocal() as session:
                subtask_to_update = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self._id_subtask).first()
                if subtask_to_update:
                    subtask_to_update.name = self._name
                    subtask_to_update.status = self._status
                    subtask_to_update.conclusion_date = self._conclusion_date
                    session.commit()
        else:
            print("No more states to revert to.")

    @property
    def status(self) -> bool:
        """bool: The completion status of the subtask."""
        return self._status

    @property
    def name(self) -> str:
        """str: The name of the subtask."""
        return self._name
    
    @property
    def task(self) -> IItem:
        """IItem: The parent task of the subtask."""
        return self._task
    
    @property
    def conclusion_date(self) -> date:
        return self._conclusion_date