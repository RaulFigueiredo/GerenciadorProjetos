from src.logic.items.item_interface import IItem
from src.logic.users.user_interface import IUser

class Label(IItem):
    def __init__(self, User: IUser, name: str, color: str) -> None:
        self._user = User
        self.name = name
        self.color = color

        self._user.add_label(self)

    def delete(self) -> None:
        self._user.remove_label(self)

    def update(self, **kwargs) -> None:
        if "task" in kwargs:
            raise ValueError("You requested an update for a non-changeable property.")

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Label does not have the attribute {key}.")

        self._user.update_label(self)
