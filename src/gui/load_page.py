import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.logic.load import Load
from src.logic.adapter import FileAdapter
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError
import os

class LoadPage(tk.Toplevel):
    def __init__(self, master, controller, user):
        super().__init__(master)
        self.controller = controller
        self.user = user
        self.file_path = ''
        self.title("Importação de Projetos")
        self.create_widgets()


    def create_widgets(self):
        self.instruction_label = tk.Label(self, text="Importe novos projetos", font=("Arial", 20))
        self.instruction_label.grid(row=0, column=0, padx=10, pady=10)

        self.instruction_label = tk.Label(self, text="Escolha um arquivo JSON ou TXT para carregar:", font=("Arial", 12))
        self.instruction_label.grid(row=1, column=0, padx=10, pady=10)

        self.choose_file_button = tk.Button(self, text="Escolher Arquivo", command=self.choose_file)
        self.choose_file_button.grid(row=2, column=0, padx=10, pady=2)

        self.file_name_label = tk.Label(self, text="")
        self.file_name_label.grid(row=3, column=0, padx=10, pady=10)

        self.load_button = tk.Button(self, text="Carregar Arquivo", command=self.load_file)
        self.load_button.grid(row=4, column=0, padx=10, pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("TXT files", "*.txt")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.file_name_label.config(text=file_name)
            self.file_path = file_path 

    def load_file(self):
        if not self.file_path:
            messagebox.showerror("Aviso", "Nenhum arquivo selecionado.")
            return

        try:
            FileAdapter.read_file(self.user, self.file_path)
            self.controller.update_main_page()
            self.destroy()
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
        except FileNotFoundError as e:
            messagebox.showerror("Aviso", str(e))
        except InvalidFileFormat as e:
            messagebox.showerror("Aviso", str(e))
        except InvalidFileEstucture as e:
            messagebox.showerror("Aviso", str(e))
        except ItemNameBlank as e:
            messagebox.showerror("Aviso", str(e))
        except ItemNameAlreadyExists as e:
            messagebox.showerror("Aviso", str(e))


    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.geometry(f'{width}x{height}+{x}+{y}')