from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.gui.mediator import FormMediator
from src.logic.items.item_factory import ItemFactory
from src.gui.subtask.subtask_create_page import SubtaskCreatePage
from src.gui.subtask.subtask_page import SubtaskPage
from src.gui.subtask.subtask_updata_page import SubtaskUpdatePage

class SubtaskDisplayManager:
    def __init__(self, controller):
        self.controller = controller
        self.top_window = None

    def open_page(self, subtask,task):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Detalhes da Subtarefa")
        self.top_window.geometry("425x200+520+140")

        self.task = task
        task_page = SubtaskPage(master=self.top_window, controller=self, manager=self,subtask=subtask)
        task_page.pack()

    def open_update_page(self,subtask):
        if self.top_window and self.top_window.winfo_exists():
            self.close_top_window()

        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Editar Tarefa")
        self.top_window.geometry("425x200+520+140")
        self.subtask = subtask

        update_subtask_page = SubtaskUpdatePage(subtask=self.subtask, master=self.top_window, controller=self.controller,
                                                mediator=FormMediator(self.update_subtask))
        update_subtask_page.pack()

    def open_create_page(self, task):
        if self.top_window and self.top_window.winfo_exists():
            if not messagebox.askyesno("Confirmar", "Fechar a janela atual?"):
                return
            self.close_top_window()

        self.top_window = tk.Toplevel(self.controller)
        self.top_window.title("Criar Nova Tarefa")
        self.top_window.geometry("425x200+520+140")
        self.task = task
        create_task_page = SubtaskCreatePage(master=self.top_window,mediator=FormMediator(self.submit_subtask))
        create_task_page.pack()

    def update_subtask(self, project_data):
        self.subtask.update(**project_data)
        self.refresh_parent_page()
        print("Task:", project_data)

    def refresh_parent_page(self):
        self.controller.task_manager.top_window.destroy()
        self.controller.task_manager.open_page(self.task, self.task.project)

    def close_top_window(self):
        if self.top_window:
            self.top_window.destroy()
            self.top_window = None
    
    def submit_subtask(self, task_data):
        ItemFactory.create_item('subtask', task=self.task, **task_data)
        # fazer esse refrash da task
        self.refresh_parent_page()
        self.close_top_window()
        print("Projeto submetido:", task_data)