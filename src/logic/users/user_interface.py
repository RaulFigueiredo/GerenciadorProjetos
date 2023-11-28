"""
This module defines an abstract base class (ABC) for user entities, following the
interface segregation principle. The class `IUser` serves as a blueprint
for various types of user entities in the application, enforcing a consistent
interface for essential user operations and properties.

Classes:
    IUser (ABC): An abstract base class that defines the common interface
    for all user types in the application. It declares abstract methods and properties
    that must be implemented by any concrete subclass. These include methods for
    managing labels and projects associated with the user, and properties for accessing
    the user's name, labels, and projects.
"""

from abc import ABC, abstractmethod
from typing import List
from src.logic.items.item_interface import IItem

class IUser(ABC):
    """
    An abstract base class that defines the common interface for user entities.

    This class serves as a contract that enforces implementation of methods and
    properties in any subclass. Methods include adding and removing labels and projects,
    and properties include the user's name, labels, and projects.

    Attributes:
        _name (str): The name of the user.
        _labels (List[IItem]): A list of labels associated with the user.
        _projects (List[IItem]): A list of projects associated with the user.

    Abstract Methods:
        add_label: To be implemented to handle adding a label to the user.
        remove_label: To be implemented to handle removing a label from the user.
        add_project: To be implemented to handle adding a project to the user.
        remove_project: To be implemented to handle removing a project from the user.
        Various abstract property getters for accessing user's attributes.
    """
    def __init__(self, name) -> None:
        self._name = name
        self._labels = List[IItem]
        self._projects = List[IItem]

    @abstractmethod
    def add_label(self, label: IItem) -> None:
        """
        Abstract method to be implemented in subclasses for adding a label to the user.

        This method should define the logic to add a label object to the user's collection
        of labels.

        Parameters:
            label (IItem): The label object to be added to the user.
        """

    @abstractmethod
    def remove_label(self, label: IItem) -> None:
        """
        Abstract method to be implemented in subclasses for removing a label from the user.

        Parameters:
            label (IItem): The label object to be removed from the user.
        """

    @abstractmethod
    def add_project(self, project: IItem) -> None:
        """
        Abstract method to be implemented in subclasses for adding a project to the user.

        Parameters:
            project (IItem): The project object to be added to the user.
        """

    @abstractmethod
    def remove_project(self, project: IItem) -> None:
        """
        Abstract method to be implemented in subclasses for removing a project from the user.

        Parameters:
            project (IItem): The project object to be removed from the user.
        """

    @property
    @abstractmethod
    def name(self) -> str:
        """ Abstract property to access the user's name. """

    @property
    @abstractmethod
    def labels(self) -> List[IItem]:
        """ Abstract property to access the list of labels associated with the user. """

    @property
    @abstractmethod
    def projects(self) -> List[IItem]:
        """ Abstract property to access the list of projects associated with the user."""
