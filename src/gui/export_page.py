"""Module: Export Page

This module provides an 'ExportPage' class for exporting projects via a graphical user interface.

Classes:
    ExportPage: Represents a window for exporting projects.

Functions:
    - No module-level functions documented -

Example Usage:
    # Example instantiation of ExportPage class
    root = tk.Tk()
    controller = Controller()
    user = User()
    project_list = [project1, project2]  # Example list of projects
    export_page = ExportPage(root, controller, user, project_list)
    export_page.center_window(402, 458)
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.logic.export import Export
from src.logic.execeptions.exceptions_items import EmptyListProjects,\
                                                   FileNameBlank,\
                                                   DirectoryBlank
from src.logic.users.user_interface import IUser

class ExportPage(tk.Toplevel):
    """ Class for the export projects window.

    Args:
        tk (Toplevel): Toplevel window.
    """
    def __init__(self, master: tk, controller: tk, user: IUser, project_list: list):
        """ Creates a new window for exporting projects.

        Args:
            master (tk): Master window.
            controller (tk): Controller for the page.
            user (User): Current user.
            project_list (list): List of projects.
        """
        super().__init__(master)
        self.controller = controller
        self.user = user
        self.project_list = project_list
        self.title("Exportação de Projetos")
        self.geometry("402x458")
        self.create_widgets()

        self.center_window(402, 458)

    def create_widgets(self) -> None:
        """ Creates the widgets for the page.
        """
        title = tk.Label(self, text="Exporte seus projetos", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=2, sticky='n', pady=10, padx=10)

        file_name_label = tk.Label(self, text="Digite o nome do arquivo:", font=("Arial", 12))
        file_name_label.grid(row=1, column=0, pady=(20, 0), padx=5, sticky='w')
        self.file_name_entry = tk.Entry(self, font=("Arial", 12))
        self.file_name_entry.grid(row=1, column=1, pady=(20, 0), padx=10, sticky='we')

        self.folder_path = tk.StringVar()
        dir_button = tk.Button(self, text="Selecionar Pasta", font=("Arial", 12),\
                         command=self.select_folder)
        dir_button.grid(row=2, column=0, columnspan=2, pady=(20, 0), padx=10, sticky='we')

        label_select_project = tk.Label(self, text="Selecione os Projetos para Exportar:",\
                         font=("Arial", 12))
        label_select_project.grid(row=3, column=0, columnspan=2, pady=(20, 0), padx=10, sticky='w')
        self.project_listbox = tk.Listbox(self, font=("Arial", 12), selectmode='multiple')
        self.project_listbox.grid(row=4, column=0, columnspan=2, pady=(5, 5), padx=10, sticky='we')

        for project in self.user.projects:
            self.project_listbox.insert(tk.END, '  ' + project.name)

        # Botão para exportar
        export_button = tk.Button(self, text="Exportar", font=("Arial", 12),\
                         command=self.export_projects)
        export_button.grid(row=5, column=0, columnspan=2, pady=(5, 10), padx=10, sticky='we')
        self.project_list.update_main_page() # check if this is necessary

    def select_folder(self) -> None:
        """ Opens a dialog to select a folder.
        """
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def export_projects(self) -> None:
        """ Exports the selected projects.
        """
        selected_indices = self.project_listbox.curselection()
        selected_projects = [self.user.projects[i] for i in selected_indices]
        print('DIRETORIO:'+str(self.folder_path.get()))

        try:
            Export.json_generator(
                selected_projects,
                self.file_name_entry.get(),
                self.folder_path.get()
            )
            self.destroy()
            messagebox.showinfo("Sucesso", "Projetos exportados com sucesso.")

        except EmptyListProjects as e:
            messagebox.showerror("Aviso", str(e))
            return

        except FileNameBlank as e:
            messagebox.showerror("Aviso", str(e))
            return

        except DirectoryBlank as e:
            messagebox.showerror("Aviso", str(e))
            return


    def center_window(self, width:int, height:int) -> None:
        """ Centers the window on the screen.

        Args:
            width (object): Width of the window.
            height (object): Height of the window.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.geometry(f'{width}x{height}+{x}+{y}')
