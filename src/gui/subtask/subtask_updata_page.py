import tkinter as tk
from src.gui.forms_base import EntryField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class SubtaskUpdatePage(BaseUpdatePage):
    def __init__(self, master, manager, mediator, subtask, parent):
        super().__init__(master, manager, mediator, subtask, parent)
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        
        self.name_field.set_value(self.item.name if self.item.name is not None else '')
       
        self.get_buttons()

    def prepare_data(self):
        data = {
            "name": self.name_field.get_value(),
        }
        return data