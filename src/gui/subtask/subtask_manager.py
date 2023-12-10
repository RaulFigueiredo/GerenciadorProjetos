from tkinter import messagebox
import tkinter as tk
from src.gui.mediator import FormMediator
from src.gui.subtask.subtask_create_page import SubtaskCreatePage
from src.gui.subtask.subtask_page import SubtaskPage
from src.gui.subtask.subtask_updata_page import SubtaskUpdatePage
from src.gui.base_CRUD.base_manager import BaseDisplayManager

class SubtaskDisplayManager(BaseDisplayManager):
    def __init__(self, home):
        super().__init__(home)

    def open_page(self, item, parent):
        if self.top_window and self.top_window.winfo_exists():
            self.top_window.destroy()

        self.top_window = tk.Toplevel(self.home)
        self.top_window.title("Detalhes da Subtarefa")

        self.parent = parent
        task_page = SubtaskPage(master=self.top_window, home=self.home, manager=self, subtask=item)
        
        # Use pack com fill e expand para preencher a janela
        task_page.pack(fill='both', expand=True)

        self.resize_page()

    def open_update_page(self,item):
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

    def open_create_page(self, parent):
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

    def refresh_parent_page(self):
        self.home.task_manager.top_window.destroy()
        self.home.task_manager.open_page(self.parent, self.parent.project)


    def refrash_page(self):
        self.top_window.destroy()
        self.open_page(self.item, self.parent)
    
