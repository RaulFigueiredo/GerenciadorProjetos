import tkinter as tk
from tkinter import ttk, messagebox

class TaskPage(tk.Frame):
    def __init__(self, master, controller, task):
        super().__init__(master)
        self.controller = controller
        self.task = task
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)  # Permite que a lista de tarefas expanda verticalmente

        # Nome da Tarefa
        name_label = tk.Label(self, text=self.task.name, font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Informações da Tarefa
        info_frame = ttk.Frame(self)
        info_frame.grid(row=1, column=0, sticky="ew", padx=10)
        info_frame.grid_columnconfigure(0, weight=1)

        labels = ["Nivel de prioridade:", "Data de Início:", "Data de previsao de termino:", "Data para notificacao:",
                  "Status:", "Data de Conclusao:"]
        values = [str(self.task.priority), str(self.task.creation_date), str(self.task.end_date),
                  str(self.task.notification_date), self.task.status, str(self.task.conclusion_date)]
        

        for i, (label, value) in enumerate(zip(labels, values)):
            if label == "Status:" and value:
                value = "Concluída"
            elif label == "Status:" and not value:
                value = "Em andamento"
            if label == "Data de Conclusao:" and value == "None":
                continue
            elif value == "None":
                value = "Nao definido"

            tk.Label(info_frame, text=f"{label} {value}").grid(row=i, column=0, sticky="w")

        # Descrição da Tarefa
        tk.Label(self, text="Descricao:").grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        description_text = tk.Text(self, height=6, width=1, wrap="word")
        description_text.grid(row=3, column=0, sticky="ew", padx=15)
        description_text.insert(tk.END, self.task.description)
        description_text.config(state="disabled")

        # Subtarefas, se houver
        tk.Label(self, text="Subtarefas:").grid(row=4, column=0, sticky="w", padx=10, pady=(10, 0))
        subtasks_listbox = tk.Listbox(self, height=7, width=1)
        subtasks_listbox.grid(row=5, column=0, sticky="ew", padx=15)
        for subtask in self.task.subtasks:
            subtasks_listbox.insert(tk.END, subtask.name)

        # Botões de Ação
        back_button = ttk.Button(self, text="Voltar", command=self.controller.close_top_window)
        back_button.grid(row=7, column=0, sticky="e", padx=10, pady=10)

        delete_button = ttk.Button(self, text="Excluir", command=self.confirm_delete)
        delete_button.grid(row=7, column=0, sticky="w", padx=10, pady=10)

        edit_button = ttk.Button(self, text="Editar", command=lambda: self.controller.open_update_task_page(self.task))
        edit_button.grid(row=7, column=0, pady=10)

        if self.task.status:
            unconclusion_button = ttk.Button(self, text="Reativar", command=self.unconclusion_task)
            unconclusion_button.grid(row=8, column=0, pady=10)
        else:
            conclusion_button = ttk.Button(self, text="Concluir", command=self.conclusion_task)
            conclusion_button.grid(row=8, column=0, pady=10)


    def confirm_delete(self):
        response = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir esta tarefa?")
        if response:
            self.delete_task()
            self.controller.refrash_project_page(self.task.project)
            self.controller.close_top_window()

    def delete_task(self):
        self.task.delete()

    def conclusion_task(self):
        self.task.conclusion()
        self.controller.refrash_project_page(self.task.project)
        self.controller.close_top_window()

    def unconclusion_task(self):
        self.task.unconclusion()
        self.controller.refrash_project_page(self.task.project)
        self.controller.close_top_window()