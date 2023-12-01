import tkinter as tk
from tkinter import ttk  # Certifique-se de importar ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField


class CreateSubtaskPage(tk.Frame):
    def __init__(self, master, mediator):
        super().__init__(master)
        self.mediator = mediator
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Criar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        
        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)

        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=self.close_window)
        close_button.grid(row=0, column=0, padx=5)


    def submit(self):
        if not self.name_field.get_value():
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")
            return
        subtask_data = {
            "name": self.name_field.get_value()
        }
        self.mediator.notify(self, "submit", subtask_data)
        self.master.destroy()

    def close_window(self):
        self.master.destroy()