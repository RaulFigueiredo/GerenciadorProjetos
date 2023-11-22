from abc import ABC, abstractmethod
from typing import List
from src.logic.items.item_interface import IItem

class IUser(ABC):
    def __init__(self, name) -> None:
        self._name = name
        self._labels = List[IItem]
        self._projects = List[IItem]

    @abstractmethod
    def add_label(self, label: IItem) -> None: ...

    @abstractmethod
    def remove_label(self, label: IItem) -> None: ...

    @abstractmethod
    def add_project(self, project: IItem) -> None: ...

    @abstractmethod
    def remove_project(self, project: IItem) -> None: ...

    @property
    @abstractmethod
    def name(self) -> str: ...
    
    @property
    @abstractmethod
    def labels(self) -> List[IItem]: ...
    
    @property
    @abstractmethod
    def projects(self) -> List[IItem]: ...