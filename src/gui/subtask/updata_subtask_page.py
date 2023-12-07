import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from tkcalendar import DateEntry
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField


class UpdateSubtaskPage(tk.Frame):
    def __init__(self, master, mediator, controller, subtask):
        super().__init__(master)
        self.mediator = mediator
        self.controler = controller
        self.subtask = subtask
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Subtarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        
        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        
        self.name_field.set_value(self.subtask.name if self.subtask.name is not None else '')
       
        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=lambda: self.controler.subtask_manager.open_subtask_page(self.subtask))
        close_button.grid(row=0, column=0, padx=5)


    def submit(self):
        if not self.name_field.get_value():
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")
            return
        task_data = {
            "name": self.name_field.get_value(),
        }
        self.mediator.notify(self, "submit", task_data)
        self.master.destroy()

