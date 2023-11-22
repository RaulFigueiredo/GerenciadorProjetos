from src.logic.items.item_interface import IItem

class Label(IItem):
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
    