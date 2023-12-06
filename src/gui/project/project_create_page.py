import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_create_page import BaseCreatePage

class ProjectCreatePage(BaseCreatePage):
    def __init__(self, master, mediator, parent, labels):
        super().__init__(master,mediator, parent)
        self.labels = labels  
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Novo Projeto", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.label_combobox = LabelCombobox(self, "Etiqueta:", self.labels, entry_width, padding, self.mediator)
        self.date_field = DateField(self, "Data de Entrega:", entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6, entry_width, padding, self.mediator)

        self.get_buttons()
    
    def prepare_data(self):
        data = {
            "item_type": "project",
            "user": self.parent,
            "name": self.name_field.get_value(),
            "label": self.label_combobox.get_value(),
            "end_date": self.date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data