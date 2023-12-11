"""
Module Name: Project Memento

Description:
This module includes the ProjectMemento class, responsible for creating a memento object 
specifically tailored for projects.

- ProjectMemento inherits from the IMemento interface.
- It encapsulates critical attributes such as name, label, end date, description, 
  status, and conclusion date related to projects.

Methods:
- __init__(): Initializes a ProjectMemento object with specific project details.
- get_state(): Retrieves the state of the memento, returning a tuple containing 
  project attributes.

The ProjectMemento class serves as a representation of a project's state at a particular time, 
enabling the capture of essential project details to support restoration or tracking of changes.
"""

from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento
from src.logic.items.item_interface import IItem

class ProjectMemento(IMemento):
    """ This class represents a memento for a project.

    Args:
        IMemento (IMemento): The interface for the memento.
    """
    def __init__(self,
                 name: str,
                 label: Optional[IItem],
                 end_date: Optional[date],
                 description: Optional[str],
                 status: bool,
                 conclusion_date: Optional[date]):

        self._name = name
        self._label = label
        self._end_date = end_date
        self._description = description
        self._status = status
        self._conclusion_date = conclusion_date

    def get_state(self):
        return (
            self._name,
            self._label,
            self._end_date,
            self._description,
            self._status,
            self._conclusion_date
        )
