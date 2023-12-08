import tkinter as tk
from tkinter import ttk

class MainPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.project_buttons_frame = tk.Frame(self)  # Frame para conter os botões
        self.project_buttons_frame.pack()

        self.create_project_buttons()

        # Botão de Retorno
        back_button = ttk.Button(self, text="Voltar", command=self.controller.show_third_page)
        back_button.pack(pady=20)


    def create_project_buttons(self):
        # Limpar botões antigos
        for widget in self.project_buttons_frame.winfo_children():
            widget.destroy()
