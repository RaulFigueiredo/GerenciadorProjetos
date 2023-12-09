"""
This module defines the User class, which is an implementation of the IUser interface.
The User class is designed as a singleton, ensuring that only one instance of the user
exists within the application context. It provides methods for managing labels and
projects associated with the user, as well as properties to access the user's attributes.

Classes:
    User (IUser): A singleton class that implements the IUser interface. It provides
    functionality to manage user-specific data such as labels and projects. The User
    class allows adding and removing labels and projects, and provides access to the
    user's name, labels, and projects.

Note:
    The User class follows the Singleton design pattern to ensure that only a single
    instance of the User exists in the application.
"""

from typing import List
from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser
from src.logic.orms.orm import UserORM
from src.db.database import Database
from sqlalchemy.orm import sessionmaker

class User(IUser):
    """
    A singleton class that implements the IUser interface, representing a user in the application.

    This class ensures that only one instance of a user exists within the application context.
    It provides methods for managing labels and projects associated with the user, as well as
    properties to access the user's name, labels, and projects. The class is designed to be
    initialized only once; subsequent attempts to instantiate it will return the existing instance.

    Attributes:
        _instance (User): A class-level attribute that holds the singleton instance of the User.
        _name (str): The name of the user.
        _labels (List[IItem]): A list of labels associated with the user.
        _projects (List[IItem]): A list of projects associated with the user.

    Methods:
        __new__: A class method to control the instantiation of the User class, ensuring it follows
                 the singleton pattern.
        __init__: Initializes the User instance with a name, labels, and projects. This method is
                  designed to run only once.
        add_label: Adds a label to the user's collection of labels.
        remove_label: Removes a label from the user's collection of labels.
        add_project: Adds a project to the user's collection of projects.
        remove_project: Removes a project from the user's collection of projects.
        Various property getters for accessing user attributes.
    """
    _instance = None

    def __new__(cls, name: str, id_user: int) -> IUser:
        """
        Control the instantiation of the User class, ensuring it follows the singleton pattern.

        This method checks if an instance of the class already exists. If not, it creates a new
        instance. If an instance already exists, it returns the existing instance, ignoring
        further initialization attempts.

        Parameters:
            name (str): The name of the user. Used during the first initialization of the instance.

        Returns:
            User: The singleton instance of the User class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name: str, id_user: int = None) -> None:
        """
        Initialize the User instance.

        This method is designed to run only once. It sets up the user's name, labels, and projects.
        Subsequent attempts to initialize an instance of this class will not reinitialize these
        attributes.

        Parameters:
            name (str): The name of the user.
        """
        if not self._initialized:
            super().__init__(name)
            self._name = name
            self._labels: List[IItem] = []
            self._projects: List[IItem] = []
            self._initialized = True
            self._id_user = id_user

            self.db = Database()
            self.SessionLocal = sessionmaker(bind=self.db.engine)

            if not self._id_user:
                self.seve_to_db()

    def seve_to_db(self):
        with self.SessionLocal() as session:
            new_user_orm = UserORM(name=self._name)
            session.add(new_user_orm)
            self._id_user = new_user_orm.id_user
            session.commit()


    def add_label(self, label: IItem) -> None:
        """
        Add a label to the user's collection of labels.

        Parameters:
            label (IItem): The label to be added to the user's collection.
        """
        self._labels.insert(0, label)
        # adicionar no banco de dados

    def remove_label(self, label: IItem) -> None:
        """
        Remove a label from the user's collection of labels.

        Parameters:
            label (IItem): The label to be removed from the user's collection.
        """
        self._labels.remove(label)

    def add_project(self, project: IItem) -> None:
        """
        Add a project to the user's collection of projects.

        Parameters:
            project (IItem): The project to be added to the user's collection.
        """
        self._projects.insert(0,project)

    def remove_project(self, project: IItem) -> None:
        """
        Remove a project from the user's collection of projects.

        Parameters:
            project (IItem): The project to be removed from the user's collection.
        """
        self._projects.remove(project)

    @property
    def name(self) -> str:
        """
        Return the name of the user.

        Returns:
            str: The name of the user.
        """
        return self._name

    @property
    def labels(self) -> List[IItem]:
        """
        Return the list of labels associated with the user.

        Returns:
            List[IItem]: A list of labels associated with the user.
        """
        return self._labels

    @property
    def projects(self) -> List[IItem]:
        """
        Return the list of projects associated with the user.

        Returns:
            List[IItem]: A list of projects associated with the user.
        """
        return self._projects
    
    @property
    def id_user(self) -> int:
        return self._id_user
