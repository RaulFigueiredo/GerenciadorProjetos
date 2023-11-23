import tkinter as tk
from tkinter import ttk

class ThirdPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        example_text = tk.Label(self, text="Texto bobo da Terceira Página.", font=("Arial", 16))
        example_text.pack(pady=20)


        back_button = ttk.Button(self, text="Ir a frente", command=self.controller.show_main_page)
        back_button.pack(pady=20)

        back_button2 = ttk.Button(self, text="History", command=self.controller.refresh_and_go_history_page)
        back_button2.pack(pady=20)
 