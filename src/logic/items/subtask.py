from src.logic.items.item_interface import IItem


class Subtask(IItem):
    def __init__(self, task: IItem ,name: str, color: str) -> None:
        self._task = task
        self._name = name
        self._color = color

        self._task.add_subtask(self)

    def delete(self):
        self._task.remove_subtask(self)

    def update(self, name = None, color = None) -> None:
        if name:
            self._name = name
        if color:
            self._color = color
        # atualizar no banco de dados

    @property
    def color(self) -> str:
        return self._color
    
    @property
    def name(self) -> str:
        return self._name