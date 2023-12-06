import tkinter as tk
from tkinter import ttk
from src.gui.base_CRUD.base_page import BasePage

class SubtaskPage(BasePage):
    def __init__(self, master, home, manager, subtask):
        super().__init__(master, home, manager, subtask)
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=0)

        name_label = tk.Label(self, text='Subtask', font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        tk.Label(self, text=self.item.name, font=("Arial", 14)).grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        self.get_buttons(row=2)