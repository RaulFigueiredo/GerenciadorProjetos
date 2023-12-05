import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from tkcalendar import DateEntry
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class SubtaskUpdatePage(BaseUpdatePage):
    def __init__(self, master, mediator, controller, subtask):
        super().__init__(master, mediator, controller, subtask)
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