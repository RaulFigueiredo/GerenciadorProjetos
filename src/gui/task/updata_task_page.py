import tkinter as tk
from src.gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from src.gui.base_CRUD.base_updata_page import BaseUpdatePage


class TaskUpdatePage(BaseUpdatePage):
    def __init__(self, master, manager, mediator,  task):
        super().__init__(master, manager, mediator,  task)
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
        
        self.name_field.set_value(self.item.name if self.item.name is not None else '')
        self.priority_combobox.set_value(self.item.priority if self.item.priority is not None else '')
        self.end_date_field.set_value(self.item.end_date)
        self.notification_date_field.set_value(self.item.notification_date)
        self.description_text.set_value(self.item.description if self.item.description is not None else '')
       
        self.get_buttons()

    def prepare_data(self):
        data = {
            "name": self.name_field.get_value(),
            "priority": self.priority_combobox.get_value(),
            "end_date": self.end_date_field.get_value(),
            "notification_date": self.notification_date_field.get_value(),
            "description": self.description_text.get_value()
        }

        return data
