import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class ProjectUpdatePage(BaseUpdatePage):
    def __init__(self, master, manager, mediator, project,parent,  labels):
        super().__init__(master, manager,mediator,  project,parent)
        self.labels = labels  # Mock de etiquetas recebidas da página principal
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Projeto", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.label_combobox = LabelCombobox(self, "Etiqueta:", self.labels, entry_width, padding, self.mediator)
        self.date_field = DateField(self, "Data de Entrega:", entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6, entry_width, padding, self.mediator)
        
        self.name_field.set_value(self.item.name if self.item.name is not None else '')
        self.label_combobox.set_value(self.item.label if self.item.label is not None else '')
        self.date_field.set_value(self.item.end_date)
        self.description_text.set_value(self.item.description if self.item.description is not None else '')

        self.get_buttons()

    def prepare_data(self):
        data = {
            "name": self.name_field.get_value(),
            "label": self.label_combobox.get_value(),
            "end_date": self.date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
