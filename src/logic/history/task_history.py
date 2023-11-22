"""
    This file contains the classes and methods used to create
    the interface for the history of completed tasks.

    Classes:
        HistoryInterface(ABC): Abstract Base Class
        HistorySingleton(HistoryInterface): Interface of the history of completed tasks,
        used to create a singleton instance of the class.

    Methods:
        add_completed_task(self, project: Item) -> None: Adds a completed task to the list
        tasks_completed(self) -> List[Item]: List of completed tasks
"""

from abc import ABC, abstractmethod
from typing import List
from src.logic.items.item_interface import IItem

class HistoryInterface(ABC):
    """ This class will be used to represent the interface history of completed tasks

    Args:
        ABC (): Abstract Base Class
    """
    @abstractmethod
    def add_completed_task(self, project: IItem) -> None:
        """ This method will be used to add a completed task to the list

        Args:
            task_name (Item): Adds a completed task to the list
        """

    @abstractmethod
    def tasks_completed(self) -> List[IItem]:
        """ This method will be used to return the list of completed tasks
        """

class HistorySingleton(HistoryInterface):
    """ This class will be used to represent the history of completed tasks

    Args:
        HistoryInterface (HistoryInterface): Interface of the history of completed tasks
    """
    _instance = None

    def __new__(cls) -> object:
        """ Creates and manages a singleton instance of the class.

        Args:
            cls (object): The class that will be used to create the singleton instance.

        Returns:
            object: The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tasks_list = []
        return cls._instance

    def add_completed_task(self, project: IItem) -> None:
        """ This method will be used to add a completed task to the list

        Args:
            project (Item): List of projects
        """
        for each_project in project:
            for each_task in each_project.tasks:
                if each_task.get_status:
                    self._instance.tasks_list.append(each_task)

    def tasks_completed(self) -> List[IItem]:
        """ This method will be used to return the list of completed tasks

        Returns:
            List[Item]: List of completed tasks
        """
        #return self._instance.tasks_list
        return self._instance.tasks_list
