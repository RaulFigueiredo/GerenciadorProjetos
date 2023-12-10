"""
Module: project_create_page.py

This module defines the ProjectCreatePage class, used to create a project creation page.

Classes:
    ProjectCreatePage(BaseCreatePage): Handles the creation of a project creation page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, mediator, parent, labels): Initializes the ProjectCreatePage instance.
    create_widgets(self): Creates widgets for the project creation page.
    prepare_data(self): Prepares data to be sent to the server.

"""

import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_create_page import BaseCreatePage

class ProjectCreatePage(BaseCreatePage):
    """ This class will be used to create the project creation page.

    Args:
        BaseCreatePage (_type_): Base class for the creation page
    """
    def __init__(self,
                master: object,
                mediator: object,
                parent: object
            ):
        super().__init__(master,mediator, parent)
        self.labels = self.parent.labels
        self.create_widgets()

    def create_widgets(self) -> None:
        """ This method will be used to create the widgets.
        """
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Novo Projeto", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        label_names = [label.name for label in self.labels]
        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.label_combobox = LabelCombobox(self, "Etiqueta:", \
                         label_names, entry_width, padding, self.mediator)
        self.date_field = DateField(self, "Data de Entrega:", entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6,\
                         entry_width, padding, self.mediator)

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server

        Returns:
            dict: The data to be sent to the server
        """
        label = None
        selected_name = self.label_combobox.get_value()
        for each_label in self.labels:
            if each_label.name == selected_name:
                label = each_label
                break
        data = {
            "item_type": "project",
            "user": self.parent,
            "name": self.name_field.get_value(),
            "label": label,
            "end_date": self.date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
