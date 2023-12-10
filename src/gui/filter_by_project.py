from tkinter import messagebox
import tkinter as tk

class ProjectFilterPage(tk.Toplevel):
    def __init__(self, master, user, on_confirm):
        super().__init__(master)
        self.user = user
        self.on_confirm = on_confirm

        self.title("Filtrar Projetos")
        self.configure(bg="white")
        self.create_widgets()
        self.center_window(320, 320) 

    def create_widgets(self):
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(padx=10, pady=10)

        label_title = tk.Label(main_frame, text="Filtrar por projetos", font=("Arial", 16), bg="white")
        label_title.pack(pady=(0, 5))

        label_subtitle = tk.Label(main_frame, text="Selecione os projetos para filtrar", font=("Arial", 12), bg="white")
        label_subtitle.pack(pady=(0, 10))

        self.listbox = tk.Listbox(main_frame, selectmode='multiple')
        self.listbox.pack(fill="both", expand=True)

        for project in self.user.projects:
            self.listbox.insert(tk.END, project.name)

        confirm_button = tk.Button(main_frame, text="Confirmar Seleção", command=self.confirm_selection)
        confirm_button.pack(pady=10)

    def confirm_selection(self):
        selected_projects = [self.user.projects[idx] for idx in self.listbox.curselection()]
        self.on_confirm(selected_projects)
        self.destroy()
    
    def center_window(self, width:int, height:int) -> None:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{x}+{y}')
