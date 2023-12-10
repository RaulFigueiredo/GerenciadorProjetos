"""
Module: task_create_page.py

This module defines the TaskCreatePage class used for creating task creation pages.

Classes:
    TaskCreatePage(BaseCreatePage): Handles the creation of task creation pages.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, mediator, parent): Initializes the TaskCreatePage instance.
    create_widgets(self): Creates widgets for the task creation page.
    prepare_data(self): Prepares data to be sent to the server.

"""

import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_create_page import BaseCreatePage

class TaskCreatePage(BaseCreatePage):
    """ This class will be used to create the task creation page.

    Args:
        BaseCreatePage (BaseCreatePage): Base class for the creation page
    """
    def __init__(self, master: tk, mediator: object, parent: object) -> None:
        super().__init__(master,mediator, parent)
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Criar Tarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        priority = [ "Alta", "Media","Baixa"]

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.priority_combobox = LabelCombobox(self, "Prioridade:", priority,\
             entry_width, padding, self.mediator)
        self.end_date_field = DateField(self, "Data de Entrega:", entry_width,\
             padding, self.mediator)
        self.notification_date_field = DateField(self, "Data da Notificação:",\
             entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6, entry_width,\
             padding, self.mediator)

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server

        Returns:
            dict: The data to be sent to the server
        """
        data = {
            "item_type": "task",
            "project": self.parent,
            "name": self.name_field.get_value(),
            "priority": self.priority_combobox.get_value(),
            "end_date": self.end_date_field.get_value(),
            "notification_date": self.notification_date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
