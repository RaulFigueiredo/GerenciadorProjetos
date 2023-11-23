import tkinter as tk
from tkinter import ttk
from .calendar_page import CalendarPage
from src.gui.project_manager import ProjectDisplayManager
from src.gui.task_manager   import TaskDisplayManager
from src.gui.dashboard import DashboardPage


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
        ttk.Button(self, text='Histórico', style='TButton', command=lambda: on_navigate('historico')).grid(row=0, column=3, padx=5)


class ProjectList(tk.Frame):
    def __init__(self, parent, user, bg_color='#ffffff'):
        super().__init__(parent, bg=bg_color, bd=1, relief='solid')
        
        self.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        parent.grid_rowconfigure(1, weight=1)

        title_label = tk.Label(self, text="Meus Projetos", font=('Arial', 18, 'bold'), bg=bg_color)
        title_label.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 20))

        self.user = user
        self.project_map = {}
        self.project_manager = ProjectDisplayManager(self, self.user)
        self.task_manager = TaskDisplayManager(self)

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
        self.tree.bind("<Double-1>", self.on_double_click)
        open_create_project_button = tk.Button(
                                    self,
                                    text="Criar Projeto",
                                    command=lambda: self.project_manager.open_create_project_page()
                                )
        open_create_project_button.grid(row=2, column=0, sticky='nsew')

    def show_project_page(self, project):
        self.project_manager.open_project_page(project)

    def on_double_click(self, event):
        item_id = self.tree.selection()[0]
        project_name = self.tree.item(item_id, 'tags')[0]
        project = self.project_map.get(project_name)
        if project:
            self.show_project_page(project)
        else:
            print(f"No project found for the selected item")

    def mock_projects(self):
        self.tree.tag_configure('projectname', font=('Arial', 12, 'bold'))

        for project in self.user.projects:
            # Use project name or another unique identifier as a tag
            project_id = self.tree.insert('', tk.END, text=project.name, open=True, tags=(project.name, 'projectname'))

            self.project_map[project.name] = project
            for task in project.tasks:
                self.tree.insert(project_id, tk.END, text=task.name)
    def update_main_page(self):
        self.tree.delete(*self.tree.get_children())
        self.mock_projects()

class HomePage(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky='nsew')

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.top_bar = TopBar(self, self.navigate)
        self.top_bar.grid(row=0, column=0, sticky='ew')
        self.user = user

        self.project_list = ProjectList(self, self.user)
        self.project_list.grid(row=1, column=0, sticky='nsew')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.calendar_page = None
        self.dashboard_page = None

    def show_home_page(self):
        if self.calendar_page:
            self.calendar_page.interface.grid_forget()
        if self.dashboard_page:
            self.dashboard_page.grid_forget()
        self.top_bar.grid(row=0, column=0, sticky='ew')
        self.project_list.grid(row=1, column=0, sticky='nsew')

    def show_calendar_page(self):
        self.project_list.grid_forget()
        self.top_bar.grid_forget()
        if not self.calendar_page:
            self.calendar_page = CalendarPage(master=self, on_close=self.show_home_page)
        self.calendar_page.interface.grid(row=1, column=0, sticky='nsew')

    def show_dashboard_page(self):
        self.project_list.grid_forget()
        self.top_bar.grid_forget()
        if not self.dashboard_page:
            self.dashboard_page = DashboardPage(master=self, on_close=self.show_home_page)
        self.dashboard_page.grid(row=1, column=0)

    def navigate(self, destination):
        print(f"Navigating to {destination}")
        if destination == 'calendario':
            self.show_calendar_page()
        elif destination == 'dashboard':
            self.show_dashboard_page()

