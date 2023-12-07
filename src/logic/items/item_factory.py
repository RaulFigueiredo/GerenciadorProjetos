"""
This module defines the ItemFactory class, which is responsible for creating
different types of item objects such as Project, Task, Subtask, and Label.
The factory ensures that the created items have unique names within their
respective collections and are correctly instantiated according to their type.

Classes:
    ItemFactory: A class with a static method to create various types of item objects.
    The method checks for name uniqueness and instantiates the appropriate item
    object based on the item type.

Exceptions:
    ItemNameBlank: Raised when the 'name' argument is missing, null, or empty for an item.
    ItemNameAlreadyExists: Raised when an item with the provided name already exists
    within the collection it belongs to.
    UnknownItem: Raised when the item type to be created is unknown or unsupported.
"""

from typing import Any
from src.logic.items.item_interface import IItem
from src.logic.items.project import Project
from src.logic.items.subtask import Subtask
from src.logic.items.task import Task
from src.logic.items.label import Label
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    UnknownItem

class ItemFactory:
    """
    A factory class for creating various types of item objects.

    This class contains a static method that takes an item type and keyword arguments
    to create and return an object of the specified item type. It ensures that each
    created item has a unique name within its respective collection (e.g., projects,
    tasks) and throws relevant exceptions if the creation criteria are not met.

    Static Methods:
        create_item(item_type: str, **kwargs: Any): Creates and returns an item object
        of the specified type.
    """

    @staticmethod
    def create_item(item_type: str, **kwargs: Any) -> IItem:
        """
        Create and return an item object of the specified type.

        This static method is responsible for creating item objects such as Project,
        Task, Subtask, or Label. It validates the 'name' parameter to ensure it is
        neither null nor empty and checks for name uniqueness within the collection
        relevant to the item type. Appropriate exceptions are raised in case of validation
        failures.

        Parameters:
            item_type (str): The type of item to be created. Accepted values are 'project',
                             'task', 'subtask', and 'label'.
            **kwargs (Any): Variable keyword arguments containing the data necessary
                            for creating the item. Common arguments include 'name',
                            and depending on the item type, 'user', 'project', or 'task'.

        Raises:
            ItemNameBlank: If the 'name' argument is missing, null, or empty.
            ItemNameAlreadyExists: If an item with the provided name already exists
                                    in the respective collection (e.g., a project with the
                                    same name in the user's project list).
            UnknownItem: If the specified item type is not recognized.

        Returns:
            IItem: An instance of the specified item type, fully initialized with the
                   provided arguments.
        """
        name = kwargs.get('name')
        if name is None or name == '':
            erro_str = "Campo 'nome' é obrigatório"
            raise ItemNameBlank(erro_str)

        if item_type == 'project':
            user = kwargs.get('user')
            if name in [project.name for project in user.projects]:
                erro_str = "Já existe um projeto com esse nome"
                raise ItemNameAlreadyExists(erro_str)
            return Project(**kwargs)

        if item_type == 'task':
            project = kwargs.get('project')
            if name in [task.name for task in project.tasks]:
                erro_str = "Já existe uma tarefa com esse nome nesse projeto"
                raise ItemNameAlreadyExists(erro_str)
            return Task(**kwargs)

        if item_type == 'subtask':
            task = kwargs.get('task')
            if name in [subtask.name for subtask in task.subtasks]:
                erro_str = "Já existe uma subtarefa com esse nome nessa tarefa"
                raise ItemNameAlreadyExists(erro_str)
            return Subtask(**kwargs)

        if item_type == 'label':
            user = kwargs.get('user')
            if name in [label.name for label in user.labels]:
                erro_str = "Já existe uma etiqueta com esse nome"
                raise ItemNameAlreadyExists(erro_str)
            return Label(**kwargs)

        raise UnknownItem("Tipo de item desconhecido")
        