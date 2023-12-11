"""
Module Name: Task Memento

Description:
This module contains the TaskMemento class used to create a memento object for tasks.

- The TaskMemento class inherits from the IMemento base class.
- Attributes include various task-related details like name, priority, dates, description, 
  status, and conclusion date.

Methods:
- __init__(): Initializes a TaskMemento object with specific task details.
- get_state(): Retrieves the state of the memento, returning a tuple comprising task 
  attributes.

The TaskMemento class serves as a representation of a task's state at a particular time, 
capturing essential details to facilitate restoration or tracking of changes.
"""


from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento

class TaskMemento(IMemento):
    """ This class will be used to create the task memento.

    Args:
        IMemento (_type_): Base class for the memento
    """
    def __init__(self,
                 name: str,
                 priority: Optional[str],
                 end_date: Optional[date],
                 notification_date: Optional[date],
                 description: Optional[str],
                 status: bool,
                 conclusion_date: Optional[date]
    ) -> None:
        self._name = name
        self._priority = priority
        self._end_date = end_date
        self._notification_date = notification_date
        self._description = description
        self._status = status
        self._conclusion_date = conclusion_date

    def get_state(self) -> tuple:
        """ Returns the state of the memento.

        Returns:
            tuple: State of the memento
        """
        return (
                    self._name,
                    self._priority,
                    self._end_date,
                    self._notification_date,
                    self._description,
                    self._status,
                    self._conclusion_date
                )
