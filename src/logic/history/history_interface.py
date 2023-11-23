"""
    This file contains the classes and methods used to create
    the interface for the history of completed tasks.

    Classes:
        HistoryInterface(ABC): Abstract Base Class
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
