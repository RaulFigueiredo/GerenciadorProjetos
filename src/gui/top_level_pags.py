from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from gui.forms_base import EntryField, LabelCombobox, DescriptionText, DateField
from gui.mediator import FormMediator
from gui.create_project_page import CreateProjectPage
from gui.project_page import ProjectPage

class ToplevelManager:
    def __init__(self, parent, project):
        self.parent = parent
        self.project = project
        self.top_window = None

    def open_project_page(self):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela de projetos atual?"):
                return
            self.close_top_window()

        screen_width = self.parent.winfo_screenwidth()   # Largura do monitor
        screen_height = self.parent.winfo_screenheight()  # Altura do monitor

        window_width = int(screen_width * 0.4)  # 40% da largura do monitor
        window_height = int(screen_height * 0.8)  # 80% da altura do monitor
        x_position = int(screen_width * 0.3)  # 30% da largura do monitor à esquerda
        y_position = int(screen_height * 0.1)  # 10% da altura do monitor no topo

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Detalhes do Projeto")
        #self.top_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.top_window.geometry("425x550+400+50")
        self.top_window.protocol("WM_DELETE_WINDOW", self.close_top_window)
        project_page = ProjectPage(master=self.top_window, controller=self.parent, project=self.project)
        project_page.pack()

    def open_create_project_page(self):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Criar Novo Projeto")
        self.top_window.geometry("425x550+400+50")  # Tamanho definido como exemplo
        labels_mock = ["Urgente", "Alta Prioridade", "Média Prioridade", "Baixa Prioridade"]
        create_project_page = CreateProjectPage(master=self.top_window, mediator=FormMediator(self.submit_project), labels=labels_mock)
        create_project_page.pack()

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None

    def submit_project(self, project_data):
        # Este método será chamado pelo Mediator quando o botão de enviar for pressionado.
        # Substitua por sua lógica de tratamento dos dados do formulário.
        print("Projeto submetido:", project_data)
