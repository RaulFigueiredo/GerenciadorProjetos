import tkinter as tk
from tkinter import ttk  # Certifique-se de importar ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField


class CreateProjectPage(tk.Frame):
    def __init__(self, master, mediator, labels):
        super().__init__(master)
        self.mediator = mediator
        self.labels = labels  # Mock de etiquetas recebidas da página principal
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

        submit_button = tk.Button(self, text="Enviar", command=self.submit)
        submit_button.pack(side="bottom", pady=10)

    def submit(self):
        if not self.name_field.get_value():
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")
            return
        project_data = {
            "name": self.name_field.get_value(),
            "label": self.label_combobox.get_value(),
            "end_date": self.date_field.get_value(),
            "description": self.description_text.get_value()
        }
        self.mediator.notify(self, "submit", project_data)
        self.master.destroy()