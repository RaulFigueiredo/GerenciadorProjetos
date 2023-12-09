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
from src.logic.orms.orm import LabelORM
from src.db.database import Database
from sqlalchemy.orm import sessionmaker
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

    def __init__(self, user: IUser, name: str,color: str, id_label: int = None) -> None:
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
        self._id_label = id_label

        self._user.add_label(self)

        self.db = Database()
        self.SessionLocal = sessionmaker(bind=self.db.engine)

        if not self._id_label:
            self.save_to_db()

    def save_to_db(self):
        with self.SessionLocal() as session:
            new_label_orm = LabelORM(  id_user=self._user.id_user,
                                        name = self._name,
                                        color = self._color,
                                        )
            
            session.add(new_label_orm)
            self._id_label = new_label_orm.id_label
            session.commit()

    def delete(self) -> None:
        """
        Delete the label and remove it from the associated user.
        """
        self._user.remove_label(self)
        with self.SessionLocal() as session:
            label_to_delete = session.query(LabelORM).filter(LabelORM.id_label == self._id_label).first()
            if label_to_delete:
                session.delete(label_to_delete)
                session.commit()

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

        with self.SessionLocal() as session:
            label_to_update = session.query(LabelORM).filter(LabelORM.id_label == self._id_label).first()
            if label_to_update:
                for key, value in kwargs.items():
                    attr_name = f"_{key}"
                    if hasattr(self, attr_name):
                        setattr(self, attr_name, value)
                        setattr(label_to_update, key, value)
                    else:
                        raise ItemDontHaveThisAttribute(f"Label does not have the attribute {key}.")
            session.commit()

    @property
    def user(self) -> IUser:
        """IUser: The user associated with the label."""
        return self._user

    @property
    def name(self) -> str:
        """str: The name of the label."""
        return self._name
    
    @property
    def color(self) -> str:
        """str: The color of the label."""
        return self._color

    @property
    def id_label(self) -> int:
        """int: The id of the label."""
        return self._id_label