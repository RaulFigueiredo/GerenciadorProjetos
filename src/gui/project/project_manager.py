"""
Module: project_display_manager.py

This module defines the ProjectDisplayManager class, used to 
manage project display and manipulation.

Classes:
    ProjectDisplayManager(BaseDisplayManager): Manages project display and manipulation.

Attributes:
    No public attributes.

Methods:
    __init__(self, home, parent): Initializes the ProjectDisplayManager instance.
    open_page(self, item, parent=None): Opens a page for a given item.
    open_create_page(self): Opens a page for creating a new project.
    open_update_page(self, item): Opens a page to update a project.
    refresh_parent_page(self): Refreshes the parent page.
    refrash_page(self): Refreshes the current page.

"""

from tkinter import messagebox
import tkinter as tk
#from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.project.project_create_page import ProjectCreatePage
from src.gui.project.project_page import ProjectPage
from src.gui.project.project_update_page import ProjectUpdatePage
#from src.logic.items.item_factory import ItemFactory
from src.gui.base_CRUD.base_manager import BaseDisplayManager

class ProjectDisplayManager(BaseDisplayManager):
    """ This class will be used to create the project display manager.

    Args:
        BaseDisplayManager (BaseDisplayManager): Base class for the display manager
    """
    def __init__(self, home: object, parent: object) -> None:
        """ Creates the project display manager.

        Args:
            home (object): home page
            parent (object): parent page
        """
        super().__init__(home)
        self.parent = parent
        self.item = None

    def open_page(self, item: object, parent=None):
        """ Opens the page.

        Args:
            item (object): Item to be opened.
            parent (_type_, optional): Parent page. Defaults to None.
        """
        # deixa apenas 1 janela aberta
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        # conf window
        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes do Projeto")

        project_page = ProjectPage(master=self.top_window, home=self.home,
                                   manager=self, project=item)
        project_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_create_page(self) -> None:
        """ Opens the create page.
        """
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Criar Novo Projeto")


        create_project_page = ProjectCreatePage(master=self.top_window,
                                                mediator=FormMediator(self.submit_item),
                                                parent= self.parent)
        create_project_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_update_page(self, item: object) -> None:
        """ Opens the update page.

        Args:
            item (object): The item to be updated.
        """
        # deixa apenas 1 janela aberta
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Editar Projeto")

        self.item = item

        update_project_page = ProjectUpdatePage(project=self.item,\
                                                manager=self,\
                                                master=self.top_window,\
                                                parent = self.parent,\
                                                mediator=FormMediator(self.update_item))
        update_project_page.pack(fill='both', expand=True)

        self.resize_page()

    def refresh_parent_page(self) -> None:
        """ Refreshes the parent page.
        """
        self.home.update_main_page()

    def refrash_page(self) -> None:
        """ Refreshes the page.
        """
        self.top_window.destroy()
        self.open_page(self.item)
