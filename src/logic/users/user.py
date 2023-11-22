from abc import ABC, abstractmethod
from typing import List
from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser


class User(IUser):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._labels: List[IItem] = []
        self._projects: List[IItem] = []

    def add_label(self, label: IItem) -> None:
        self._labels.append(label)
        # adicionar no banco de dados 

    def remove_label(self, label: IItem) -> None:
        self._labels.remove(label)
        # remover do banco de dados

    def add_project(self, project: IItem) -> None:
        self._projects.append(project)
        # adicionar no banco de dados 

    def remove_project(self, project: IItem) -> None:
        self._projects.remove(project)
        # remover do banco de dados

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def labels(self) -> List[IItem]:
        return self._labels
    
    @property
    def projects(self) -> List[IItem]:
        return self._projects


    

    