"""
This module defines an abstract base class (ABC) for items, following the
interface segregation principle. The class `IItem` serves as a blueprint
for various types of items in the application, enforcing a consistent
interface for essential item operations.

Classes:
    IItem (ABC): An abstract base class that defines the common interface
    for all item types in the application. It declares abstract methods
    that must be implemented by any concrete subclass. These methods
    include `delete`, `update`, ensuring a consistent set of operations
    across different item types.
"""

from abc import ABC, abstractmethod

class IItem(ABC):
    """
    An abstract base class that defines the common interface for item entities.

    This class serves as a contract that enforces implementation of
    the `delete` and `update` methods in any subclass. The `delete` method is
    intended for removing an item, and the `update` method is for modifying
    item attributes dynamically.

    Methods:
        delete(self): An abstract method that should be implemented to handle the deletion
                      of an item.

        update(self, **kwargs): An abstract method that should be implemented to handle the
                                updating of an item's attributes.
    """
    @abstractmethod
    def delete(self) -> None:
        """
        Abstract method to be implemented in subclasses for item deletion.
        """


    @abstractmethod
    def update(self, **kwargs) -> None:
        """
        Abstract method to be implemented in subclasses for updating item attributes.

        Parameters:
            **kwargs: Variable keyword arguments representing the attributes and their new values
                      that need to be updated on the item.
        """

    @abstractmethod
    def has_memento(self) -> bool:
        """
        Abstract method to be implemented in subclasses for checking if the item has memento.
        """
    
    @abstractmethod
    def restore_from_memento(self) -> None:
        """
        Abstract method to be implemented in subclasses for restoring item from memento.
        """
