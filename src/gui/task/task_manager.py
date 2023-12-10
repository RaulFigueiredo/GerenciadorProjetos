"""
Module: task_display_manager.py

This module defines the TaskDisplayManager class used for managing task display.

Classes:
    TaskDisplayManager(BaseDisplayManager): Handles the management of task display.

Attributes:
    No public attributes.

Methods:
    __init__(self, home): Initializes the TaskDisplayManager instance.
    open_page(self, item, parent): Opens the task page.
    open_update_page(self, item): Opens the update page for a task.
    open_create_page(self, parent): Opens the create page for a task.
    refresh_parent_page(self): Refreshes the parent page.
    refresh_page(self): Refreshes the current page.

"""

from tkinter import messagebox
import tkinter as tk
#from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.task.task_page import TaskPage
from src.gui.task.updata_task_page import TaskUpdatePage
from src.gui.task.task_create_page import TaskCreatePage
#from src.logic.items.item_factory import ItemFactory
#from src.logic.execeptions.exceptions_items import ItemNameBlank,\
#                                                    ItemNameAlreadyExists
#PENSAR SE TENHO Q COLOCAR O ERRO ITEM DESCONHECIDO
from src.gui.base_CRUD.base_manager import BaseDisplayManager


class TaskDisplayManager(BaseDisplayManager):
    """ This class will be used to create the task display manager.

    Args:
        BaseDisplayManager (BaseDisplayManager): Base class for the display manager
    """
    def __init__(self, home: tk) -> None:
        """ Creates the task display manager.

        Args:
            home (_type_): _description_
        """
        self.home = home
        self.top_window = None

    def open_page(self, item: callable, parent: object):
        """ Opens the page.

        Args:
            item (): 
            parent (): 
        """
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes da Tarefa")

        self.parent = parent
        task_page = TaskPage(master=self.top_window, home=self.home, manager=self, task=item)
        task_page.pack(fill='both', expand=True)

        self.resize_page()


    def open_update_page(self,item):
        """ Opens the update page.

        Args:
            item (_type_): Item to be updated.
        """
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
        """ Opens the create page.

        Args:
            parent (_type_): Parent page.
        """
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

    def refresh_parent_page(self) -> None:
        """ Refreshes the parent page.
        """
        self.home.project_manager.top_window.destroy()
        self.home.project_manager.open_page(self.parent)
        self.home.project_manager.refresh_parent_page()

    def refrash_page(self) -> None:
        """ Refreshes the page.
        """
        self.top_window.destroy()
        self.open_page(self.item, self.parent)
