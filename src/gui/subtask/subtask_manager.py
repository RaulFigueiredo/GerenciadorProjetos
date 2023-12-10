"""
Module: subtask_display_manager.py

This module defines the SubtaskDisplayManager class used to manage subtask display and manipulation.

Classes:
    SubtaskDisplayManager(BaseDisplayManager): Manages subtask display and manipulation.

Attributes:
    No public attributes.

Methods:
    __init__(self, home): Initializes the SubtaskDisplayManager instance.
    open_page(self, item, parent): Opens a page for a given subtask item.
    open_update_page(self, item): Opens a page to update a subtask.
    open_create_page(self, parent): Opens a page for creating a new subtask.
    refresh_parent_page(self): Refreshes the parent page.
    refrash_page(self): Refreshes the current page.

"""

from tkinter import messagebox
import tkinter as tk
from src.gui.mediator import FormMediator
from src.gui.subtask.subtask_create_page import SubtaskCreatePage
from src.gui.subtask.subtask_page import SubtaskPage
from src.gui.subtask.subtask_updata_page import SubtaskUpdatePage
from src.gui.base_CRUD.base_manager import BaseDisplayManager

class SubtaskDisplayManager(BaseDisplayManager):
    """ This class will be used to create the subtask display manager.

    Args:
        BaseDisplayManager (BaseDisplayManager): Base class for the display manager
    """
    def __init__(self, home) -> None:
        """ Creates the subtask display manager.

        Args:
            home (object): home page
        """
        super().__init__(home)
        self.item = None
        self.parent = None

    def open_page(self, item: callable, parent: callable) -> None:
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes da Subtarefa")

        self.parent = parent
        task_page = SubtaskPage(master=self.top_window, home=self.home, manager=self, subtask=item)

        # Use pack com fill e expand para preencher a janela
        task_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_update_page(self,item:callable) -> None:
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Editar Tarefa")

        self.item = item
        update_subtask_page = SubtaskUpdatePage(subtask=self.item,
                                                manager=self,
                                                parent=self.parent,
                                                master=self.top_window,
                                                mediator=FormMediator(self.update_item))
        update_subtask_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_create_page(self, parent) -> None:
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Criar Nova Tarefa")

        self.parent = parent
        create_task_page = SubtaskCreatePage(master=self.top_window,
                                             mediator=FormMediator(self.submit_item),
                                             parent = self.parent)
        create_task_page.pack(fill='both', expand=True)

        self.resize_page()

    def refresh_parent_page(self) -> None:
        """ Refreshes the parent page.
        """
        self.home.task_manager.top_window.destroy()
        self.home.task_manager.open_page(self.parent, self.parent.project)


    def refrash_page(self) -> None:
        """ Refreshes the page.
        """
        self.top_window.destroy()
        self.open_page(self.item, self.parent)
