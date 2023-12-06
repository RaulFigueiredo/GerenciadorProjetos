from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.task.task_page import TaskPage
from src.gui.task.updata_task_page import TaskUpdatePage
from src.gui.task.task_create_page import TaskCreatePage
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists
#PENSAR SE TENHO Q COLOCAR O ERRO ITEM DESCONHECIDO


class TaskDisplayManager:
    def __init__(self, controller):
        self.controller = controller
        self.top_window = None

    def open_page(self, task, project):
        self.project = project
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Detalhes da Tarefa")
        self.top_window.geometry("425x620+480+100")
        # passar self.controller como controller facilita minha vida
        task_page = TaskPage(master=self.top_window, controller=self.controller, manager=self,task=task)
        task_page.pack()

    def open_update_page(self,task):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Editar Tarefa")
        self.top_window.geometry("425x480+480+100")
        self.task = task

        update_task_page = TaskUpdatePage(task=self.task, master=self.top_window, controller=self.controller,
                                                mediator=FormMediator(self.update_item))
        update_task_page.pack()

    def open_create_page(self, project):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.project = project
        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Criar Nova Tarefa")
        self.top_window.geometry("425x620+480+100")
        create_task_page = TaskCreatePage(master=self.top_window, mediator=FormMediator(self.create_item))
        create_task_page.pack()

    def update_item(self, project_data):
        self.task.update(**project_data)
        self.refresh_parent_page()
        print("Task:", project_data)

    def refresh_parent_page(self):
        self.controller.project_manager.top_window.destroy()
        self.controller.project_manager.open_page(self.project)
        self.controller.project_manager.refresh_parent_page()

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None
    
    def create_item(self, project_data):
        try:
            ItemFactory.create_item('task', project=self.project, **project_data)
            self.refresh_parent_page()
            self.close_top_window()
            print("Tarefa submetido:", project_data)
        except ItemNameBlank as e:
            if not messagebox.showerror("Erro", e):
                return
        except ItemNameAlreadyExists as e:
            if not messagebox.showerror("Erro", e):
                return
        