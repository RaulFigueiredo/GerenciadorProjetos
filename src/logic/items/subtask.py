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
from src.logic.execeptions.exceptions_items import ItemDontHaveThisAttribute, NonChangeableProperty


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

    def __init__(self, task: IItem ,name: str):
        """
        Initialize a Subtask instance.

        Args:
            task (IItem): The parent task to which the subtask belongs.
            name (str): The name of the subtask.
        """
        self._task = task
        self._name = name
        self._status = False

        self._task.add_subtask(self)

    def delete(self) -> None:
        """Remove the subtask from its parent task."""
        self._task.remove_subtask(self)
        # remover do banco de dados

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
        for key, value in kwargs.items():
            attr_name = f"_{key}"
            if hasattr(self, attr_name):
                setattr(self, attr_name, value)
            else:
                raise ItemDontHaveThisAttribute(f"Subtask does not have the attribute {key}.")
            # atualizar no banco de dados

    def conclusion(self) -> None:
        """Mark the subtask as completed."""
        self._status = True
        # atualizar no banco de dados

    def unconclusion(self) -> None:
        """Mark the subtask as not completed."""
        self._status = False
        # atualizar no banco de dados

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