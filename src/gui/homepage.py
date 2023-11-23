import tkinter as tk
from tkinter import ttk
from src.gui.calendar_page import CalendarPage

class TopBar(tk.Frame):
    def __init__(self, parent, on_navigate, bg_color='#5a6e7f', fg_color='white'):
        super().__init__(parent, bg=bg_color)
        self.grid(row=0, column=0, sticky='ew')
        parent.grid_columnconfigure(0, weight=1)

        spacer = tk.Frame(self, bg=bg_color)
        spacer.grid(row=0, column=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1)

        btn_style = ttk.Style()
        btn_style.configure('TButton', font=('Arial', 12), padding=10, background=bg_color, foreground=fg_color)

        ttk.Button(self, text='Dashboard', style='TButton', command=lambda: on_navigate('dashboard')).grid(row=0, column=1, padx=5)
        ttk.Button(self, text='Calendário', style='TButton', command=lambda: on_navigate('calendario')).grid(row=0, column=2, padx=5)
        ttk.Button(self, text='Projetos', style='TButton', command=lambda: on_navigate('page3')).grid(row=0, column=3, padx=5)


class ProjectList(tk.Frame):
    def __init__(self, parent, bg_color='#ffffff'):
        super().__init__(parent, bg=bg_color, bd=1, relief='solid')
        
        self.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        parent.grid_rowconfigure(1, weight=1)

        title_label = tk.Label(self, text="Meus Projetos", font=('Arial', 18, 'bold'), bg=bg_color)
        title_label.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 20))

        self.tree = ttk.Treeview(self, show='tree')
        self.tree.grid(row=1, column=0, sticky='nsew')

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure('Treeview', font=('Arial', 12), rowheight=25)
        style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.mock_projects()

    def mock_projects(self):
        projects = [
            ('Project Alpha', ['Task 1', 'Task 2', 'Task 3']),
            ('Project Beta', ['Task 1', 'Task 2']),
            ('Project Gamma', ['Task 1'])
        ]
        for project, tasks in projects:
            project_id = self.tree.insert('', tk.END, text=project, open=True)
            for task in tasks:
                self.tree.insert(project_id, tk.END, text=task)

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky='nsew')

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.top_bar = TopBar(self, self.navigate)
        self.top_bar.grid(row=0, column=0, sticky='ew')

        self.project_list = ProjectList(self)
        self.project_list.grid(row=1, column=0, sticky='nsew')

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def navigate(self, destination):
        print(f"Navigating to {destination}")