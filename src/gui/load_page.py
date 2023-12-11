"""Module: Load Page

This module provides a 'LoadPage' class for importing projects via a graphical user interface.

Classes:
    LoadPage: Represents a window for importing projects.

Functions:
    - No module-level functions documented -

Example Usage:
    # Example instantiation of LoadPage class
    root = tk.Tk()
    controller = Controller()
    user = User()
    load_page = LoadPage(root, controller, user)
    load_page.center_window(500, 300)
"""

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from src.logic.adapter import FileAdapter
from src.logic.users.user_interface import IUser

# pylint: disable=redefined-builtin
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
    ItemNameAlreadyExists, \
    InvalidFileFormat,\
    InvalidFileEstucture,\
    FileNotFoundError


class LoadPage(tk.Toplevel):
    """ Class for the import projects window.

    Args:
        tk (tk.Toplevel): Toplevel window.
    """
    def __init__(self, master: tk, controller: tk, user: IUser) -> None:
        """ Creates a new window for importing projects.

        Args:
            master (_type_): Master window.
            controller (_type_): Controller for the page.
            user (_type_): Current user.
        """
        if hasattr(controller, 'load_page_window') and controller.load_page_window:
            controller.load_page_window.destroy()

        super().__init__(master)
        self.controller = controller
        self.user = user
        self.file_path = ''
        self.title("Importação de Projetos")

        self.create_widgets()
        self.center_window(294, 250)

        self.controller.load_page_window = self

    def create_widgets(self) -> None:
        """ Creates the widgets for the page.
        """
        self.instruction_label = tk.Label(self, text="Importe novos projetos", font=("Arial", 20))
        self.instruction_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.instruction_label =tk.Label(self,text="Escolha um arquivo para carregar:",\
                     font=("Arial", 12))
        self.instruction_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.choose_file_button = tk.Button(self, text="Escolher Arquivo", command=self.choose_file)
        self.choose_file_button.grid(row=2, column=0, padx=10, pady=2, sticky="nsew")

        self.file_name_label = tk.Label(self, text="")
        self.file_name_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.load_button = tk.Button(self, text="Carregar Arquivo", command=self.load_file)
        self.load_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def choose_file(self) -> None:
        """ Opens a file dialog to choose a file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"),\
                         ("TXT files", "*.txt"), ("CSV files", "*.csv")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.file_name_label.config(text=file_name)
            self.file_path = file_path
            print("File selected:", self.file_path)  # Para depuração
        else:
            print("No file selected")  # Para depuração


    def load_file(self) -> None:
        """ Loads a file and adds the projects to the user's list of projects.
        """
        if not self.file_path:
            messagebox.showerror("Aviso", "Nenhum arquivo selecionado.")
            return

        try:
            FileAdapter.read_file(self.user, self.file_path)
            self.controller.update_main_page()
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
            self.destroy()
        except FileNotFoundError as _:
            messagebox.showerror("Aviso", str(_))
        except InvalidFileFormat as _:
            messagebox.showerror("Aviso", str(_))
        except InvalidFileEstucture as _:
            messagebox.showerror("Aviso", str(_))
        except ItemNameBlank as _:
            messagebox.showerror("Aviso", str(_))
        except ItemNameAlreadyExists as _:
            messagebox.showerror("Aviso", str(_))


    def center_window(self, width:int, height:int) -> None:
        """ Centers the window on the screen.

        Args:
            width (object): Width of the window.
            height (object): Height of the window.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        _x = int((screen_width / 2) - (width / 2))
        _y = int((screen_height / 2) - (height / 2))

        self.geometry(f'{width}x{height}+{_x}+{_y}')
