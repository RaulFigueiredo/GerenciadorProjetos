"""
Module: subtask_create_page.py

This module defines the SubtaskCreatePage class used for creating subtask creation pages.

Classes:
    SubtaskCreatePage(BaseCreatePage): Handles the creation of subtask creation pages.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, mediator, parent): Initializes the SubtaskCreatePage instance.
    create_widgets(self): Creates widgets for the subtask creation page.
    prepare_data(self): Prepares data to be sent to the server.

"""

import tkinter as tk

from src.gui.forms_base import EntryField
from src.gui.base_CRUD.base_create_page import BaseCreatePage

class SubtaskCreatePage(BaseCreatePage):
    """ This class will be used to create the subtask creation page.

    Args:
        BaseCreatePage (_type_): Base class for the creation page
    """
    def __init__(self, master: tk, mediator: object, parent: object) -> None:
        super().__init__(master, mediator, parent)
        self.create_widgets()

    def create_widgets(self) -> None:
        """ This method will be used to create the widgets.
        """
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Criar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server

        Returns:
            dict: The data to be sent to the server
        """
        data = {
            "item_type": "subtask",
            "task": self.parent,
            "name": self.name_field.get_value()
        }

        return data
