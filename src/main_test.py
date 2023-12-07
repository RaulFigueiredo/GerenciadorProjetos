from src.gui.mock_page import MainPage
from src.gui.project.project_page import ProjectPage
from src.gui.third_page import ThirdPage
from src.gui.project.project_manager import ProjectDisplayManager
from src.gui.task.task_manager   import TaskDisplayManager
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.users.user import User
from src.logic.items.label import Label

from src.gui.history_page import HistoryManagerApp

import tkinter as tk




class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação Tkinter")
        self.geometry("+500+200")  # Define apenas a posição inicial

        # Inicializa o objeto User com um usuário exemplo
        self.user = User(name="Usuário Exemplo")
        pj_1 = Project(name="Projeto Exemplo1", user=self.user,description='asd' )
        Project(name="Projeto Exemplo3", user=self.user,description='asd' )
        Project(name="Projeto Exemplo4", user=self.user,description='asd' )

        Task(name="Tarefa Exemplo1", project=pj_1,description='asd' )
        t = Task(name="Tarefa Exemplo2", project=pj_1,description='asd' )
        t.conclusion()
        # O gerenciador de telas
        self.project_manager = ProjectDisplayManager(self, self.user)
        self.task_manager = TaskDisplayManager(self)

        # Configuração do container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.create_pages()

    def create_pages(self):
        page = HistoryManagerApp(master=self.container, controller=self,user = self.user)
        self.pages[HistoryManagerApp] = page
        page.grid(row=0, column=0, sticky="nsew")

        for Page in (MainPage, ThirdPage):
            page = Page(master=self.container, controller=self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

    def show_main_page(self):
        self.show_page(MainPage)

    def show_project_page(self, project):
        self.project_manager.open_project_page(project)

    def show_third_page(self):
        self.show_page(ThirdPage)

    def show_history_page(self):
        self.show_page(HistoryManagerApp)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()



    def add_project(self, new_project):
        self.user.projects.append(new_project)
        self.update_main_page()

    def update_main_page(self):
        main_page = self.pages[MainPage]
        main_page.create_project_buttons()

    def update_project_page(self, project):
        project_page = self.pages[ProjectPage]
        project_page.update_project(project)
        self.project_manager.close_top_window()

    def refresh_and_go_history_page(self):
        history_page = self.pages[HistoryManagerApp]
        history_page.display_completed_tasks()
        self.show_page(HistoryManagerApp)


def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()