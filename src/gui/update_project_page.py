import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkcalendar import DateEntry
from gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField


class UpdateProjectPage(tk.Frame):
    def __init__(self, master, mediator,controller, labels, project):
        super().__init__(master)
        self.mediator = mediator
        self.controler = controller
        self.labels = labels  # Mock de etiquetas recebidas da página principal
        self.project = project
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
        
        self.name_field.set_value(self.project.name if self.project.name is not None else '')
        self.label_combobox.set_value(self.project.label if self.project.label is not None else '')
        self.date_field.set_value(self.project.end_date)
        self.description_text.set_value(self.project.description if self.project.description is not None else '')

        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=lambda: self.controler.project_manager.open_project_page(self.project))
        close_button.grid(row=0, column=0, padx=5)


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
        self.mediator.notify(self, "update", project_data)
        self.master.destroy()

