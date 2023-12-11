"""
Module: project_page.py

This module defines the ProjectPage class, used to create the project page.

Classes:
    ProjectPage(BasePage): Creates the project page.

Attributes:
    No public attributes.

Methods:
    __init__(self, master, home, manager, project): Initializes the ProjectPage instance.
    create_widgets(self): Creates widgets for the project page.
    on_double_click(self, event): Handles the double-click event on tasks.
    info_box(self): Creates the information box for the project.
    description_box(self): Creates the description box for the project.
    task_box(self): Creates the task box for the project.

"""
import tkinter as tk
from tkinter import ttk
from src.gui.base_CRUD.base_page import BasePage

class ProjectPage(BasePage):
    """ This class will be used to create the project page.

    Args:
        BasePage (BasePage): Base class for the page
    """
    def __init__(self, master: tk, home: object, manager: object, project: callable) -> None:
        super().__init__(master, home, manager, project)
        self.create_widgets()
        #self.tasks_listbox

    def create_widgets(self) -> None:
        """ Creates the widgets.
        """
        self.info_box()

        self.description_box()

        self.task_box()

        self.get_buttons(row=7)

    def on_double_click(self, event):
        """ Double click event.

        Args:
            event (object): Event object
        """
        selection = self.tasks_listbox.curselection()
        if selection:
            index = selection[0]
            task = self.item.tasks[index]
            self.home.task_manager.open_page(task, parent = self.item)

    def info_box(self) -> None:
        """ Creates the info box.
        """
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)

        name_label = tk.Label(self, text=self.item.name, font=("Arial", 24), wraplength=400)
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        info_frame = ttk.Frame(self)
        info_frame.grid(row=1, column=0, sticky="ew", padx=10)
        info_frame.grid_columnconfigure(0, weight=1)

        label_value = self.item.label.name if self.item.label else "Sem etiqueta"

        labels = ["Etiqueta:", "Data de Início:", "Data de previsao de Termino:",\
                  "Status:", "Data de Conclusao:"]
        values = [label_value, str(self.item.creation_date), self.item.end_date,\
                  self.item.status, str(self.item.conclusion_date)  ]

        for i, (label, value) in enumerate(zip(labels, values)):
            if label == "Status:" and value:
                value = "Concluído"

            elif label == "Status:" and not value:
                value = "Em andamento"

            if label == "Data de Conclusao:" and value == "None":
                continue

            tk.Label(info_frame, text=f"{label} {value}").grid(row=i, column=0, sticky="w")

    def description_box(self) -> None:
        """ Creates the description box.
        """
        tk.Label(self, text="Descrição:").grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        descriptions_text = tk.Text(self, height=3, width=1, wrap="word")
        descriptions_text.grid(row=3, column=0, sticky="ew", padx=15)
        if self.item.description is None:
            description_content = ""
        else:
            description_content = self.item.description
        descriptions_text.insert(tk.END, description_content)
        descriptions_text.config(state="disabled")

    def task_box(self) -> None:
        """ Creates the task box.
        """
        tasks_frame = ttk.Frame(self)
        tasks_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 0))
        tasks_frame.grid_columnconfigure(1, weight=1)

        tasks_label = tk.Label(tasks_frame, text="Tarefas:")
        tasks_label.grid(row=0, column=0, sticky="w")

        add_task_button = ttk.Button(tasks_frame, text="+", width=2,\
             command=lambda: self.home.task_manager.open_create_page(self.item))
        add_task_button.grid(row=0, column=1, sticky="w")

        self.tasks_listbox = tk.Listbox(self, height=5, width=40)
        self.tasks_listbox.grid(row=5, column=0, sticky="ew", padx=10)

        for task in self.item.tasks:
            if task.status:
                self.tasks_listbox.insert(tk.END, task.name + " (Concluída)")
                self.tasks_listbox.itemconfig(tk.END, {'fg': 'green'})
            else:
                self.tasks_listbox.insert(tk.END, task.name)

        self.tasks_listbox.bind("<Double-1>", self.on_double_click)
