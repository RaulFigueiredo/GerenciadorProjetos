from abc import ABC, abstractmethod

class IItem(ABC):
    @abstractmethod
    def delete(self) -> None: ...

    @abstractmethod
    def update(self, **kwargs) -> None: ...

    # undo fica aqui, assim controlo esse padrao em todos os items
        
