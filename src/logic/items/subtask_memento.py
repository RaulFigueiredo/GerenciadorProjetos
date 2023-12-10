from datetime import date
from typing import Optional
from src.logic.items.memento_interface import IMemento

class SubtaskMemento(IMemento):
    def __init__(self, name: str, status: bool, conclusion_date: Optional[date]):
        self._name = name
        self._status = status
        self._conclusion_date = conclusion_date

    def get_state(self):
        return self._name, self._status, self._conclusion_date
