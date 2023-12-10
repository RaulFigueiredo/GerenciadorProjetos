from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento

class TaskMemento(IMemento):
    def __init__(self,
                 name: str,
                 priority: Optional[str],
                 end_date: Optional[date],
                 notification_date: Optional[date],
                 description: Optional[str],
                 status: bool,
                 conclusion_date: Optional[date]):
        self._name = name
        self._priority = priority
        self._end_date = end_date
        self._notification_date = notification_date
        self._description = description
        self._status = status
        self._conclusion_date = conclusion_date

    def get_state(self):
        return (
                    self._name, 
                    self._priority, 
                    self._end_date, 
                    self._notification_date, 
                    self._description, 
                    self._status, 
                    self._conclusion_date
                )