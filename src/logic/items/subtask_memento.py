"""
Module Name: Subtask Memento

Description:
This module contains the SubtaskMemento class responsible for creating a memento object
specifically for subtasks.

- SubtaskMemento inherits from the IMemento interface.
- It encompasses essential attributes like name, status, and conclusion date 
  related to subtasks.

Methods:
- __init__(): Initializes a SubtaskMemento object with specific subtask details.
- get_state(): Retrieves the state of the memento, returning a tuple containing 
  subtask attributes.

The SubtaskMemento class acts as a representation of a subtask's state at a particular time, 
allowing for the capture of critical details to facilitate restoration or tracking of changes.
"""


from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento

class SubtaskMemento(IMemento):
    """ This class represents a memento for a subtask.

    Args:
        IMemento (IMemento): The interface for the memento.
    """
    def __init__(self, name: str, status: bool, conclusion_date: Optional[date]):
        self._name = name
        self._status = status
        self._conclusion_date = conclusion_date

    def get_state(self) -> tuple:
        """ Returns the state of the memento.

        Returns:
            tuple: The state of the memento.
        """
        return self._name, self._status, self._conclusion_date
