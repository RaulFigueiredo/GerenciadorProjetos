import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from tkcalendar import DateEntry
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField


class UpdateTaskPage(tk.Frame):
    def __init__(self, master, mediator, controller, task):
        super().__init__(master)
        self.mediator = mediator
        self.controler = controller
        self.task = task
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 5}
        entry_width = 40

        title_label = tk.Label(self, text="Editar Tarefa", font=("Arial", 20))
        title_label.pack(side="top", fill="x", **padding)

        priority = [ "Alta", "Media","Baixa"]
        
        
        self.name_field = EntryField(self, "Nome:", entry_width, padding, self.mediator)
        self.priority_combobox = LabelCombobox(self, "Prioridade:", priority, entry_width, padding, self.mediator)
        self.end_date_field = DateField(self, "Data de Entrega:", entry_width, padding, self.mediator)
        self.notification_date_field = DateField(self, "Data da Notificacao:", entry_width, padding, self.mediator)
        self.description_text = DescriptionText(self, "Descrição:", 6, entry_width, padding, self.mediator)
        
        self.name_field.set_value(self.task.name if self.task.name is not None else '')
        self.priority_combobox.set_value(self.task.priority if self.task.priority is not None else '')
        self.end_date_field.set_value(self.task.end_date)
        self.notification_date_field.set_value(self.task.notification_date)
        self.description_text.set_value(self.task.description if self.task.description is not None else '')
       
        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=lambda: self.controler.task_manager.open_task_page(self.task))
        close_button.grid(row=0, column=0, padx=5)


    def submit(self):
        if not self.name_field.get_value():
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")
            return
        task_data = {
            "name": self.name_field.get_value(),
            "priority": self.priority_combobox.get_value(),
            "end_date": self.end_date_field.get_value(),
            "notification_date": self.notification_date_field.get_value(),
            "description": self.description_text.get_value()
        }
        self.mediator.notify(self, "update", task_data)
        self.master.destroy()

