from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser
from datetime import date
from typing import List


class Project(IItem):
    def __init__(self, user: IUser ,name: str, label: IItem = None,
                 end_date: date = None, description: str = None) -> None:
        
        self._user = user
        self._name = name
        self._label = label
        self._end_date = end_date
        self._description = description
        self._creation_date = date.today()
        self._conclusion_date = None
        self._status = False
        self._tasks: List[IItem] = [] 

        self._user.add_project(self)

    def delete(self):
        for task in self._tasks[:]:
            task.delete()

        self._user.remove_project(self)
        # remover do banco de dados

    def update(self, name: str = None, label: IItem = None, end_date: date = None,
                description: str = None, status: bool = None, conclusion_date: date = None) -> None:
          if name:
                self._name = name
          if label:
                self._label = label
          if end_date:
                self._end_date = end_date
          if description:
                self._description = description
          if status:
                self._status = status
          if conclusion_date:
                self._conclusion_date = conclusion_date
          # atualizar no banco de dados

    def add_task(self, task: IItem) -> None:
        self._tasks.append(task)
        # adicionar no banco de dados 

    def remove_task(self, task: IItem) -> None:
        self._tasks.remove(task)
        # remover do banco de dados

    @property
    def tasks(self) -> List[IItem]:
        return self._tasks
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def label(self) -> IItem:
        return self._label
    
    @property
    def end_date(self) -> date:
        return self._end_date
    
    @property
    def creation_date(self) -> date:
        return self._creation_date
    
    @property
    def conclusion_date(self) -> date:
        return self._conclusion_date
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def status(self) -> bool:
        return self._status