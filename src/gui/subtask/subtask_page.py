import tkinter as tk
from tkinter import ttk, messagebox

class SubtaskPage(tk.Frame):
    def __init__(self, master, controller, subtask):
        super().__init__(master)
        self.controller = controller
        self.subtask = subtask
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)  # Permite que a lista de tarefas expanda verticalmente

        # Nome da Tarefa
        name_label = tk.Label(self, text='Subtask', font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Informações da Tarefa
        info_frame = ttk.Frame(self)
        info_frame.grid(row=1, column=0, sticky="ew", padx=10)
        info_frame.grid_columnconfigure(0, weight=1)

        # show "name"only 
        tk.Label(self, text=self.subtask.name, font=("Arial", 10)).grid(row=0, column=0, sticky="ew", padx=10, pady=10)


        # Botões de Ação
        back_button = ttk.Button(self, text="Voltar", command=self.controller.close_top_window)
        back_button.grid(row=7, column=0, sticky="e", padx=10, pady=10)

        delete_button = ttk.Button(self, text="Excluir", command=self.confirm_delete)
        delete_button.grid(row=7, column=0, sticky="w", padx=10, pady=10)

        edit_button = ttk.Button(self, text="Editar", command=lambda: self.controller.open_update_subtask_page(self.subtask))
        edit_button.grid(row=7, column=0, pady=10)

        if self.subtask.status:
            unconclusion_button = ttk.Button(self, text="Reativar", command=self.unconclusion_task)
            unconclusion_button.grid(row=8, column=0, pady=10)
        else:
            conclusion_button = ttk.Button(self, text="Concluir", command=self.conclusion_task)
            conclusion_button.grid(row=8, column=0, pady=10)


    def confirm_delete(self):
        response = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir esta tarefa?")
        if response:
            self.delete_task()
            self.controller.refrash_project_page(self.subtask.task)
            self.controller.close_top_window()

    def delete_task(self):
        self.subtask.delete()

    def conclusion_task(self):
        self.subtask.conclusion()
        self.controller.refrash_project_page(self.subtask.task)
        self.controller.close_top_window()

    def unconclusion_task(self):
        self.subtask.unconclusion()
        self.controller.refrash_project_page(self.subtask.task)
        self.controller.close_top_window()

    def on_double_click(self, event):
        selection = self.subtasks_listbox.curselection()
        if selection:
            index = selection[0]
            task = self.task.subtasks[index]
            self.controller.subtask_manager.open_subtask_page(task)