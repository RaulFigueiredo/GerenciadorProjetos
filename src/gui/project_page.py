import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ProjectPage(tk.Frame):
    def __init__(self, master, controller, project):
        super().__init__(master)
        self.controller = controller
        self.project = project
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)  

        name_label = tk.Label(self, text=self.project.name, font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        info_frame = ttk.Frame(self)
        info_frame.grid(row=1, column=0, sticky="ew", padx=10)
        info_frame.grid_columnconfigure(0, weight=1)

        labels = ["Etiqueta:", "Data de Início:", "Data de previsao de Termino:",\
                  "Status:", "Data de Conclusao:"]
        values = [self.project.label, str(self.project.creation_date), self.project.end_date,\
                  self.project.status, str(self.project.conclusion_date)  ] 
        
        for i, (label, value) in enumerate(zip(labels, values)):
            if label == "Etiqueta:" and not value:
                value = "Sem etiqueta"
 
            if label == "Status:" and value:
                value = "Concluído"

            elif label == "Status:" and not value:
                value = "Em andamento"
            
            if label == "Data de Conclusao:" and value == "None":
                continue

            tk.Label(info_frame, text=f"{label} {value}").grid(row=i, column=0, sticky="w")

        
        tk.Label(self, text="Comentários:").grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        comments_text = tk.Text(self, height=6, width=1, wrap="word")
        comments_text.grid(row=3, column=0, sticky="ew", padx=15)
        comments_text.insert(tk.END, self.project.description)
        comments_text.config(state="disabled")

        tasks_frame = ttk.Frame(self)
        tasks_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 0))
        tasks_frame.grid_columnconfigure(1, weight=1)

        tasks_label = tk.Label(tasks_frame, text="Tarefas:")
        tasks_label.grid(row=0, column=0, sticky="w")

        add_task_button = ttk.Button(tasks_frame, text="+", width=2, command=lambda: self.controller.task_manager.open_create_task_page(self.project))
        add_task_button.grid(row=0, column=1, sticky="w")

        self.tasks_listbox = tk.Listbox(self, height=7, width=1)
        self.tasks_listbox.grid(row=5, column=0, sticky="ew", padx=10)

        for task in self.project.tasks:
            self.tasks_listbox.insert(tk.END, task.name)

        self.tasks_listbox.bind("<Double-1>", self.on_double_click)

        back_button2 = ttk.Button(self, text="Voltar", command=self.controller.project_manager.close_top_window)
        back_button2.grid(row=7, column=0, sticky="e", padx=10, pady=10)

        delete_button = ttk.Button(self, text="Excluir", command=self.confirm_delete)
        delete_button.grid(row=7, column=0, sticky="w", padx=10, pady=10)
        
        open_update_project_button = tk.Button(
                                        self,
                                        text="Editar",
                                        command=lambda: self.controller.project_manager.open_update_project_page(self.project)
                                    )
        open_update_project_button.grid(row=7, column=0, pady=20)

        if self.project.status:
            unconclusion_button = ttk.Button(self, text="Reativar", command=self.unconclusion_project)
            unconclusion_button.grid(row=8, column=0, pady=10)
        else:
            conclusion_button = ttk.Button(self, text="Concluir", command=self.conclusion_project)
            conclusion_button.grid(row=8, column=0, pady=10)

    def confirm_delete(self):
        response = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este projeto?")
        if response:
            self.delete_project()  
            self.controller.update_main_page()  
            self.controller.project_manager.close_top_window()  

    def delete_project(self):
        self.project.delete()
        self.controller.update_main_page()

    def on_double_click(self, event):
        selection = self.tasks_listbox.curselection()
        if selection:
            index = selection[0]
            task = self.project.tasks[index]
            self.controller.task_manager.open_task_page(task)

    def conclusion_project(self):
        self.project.conclusion()
        self.controller.update_main_page()
        self.controller.project_manager.close_top_window()

    def unconclusion_project(self):
        self.project.unconclusion()
        self.controller.update_main_page()
        self.controller.project_manager.close_top_window()
