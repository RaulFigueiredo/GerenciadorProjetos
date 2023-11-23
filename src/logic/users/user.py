from abc import ABC, abstractmethod
from typing import List
from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser


class User(IUser):
    _instance = None  # Variável de classe para armazenar a instância única

    def __new__(cls, name: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, name: str) -> None:
        if not self.__initialized:
            super().__init__(name)
            self._name = name
            self._labels: List[IItem] = []
            self._projects: List[IItem] = []
            self.__initialized = True

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


    

    