"""
Module: task_page.py

This module defines the TaskPage class used to create and manage the task page.

Classes:
    TaskPage(BasePage): Manages the task page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, home, manager, task): Initializes the TaskPage instance.
    create_widgets(self): Creates the widgets on the task page.
    on_double_click(self, event): Handles the double click event on subtasks.
    info_box(self): Creates the information box on the task page.
    description_box(self): Creates the description box on the task page.
    subtask_box(self): Creates the subtask box on the task page.

"""

import tkinter as tk
from tkinter import ttk

from src.gui.base_CRUD.base_page import BasePage

class TaskPage(BasePage):
    """ This class will be used to create the task page.

    Args:
        BasePage (_type_): Base class for the page
    """
    def __init__(self, master: tk, home: object, manager:object, task:callable):
        super().__init__(master, home, manager, task)
        self.subtasks_listbox = None
        self.create_widgets()

    def create_widgets(self) -> None:
        """ Creates the widgets.
        """
        # pensar se deixo assim memo, não sei se gostei
        # as outras paginas ficaram pequenas, ai ficava suave
        # deixar tudo aq dentro, nessa ficou estranho
        # Pensar nisso dps

        self.info_box()

        self.description_box()

        self.subtask_box()

        self.get_buttons(row=7)

    def on_double_click(self, event: object):
        """ Double click event.

        Args:
            event (object): Event object
        """
        selection = self.subtasks_listbox.curselection()
        if selection:
            index = selection[0]
            subtask = self.item.subtasks[index]
            self.home.subtask_manager.open_page(subtask,self.item)


    def info_box(self) -> None:
        """ Creates the info box.
        """
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)

        # Nome da Tarefa
        name_label = tk.Label(self, text=self.item.name, font=("Arial", 24), wraplength=400)
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Informações da Tarefa
        info_frame = ttk.Frame(self)
        info_frame.grid(row=1, column=0, sticky="ew", padx=10)
        info_frame.grid_columnconfigure(0, weight=1)

        labels = ["Nivel de prioridade:", "Data de Início:", \
             "Data de previsao de termino:", "Data para notificacao:",\
             "Status:", "Data de Conclusao:"]
        values = [str(self.item.priority), str(self.item.creation_date), str(self.item.end_date),
                  str(self.item.notification_date),self.item.status,str(self.item.conclusion_date)]

        for i, (label, value) in enumerate(zip(labels, values)):
            if label == "Status:" and value:
                value = "Concluída"
            elif label == "Status:" and not value:
                value = "Em andamento"
            if label == "Data de Conclusao:" and value == "None":
                continue
            elif value == "None":
                value = "Não definido"

            tk.Label(info_frame, text=f"{label} {value}").grid(row=i, column=0, sticky="w")


    def description_box(self) -> None:
        """ Creates the description box.
        """
        tk.Label(self, text="Descrição:").grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        description_text = tk.Text(self, height=3, width=1, wrap="word")
        description_text.grid(row=3, column=0, sticky="ew", padx=15)
        if self.item.description is None:
            description_content = ""
        else:
            description_content = self.item.description
        description_text.insert(tk.END, description_content)
        description_text.config(state="disabled")

    def subtask_box(self) -> None:
        """ Creates the subtask box.
        """
        subtasks_frame = ttk.Frame(self)
        subtasks_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 0))
        subtasks_frame.grid_columnconfigure(1, weight=1)

        subtasks_label = tk.Label(subtasks_frame, text="Subtarefas:")
        subtasks_label.grid(row=0, column=0, sticky="w")

        add_task_button = ttk.Button(subtasks_frame, text="+", width=2,\
             command=lambda: self.home.subtask_manager.open_create_page(self.item))
        add_task_button.grid(row=0, column=1, sticky="w")

        self.subtasks_listbox = tk.Listbox(self, height=5, width=40)
        self.subtasks_listbox.grid(row=5, column=0, sticky="ew", padx=10)

        for task in self.item.subtasks:
            if task.status:
                self.subtasks_listbox.insert(tk.END, task.name + " (Concluída)")
                self.subtasks_listbox.itemconfig(tk.END, {'fg': 'green'})
            else:
                self.subtasks_listbox.insert(tk.END, task.name)

        self.subtasks_listbox.bind("<Double-1>", self.on_double_click)
