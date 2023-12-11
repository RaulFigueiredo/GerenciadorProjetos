"""
Module: subtask_update_page.py

This module defines the SubtaskUpdatePage class used to create the subtask update page.

Classes:
    SubtaskUpdatePage(BaseUpdatePage): Handles the creation of the subtask update page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, manager, mediator, subtask, parent):
Initializes the SubtaskUpdatePage instance.
    create_widgets(self): Creates widgets for the subtask update page.
    prepare_data(self): Prepares data to be sent to the server.

"""

import tkinter as tk
from src.gui.forms_base import EntryField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class SubtaskUpdatePage(BaseUpdatePage):
    """ This class will be used to create the subtask update page.

    Args:
        BaseUpdatePage (BaseUpdatePage): Base class for the update page
    """
    def __init__(
        self,
        master:tk,
        manager: object,
        mediator: object,
        subtask: callable,
        parent: object
    ) -> None:
        super().__init__(master, manager, mediator, subtask, parent)
        self.create_widgets()

    def create_widgets(self) -> None:
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)

        self.name_field.set_value(self.item.name if self.item.name is not None else '')

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server

        Returns:
            dict: The data to be sent to the server
        """
        data = {
            "name": self.name_field.get_value(),
        }
        return data
