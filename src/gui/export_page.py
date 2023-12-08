import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.logic.export import Export

class ExportPage(tk.Frame):
    def __init__(self, master, controller, user):
        super().__init__(master)
        self.controller = controller
        self.user = user

        self.controller.title("Exportação de Projetos")
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)
        self.create_widgets()

        self.controller.geometry("402x458")
        self.center_window(402, 458)

    def create_widgets(self):
        title = tk.Label(self, text="Exporte seus projetos", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=2, sticky='n', pady=10, padx=10)

        file_name_label = tk.Label(self, text="Digite o nome do arquivo:", font=("Arial", 12))
        file_name_label.grid(row=1, column=0, pady=(20, 0), padx=5, sticky='w')
        self.file_name_entry = tk.Entry(self, font=("Arial", 12))
        self.file_name_entry.grid(row=1, column=1, pady=(20, 0), padx=10, sticky='we')

        self.folder_path = tk.StringVar()
        dir_button = tk.Button(self, text="Selecionar Pasta", font=("Arial", 12), command=self.select_folder)
        dir_button.grid(row=2, column=0, columnspan=2, pady=(20, 0), padx=10, sticky='we')

        label_select_project = tk.Label(self, text="Selecione os Projetos para Exportar:", font=("Arial", 12))
        label_select_project.grid(row=3, column=0, columnspan=2, pady=(20, 0), padx=10, sticky='w')
        self.project_listbox = tk.Listbox(self, font=("Arial", 12), selectmode='multiple')
        self.project_listbox.grid(row=4, column=0, columnspan=2, pady=(5, 5), padx=10, sticky='we')

        for project in self.user.projects:
            self.project_listbox.insert(tk.END, '  ' + project.name)

        # Botão para exportar
        export_button = tk.Button(self, text="Exportar", font=("Arial", 12), command=self.export_projects)
        export_button.grid(row=5, column=0, columnspan=2, pady=(5, 10), padx=10, sticky='we')
        self.controller.update()

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def export_projects(self):
        selected_indices = self.project_listbox.curselection()
        selected_projects = [self.user.projects[i] for i in selected_indices]

        if not selected_projects:
            messagebox.showwarning("Aviso", "Selecione pelo menos um projeto para exportar.")
            return

        if not self.folder_path.get():
            messagebox.showwarning("Aviso", "Selecione um diretório para exportar.")
            return

        try:
            print(selected_projects)
            Export.json_generator(selected_projects, self.file_name_entry.get(), self.folder_path.get())
            messagebox.showinfo("Sucesso", "Projetos exportados com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro", str(e))


    def center_window(self, width, height):
        screen_width = self.controller.winfo_screenwidth()
        screen_height = self.controller.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.controller.geometry(f'{width}x{height}+{x}+{y}')