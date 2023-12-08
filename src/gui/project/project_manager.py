from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.project.project_create_page import ProjectCreatePage
from src.gui.project.project_page import ProjectPage
from src.gui.project.project_update_page import ProjectUpdatePage
from src.logic.items.item_factory import ItemFactory
from src.gui.base_CRUD.base_manager import BaseDisplayManager

class ProjectDisplayManager(BaseDisplayManager):
    def __init__(self, home, user):
        super().__init__(home)
        self.user = user

    def open_page(self, item):
        # deixa apenas 1 janela aberta
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.top_window.destroy()

        # conf window
        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes do Projeto")
    
        project_page = ProjectPage(master=self.top_window, home=self.home, 
                                   manager=self, project=item)
        project_page.pack(fill='both', expand=True)

        self.resize_page()



    def open_create_page(self):
        # deixa apenas 1 janela aberta
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Criar Novo Projeto")

        labels_mock = ["Pessoal", "Faculdade", "Trabalho", "FreeLancing"]

        parent = self.user
        create_project_page = ProjectCreatePage(master=self.top_window,
                                                mediator=FormMediator(self.submit_item),
                                                parent= parent,
                                                labels=labels_mock)
        create_project_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_update_page(self,item):
        # deixa apenas 1 janela aberta
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        # conf window
        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Editar Projeto")

        self.item  = item
        labels_mock = ["Pessoal", "Faculdade", "Trabalho", "FreeLancing"]

        update_project_page = ProjectUpdatePage(project=self.item,\
                                                manager=self,\
                                                master=self.top_window,\
                                                mediator=FormMediator(self.update_item), labels=labels_mock)
        update_project_page.pack(fill='both', expand=True)

        self.resize_page()

    def refresh_parent_page(self):
        self.home.update_main_page()