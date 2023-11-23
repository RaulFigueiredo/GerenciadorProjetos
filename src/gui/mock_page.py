import tkinter as tk
from tkinter import ttk

class MainPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.project_buttons_frame = tk.Frame(self)  # Frame para conter os botões
        self.project_buttons_frame.pack()

        self.create_project_buttons()

        
        open_create_project_button = tk.Button(
                                        self,
                                        text="Criar Projeto",
                                        command=lambda: self.controller.project_manager.open_create_project_page()
                                    )
        open_create_project_button.pack(pady=20)
        
        # Botão de Retorno
        back_button = ttk.Button(self, text="Voltar", command=self.controller.show_third_page)
        back_button.pack(pady=20)


    def create_project_buttons(self):
        # Limpar botões antigos
        for widget in self.project_buttons_frame.winfo_children():
            widget.destroy()

        # Criar novos botões
        for project in self.controller.user.projects:
            button = ttk.Button(self.project_buttons_frame, text=project.name, 
                                command=lambda p=project: self.open_project(p))
            button.pack(pady=5)

    def open_project(self, project):
        self.controller.project_manager.open_project_page(project)

