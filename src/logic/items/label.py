"""
This module defines the Label class, which implements the IItem interface.
It represents a label with various attributes and methods to manage its
lifecycle within a user context.

Classes:
    Label: Represents a label with attributes and methods for label management.
    It allows creating, deleting, and updating labels, and is associated with
    a specific user.

Exceptions:
    ItemDontHaveThisAttribute: Raised when trying to update an attribute that doesn't
                               exist in the Label class.
    NonChangeableProperty: Raised when attempting to change a property that is not
                           allowed to be modified.
"""

from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser
from src.logic.execeptions.exceptions_items import  ItemDontHaveThisAttribute,\
                                                    NonChangeableProperty

class Label(IItem):
    """
    A class to represent a label, implementing the IItem interface.

    Attributes:
        _user (IUser): The user associated with the label.
        _name (str): The name of the label.
        _color (str): The color of the label.

    Methods:
        delete: Deletes the label and removes it from the associated user.
        update: Updates the label's attributes, except for non-changeable properties.
        Various property getters and setters for accessing and modifying label attributes.
    """

    def __init__(self, user: IUser, name: str, color: str) -> None:
        """
        Initialize a new Label object with given parameters.

        Parameters:
            User (IUser): The user associated with the label.
            name (str): The name of the label.
            color (str): The color of the label.
        """
        self._user = user
        self._name = name
        self._color = color

        self._user.add_label(self)

    def delete(self) -> None:
        """
        Delete the label and remove it from the associated user.
        """
        self._user.remove_label(self)
        # deleta do banco de dados

    def update(self, **kwargs) -> None:
        """
        Update the label's attributes based on the provided keyword arguments.

        This method updates the label's attributes based on the provided keyword arguments.
        Some properties such as 'user' are non-changeable, and attempting to update them
        will raise an exception.

        Parameters:
            **kwargs (Any): Variable keyword arguments for updating label attributes.

        Raises:
            NonChangeableProperty: If an attempt is made to change a non-modifiable property.
            ItemDontHaveThisAttribute: If an attribute to update does not exist in the Label class.
        """
        if "user" in kwargs:
            raise NonChangeableProperty("You requested an update for a non-changeable property.")

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ItemDontHaveThisAttribute(f"Label does not have the attribute {key}.")

        self._user.update_label(self)

    @property
    def user(self) -> IUser:
        """IUser: The user associated with the label."""
        return self._user

    @property
    def name(self) -> str:
        """str: The name of the label."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def color(self) -> str:
        """str: The color of the label."""
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value