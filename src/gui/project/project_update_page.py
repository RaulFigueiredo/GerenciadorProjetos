"""
Module: project_update_page.py

This module defines the ProjectUpdatePage class used to create the project update page.

Classes:
    ProjectUpdatePage(BaseUpdatePage): Handles the creation of the project update page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, manager, mediator, project, parent, labels):
Initializes the ProjectUpdatePage instance.
    create_widgets(self): Creates widgets for the project update page.
    prepare_data(self): Prepares data to be sent to the server.

"""

import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class ProjectUpdatePage(BaseUpdatePage):
    """ This class will be used to create the project update page.

    Args:
        BaseUpdatePage (BaseUpdatePage): Base class for the update page
    """
    def __init__(
        self,
        master: object,
        manager: object,
        mediator: object,
        project: callable,
        parent: object

    ) -> None:
        super().__init__(master, manager,mediator,  project ,parent)
        self.labels = self.parent.labels
        self.create_widgets()

    def create_widgets(self) -> None:
        """ This method will be used to create the widgets.
        """
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Projeto", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        label_names = [label.name for label in self.labels]

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.label_combobox = LabelCombobox(self, "Etiqueta:", label_names, entry_width,\
             padding, self.mediator)
        self.date_field = DateField(self, "Data de Entrega:", entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6, entry_width,\
             padding, self.mediator)

        self.name_field.set_value(self.item.name if self.item.name is not None else '')
        self.label_combobox.set_value(self.item.label.name if self.item.label is not None else '')
        self.date_field.set_value(self.item.end_date)
        self.description_text.set_value(self.item.description if self.item.description\
             is not None else '')

        self.get_buttons()

    def prepare_data(self) -> dict:
        """ Prepares the data to be sent to the server
        """
        label = None
        selected_name = self.label_combobox.get_value()
        for each_label in self.labels:
            if each_label.name == selected_name:
                label = each_label
                break
        data = {
            "name": self.name_field.get_value(),
            "label": label,
            "end_date": self.date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
