import tkinter as tk
from tkinter import ttk
from src.gui.base_CRUD.base_page import BasePage

class SubtaskPage(BasePage):
    def __init__(self, master, home, manager, subtask):
        super().__init__(master, home, manager, subtask)
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(4, weight=1)  

        name_label = tk.Label(self, text='Subtarefa', font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        if self.item.status:
            text_conclusion = f"Concluída em {str(self.item.conclusion_date)}"
            conclusion_label = tk.Label(self, text=text_conclusion)
            conclusion_label.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Adiciona wraplength para quebrar linhas longas
        text_label = tk.Label(self, text=self.item.name, font=("Arial", 14), wraplength=400)
        text_label.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        self.get_buttons(row=3)