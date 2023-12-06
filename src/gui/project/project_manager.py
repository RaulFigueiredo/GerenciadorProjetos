from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.project.project_create_page import ProjectCreatePage
from src.gui.project.project_page import ProjectPage
from src.gui.project.project_update_page import ProjectUpdatePage
from src.logic.items.item_factory import ItemFactory

class ProjectDisplayManager:
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user
        self.top_window = None

    def open_page(self, project):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Detalhes do Projeto")
        self.top_window.geometry("425x620+400+50")
        self.top_window.protocol("WM_DELETE_WINDOW", self.close_top_window)
        project_page = ProjectPage(master=self.top_window, controller=self.parent, manager=self, project=project)
        project_page.pack()

    def open_create_page(self):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Criar Novo Projeto")
        self.top_window.geometry("425x620+400+50")  # Tamanho definido como exemplo
        labels_mock = ["Pessoal", "Faculdade", "Trabalho", "FreeLancing"]

        create_project_page = ProjectCreatePage(master=self.top_window, mediator=FormMediator(self.submit_project), labels=labels_mock)
        create_project_page.pack()

    def open_update_page(self,project):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Editar Projeto")
        self.top_window.geometry("425x480+400+50")  # Tamanho definido como exemplo
        self.project = project
        labels_mock = ["Pessoal", "Faculdade", "Trabalho", "FreeLancing"]

        update_project_page = ProjectUpdatePage(project=self.project, master=self.top_window, controller=self.parent,
                                                mediator=FormMediator(self.update_project), labels=labels_mock)
        update_project_page.pack()

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None

    def submit_project(self, project_data):
        ItemFactory.create_item('project', user=self.user, **project_data)
        self.parent.update_main_page()
        self.close_top_window()
        print("Projeto submetido:", project_data)

    def update_project(self, project_data):
        self.project.update(**project_data)
        self.parent.update_main_page()
        print("Projeto submetido:", project_data)

    def refresh_parent_page(self):
        self.parent.update_main_page()