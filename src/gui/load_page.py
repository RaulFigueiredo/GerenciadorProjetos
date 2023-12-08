import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.logic.load import Load
import os

class LoadPage(tk.Frame):
    def __init__(self, master, controller, user):
        super().__init__(master)
        self.controller = controller
        self.user = user

        self.controller.title("Importação de Projetos")
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)
        self.create_widgets()


    def create_widgets(self):
        self.instruction_label = tk.Label(self, text="Importe novos projetos", font=("Arial", 20))
        self.instruction_label.grid(row=0, column=0, padx=10, pady=10)

        self.instruction_label = tk.Label(self, text="Escolha um arquivo JSON para carregar:")
        self.instruction_label.grid(row=1, column=0, padx=10, pady=10)

        self.choose_file_button = tk.Button(self, text="Escolher Arquivo", command=self.choose_file)
        self.choose_file_button.grid(row=2, column=0, padx=10, pady=2)

        self.file_name_label = tk.Label(self, text="")
        self.file_name_label.grid(row=3, column=0, padx=10, pady=10)

        self.load_button = tk.Button(self, text="Carregar Arquivo", command=self.load_file)
        self.load_button.grid(row=4, column=0, padx=10, pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.file_name_label.config(text=file_name)
            self.file_path = file_path 

    def load_file(self):
        file_path = self.file_path_label.cget("text")
        if file_path:
            Load.json_reader(file_path, self.user) 
        else:
            print("Nenhum arquivo selecionado.")


    def center_window(self, width, height):
        screen_width = self.controller.winfo_screenwidth()
        screen_height = self.controller.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.controller.geometry(f'{width}x{height}+{x}+{y}')