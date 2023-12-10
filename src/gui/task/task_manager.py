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
from src.gui.base_CRUD.base_manager import BaseDisplayManager


class TaskDisplayManager(BaseDisplayManager):
    def __init__(self, home):
        self.home = home
        self.top_window = None

    def open_page(self, item, parent):
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes da Tarefa")

        self.parent = parent
        task_page = TaskPage(master=self.top_window, home=self.home, manager=self, task=item)
        task_page.pack(fill='both', expand=True)

        self.resize_page()


    def open_update_page(self,item):
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Editar Tarefa")

        self.item = item
        update_task_page = TaskUpdatePage(task=self.item,
                                          manager=self,
                                          master=self.top_window, 
                                          parent=self.parent,
                                          mediator=FormMediator(self.update_item))
        update_task_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_create_page(self, parent):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Criar Nova Tarefa")

        self.parent = parent
        create_task_page = TaskCreatePage(master=self.top_window,
                                          mediator=FormMediator(self.submit_item),
                                          parent = self.parent)
        
        create_task_page.pack(fill='both', expand=True)
        self.resize_page()

    def refresh_parent_page(self):
        self.home.project_manager.top_window.destroy()
        self.home.project_manager.open_page(self.parent)
        self.home.project_manager.refresh_parent_page()

    def refrash_page(self):
        self.top_window.destroy()
        self.open_page(self.item, self.parent)
    
