"""
Module: task_update_page.py

This module defines the TaskUpdatePage class used to create and manage the task update page.

Classes:
    TaskUpdatePage(BaseUpdatePage): Manages the task update page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, manager, mediator, task, parent): Initializes
the TaskUpdatePage instance.
    create_widgets(self): Creates the widgets on the task update page.
    prepare_data(self): Prepares the data to be sent to the server.

"""

import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class TaskUpdatePage(BaseUpdatePage):
    """
        Initializes a TaskUpdatePage object.

        Args:
            master (tk): The master widget.
            manager (object): The manager object.
            mediator (object): The mediator object.
            task (callable): The task object.
            parent (callable): The parent object.

        Returns:
            None
    """
    def __init__(self, master:tk, manager: object, mediator:object, task:callable, parent:callable):
        super().__init__(master, manager, mediator, task, parent)
        self.create_widgets()

    def create_widgets(self) -> None:
        """ This method will be used to create the widgets.
        """
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Tarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        priority = [ "Alta", "Media","Baixa"]

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.priority_combobox = LabelCombobox(self, "Prioridade:", priority,\
             entry_width, padding, self.mediator)
        self.end_date_field = DateField(self, "Data de Entrega:", entry_width,\
             padding, self.mediator)
        self.notification_date_field = DateField(self, "Data da Notificacao:",\
             entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:",\
             6, entry_width, padding, self.mediator)

        self.name_field.set_value(self.item.name if self.item.name is not None else '')
        self.priority_combobox.set_value(self.item.priority if\
             self.item.priority is not None else '')
        self.end_date_field.set_value(self.item.end_date)
        self.notification_date_field.set_value(self.item.notification_date)
        self.description_text.set_value(self.item.description if \
            self.item.description is not None else '')

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server

        Returns:
            dict: The data to be sent to the server
        """
        data = {
            "name": self.name_field.get_value(),
            "priority": self.priority_combobox.get_value(),
            "end_date": self.end_date_field.get_value(),
            "notification_date": self.notification_date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
