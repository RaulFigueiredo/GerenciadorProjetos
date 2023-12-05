from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.task.task_page import TaskPage
from src.gui.task.updata_task_page import UpdateTaskPage
from src.gui.task.task_create_page import TaskCreatePage
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists
#PENSAR SE TENHO Q COLOCAR O ERRO ITEM DESCONHECIDO


class TaskDisplayManager:
    def __init__(self, parent):
        self.parent = parent
        self.top_window = None

    def open_task_page(self, task):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Detalhes da Tarefa")
        self.top_window.geometry("425x620+480+100")
        # passar self.parent como controller facilita minha vida
        task_page = TaskPage(master=self.top_window, controller=self, task=task)
        task_page.pack()

    def open_update_task_page(self,task):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Editar Tarefa")
        self.top_window.geometry("425x480+480+100")
        self.task = task

        update_task_page = UpdateTaskPage(task=self.task, master=self.top_window, controller=self.parent,
                                                mediator=FormMediator(self.update_task))
        update_task_page.pack()

    def open_create_task_page(self, project):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Criar Nova Tarefa")
        self.top_window.geometry("425x620+480+100")
        self.project = project
        create_task_page = TaskCreatePage(master=self.top_window, mediator=FormMediator(self.submit_task))
        create_task_page.pack()

    def update_task(self, project_data):
        self.task.update(**project_data)
        self.refrash_project_page(self.task.project)
        print("Task:", project_data)

    def refrash_project_page(self, project):
        self.parent.project_manager.top_window.destroy()
        self.parent.project_manager.open_project_page(project)

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None
    
    def submit_task(self, project_data):
        try:
            ItemFactory.create_item('task', project=self.project, **project_data)
            self.refrash_project_page(self.project)
            self.close_top_window()
            print("Tarefa submetido:", project_data)
        except ItemNameBlank as e:
            if not messagebox.showerror("Erro", e):
                return
        except ItemNameAlreadyExists as e:
            if not messagebox.showerror("Erro", e):
                return
        