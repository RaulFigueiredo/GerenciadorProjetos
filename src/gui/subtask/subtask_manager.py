from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.gui.project.create_project_page import CreateProjectPage
from src.gui.project.project_page import ProjectPage
from src.gui.task.task_page import TaskPage
from src.gui.task.updata_task_page import UpdateTaskPage
from src.gui.task.create_task_page import CreateTaskPage
from src.logic.items.item_factory import ItemFactory
from src.gui.subtask.create_subtask_page import CreateSubtaskPage
from src.gui.subtask.subtask_page import SubtaskPage
from src.gui.subtask.updata_subtask_page import UpdateSubtaskPage

class SubtaskDisplayManager:
    def __init__(self, parent):
        self.parent = parent
        self.top_window = None

    def open_subtask_page(self, subtask):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Detalhes da Subtarefa")
        self.top_window.geometry("425x200+520+140")
        task_page = SubtaskPage(master=self.top_window, controller=self, subtask=subtask)
        task_page.pack()

    def open_update_subtask_page(self,subtask):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Editar Tarefa")
        self.top_window.geometry("425x200+520+140")
        self.subtask = subtask

        update_subtask_page = UpdateSubtaskPage(subtask=self.subtask, master=self.top_window, controller=self.parent,
                                                mediator=FormMediator(self.update_subtask))
        update_subtask_page.pack()

    def open_create_subtask_page(self, task):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.parent)
        self.top_window.title("Criar Nova Tarefa")
        self.top_window.geometry("425x200+520+140")
        self.task = task
        create_task_page = CreateSubtaskPage(master=self.top_window,mediator=FormMediator(self.submit_subtask))
        create_task_page.pack()


    def update_subtask(self, project_data):
        self.subtask.update(**project_data)
        self.refrash_project_page(self.task)
        print("Task:", project_data)


    def refrash_project_page(self, task):
        self.parent.task_manager.top_window.destroy()
        self.parent.task_manager.open_task_page(task)

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None

    
    def submit_subtask(self, task_data):
        ItemFactory.create_item('subtask', task=self.task, **task_data)
        # fazer esse refrash da task
        self.refrash_project_page(self.task)
        self.close_top_window()
        print("Projeto submetido:", task_data)