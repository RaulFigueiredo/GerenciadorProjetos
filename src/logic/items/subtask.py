from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import ItemDontHaveThisAttribute, NonChangeableProperty


class Subtask(IItem):
    def __init__(self, task: IItem ,name: str) -> None:
        self._task = task
        self._name = name
        self._status = False

        self._task.add_subtask(self)

    def delete(self):
        self._task.remove_subtask(self)

    def update(self, **kwargs) -> None:
        task = kwargs.get("task")
        if task:
            raise NonChangeableProperty("You requested an update for a non-changeable property.")
        for key, value in kwargs.items():
            attr_name = f"_{key}"
            if hasattr(self, attr_name):
                setattr(self, attr_name, value)
            else:
                raise ItemDontHaveThisAttribute(f"Subtask nao tem o atributo {key}.")
            # atualizar no banco de dados
    
    def conclusion(self) -> None:
        self._status = True
        # atualizar no banco de dados

    def unconclusion(self) -> None:
        self._status = False
        # atualizar no banco de dados
        
    @property
    def status(self) -> bool:
        return self._status
    
    @property
    def name(self) -> str:
        return self._name