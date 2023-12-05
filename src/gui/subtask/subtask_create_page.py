import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from src.gui.forms_base import EntryField
from src.gui.base_CRUD.base_create_page import BaseCreatePage

class SubtaskCreatePage(BaseCreatePage):
    def __init__(self, master, mediator):
        super().__init__(master, mediator)
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Criar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)

        self.get_buttons()

    def prepare_data(self):
        data = {
            "name": self.name_field.get_value(),
        }

        return data