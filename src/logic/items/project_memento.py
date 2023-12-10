from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento
from src.logic.items.item_interface import IItem

class ProjectMemento(IMemento):
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