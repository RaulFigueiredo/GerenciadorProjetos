"""
Creates a custom GUI application using tkinter to manage projects, tasks, and labels.

This module defines several custom tkinter Frames for various functionalities in
the application.

Classes:
    - TopBar: A custom tkinter Frame serving as the top navigation bar.
    - ProjectList: A custom tkinter Frame to display a list of projects.
    - HomePage: A custom tkinter Frame serving as the home page of the application.

Usage:
    - The TopBar class provides navigation buttons for various pages like Dashboard, 
Calendar, History, Export, Import, and Labels.
    - The ProjectList class displays a list of projects and allows users to navigate 
to individual project pages.
    - The HomePage class serves as the main layout displaying the TopBar and ProjectList,
allowing navigation to different sections of the application.
"""

import tkinter as tk
from tkinter import ttk

from src.gui.project.project_manager import ProjectDisplayManager
from src.gui.task.task_manager import TaskDisplayManager
from src.gui.subtask.subtask_manager import SubtaskDisplayManager
from src.gui.dashboard import DashboardPage
from src.gui.history_page import HistoryManagerApp
from src.gui.export_page import ExportPage
from src.gui.load_page import LoadPage
from src.gui.labels.labelpage import LabelManager
from src.gui.filter_by_project import ProjectFilterPage
from src.gui.filter_by_label import LabelFilterPage
from src.logic.items.project import Project
from src.logic.users.user import User
from .calendar_page import CalendarPage
from src.gui.notifications_page import NotificationPage



class TopBar(tk.Frame):
    """ A custom tkinter Frame that serves as a top navigation bar for the application.

    Attributes:
        parent (tk.Widget): The parent widget of this frame.
        on_navigate (function): A callback function to handle navigation requests.
        bg_color (str): Background color for the top bar.
        fg_color (str): Foreground color for the text in the top bar.
    """
    def __init__(
            self,
            parent: tk.Widget,
            on_navigate: callable,
            bg_color: str='#5a6e7f',
            fg_color: str='white'
        ):
        """ Initialize the TopBar.

        Parameters:
            parent (tk.Widget): The parent widget of this frame.
            on_navigate (function): A callback function to handle navigation requests.
            bg_color (str, optional): Background color for the top bar. Defaults to '#5a6e7f'.
            fg_color (str, optional): Foreground color for the text in the top bar.
        Defaults to 'white'.
        """

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
        ttk.Button(self, text='Exportar', style='TButton', command=lambda: on_navigate('exportar')).grid(row=0, column=4, padx=5)
        ttk.Button(self, text='Importar', style='TButton', command=lambda: on_navigate('importar')).grid(row=0, column=5, padx=5)
        ttk.Button(self, text='Etiquetas', style='TButton', command=lambda: on_navigate('labels')).grid(row=0, column=6, padx=5)
        ttk.Button(self, text='Filtrar Projetos', style='TButton', command=lambda: on_navigate('filter_by_projects')).grid(row=0, column=7, padx=5)
        ttk.Button(self, text='Filtrar por Etiqueta', style='TButton', command=lambda: on_navigate('filter_by_labels')).grid(row=0, column=8, padx=5)
        ttk.Button(self, text='Remover Filtro', style='TButton', command=lambda: on_navigate('remove_filter')).grid(row=0, column=9, padx=5)

class ProjectList(tk.Frame):
    """ A custom tkinter Frame to display a list of projects.

    Attributes:
        parent (tk.Widget): The parent widget of this frame.
        user (User): The user object associated with the project list.
        bg_color (str): Background color for the project list.
    """

    def __init__(self, parent, user, bg_color='#ffffff'):
        """ Initialize the ProjectList.

        Parameters:
            parent (tk.Widget): The parent widget of this frame.
            user (User): The user object associated with the project list.
            bg_color (str, optional): Background color for the project list. Defaults to '#ffffff'.
        """

        super().__init__(parent, bg=bg_color, bd=1, relief='solid')

        self.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        parent.grid_rowconfigure(1, weight=1)

        title_label = tk.Label(self, text="Meus Projetos", font=('Arial', 18, 'bold'), bg=bg_color)
        title_label.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 20))

        self.user = user
        self.project_map = {}
        self.project_manager = ProjectDisplayManager(self, self.user)
        self.task_manager = TaskDisplayManager(self)
        self.subtask_manager = SubtaskDisplayManager(self)
        self.filtered_projects = self.user.projects
        
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
                                    # pylint: disable=unnecessary-lambda
                                    command= lambda: self.project_manager.open_create_page()
                                )
        open_create_project_button.grid(row=2, column=0, sticky='nsew')

    def show_project_page(self, project: Project):
        """ Display the page for a selected project.

        Parameters:
            project (Project): The project to display.
        """

        self.project_manager.open_page(project)

    # pylint: disable=unused-argument
    def on_double_click(self, event: object):
        """ Handle double-click events on project items.

        Parameters:
            event: The event object containing details of the double-click event.
        """

        item_id = self.tree.selection()[0]
        project_name = self.tree.item(item_id, 'tags')[0]
        project = self.project_map.get(project_name)

        if project:
            self.show_project_page(project)
        else:
            print("No project found for the selected item")

    def mock_projects(self) -> None:
        """ Populate the tree view with mock projects for demonstration purposes.
        """
        self.tree.tag_configure('projectname', font=('Arial', 12, 'bold'))
        self.tree.tag_configure('concluded', foreground='green')
        print(self.user.projects)
        for project in self.user.projects:
            if project.status:
                project_id = self.tree.insert('', tk.END, text=f'{project.name} - Concluído',\
                     open=True, tags=(project.name, 'projectname', 'concluded'))
            else:
                project_id = self.tree.insert('', tk.END, text=project.name, open=True,\
                     tags=(project.name, 'projectname'))

            self.project_map[project.name] = project
            for task in project.tasks:
                if not task.status:
                    self.tree.insert(project_id, tk.END, text=task.name)

    def update_main_page(self):
        """ Update the main page by refreshing the project list.
        """
        self.update_project_list(self.filtered_projects)

    def apply_filter(self, selected_projects):
        self.filtered_projects = selected_projects
        self.update_project_list(selected_projects)

    def update_project_list(self, projects):
        self.tree.delete(*self.tree.get_children())
        self.project_map.clear()

        self.tree.tag_configure('projectname', font=('Arial', 12, 'bold'))
        self.tree.tag_configure('concluded', foreground='green')

        for project in projects:
            if project.status:
                project_id = self.tree.insert('', tk.END, text=f'{project.name} - Concluído', open=True, tags=(project.name, 'projectname', 'concluded'))
            else:
                project_id = self.tree.insert('', tk.END, text=project.name, open=True, tags=(project.name, 'projectname'))

            self.project_map[project.name] = project
            for task in project.tasks:
                if not task.status:
                    self.tree.insert(project_id, tk.END, text=task.name)

    def apply_label_filter(self, selected_labels):
        filtered_projects = [project for project in self.user.projects if project.label in selected_labels]
        self.filtered_projects = filtered_projects
        self.update_project_list(filtered_projects)

    def remove_filter(self):
            self.filtered_projects = self.user.projects
            self.update_project_list(self.user.projects)

class HomePage(tk.Frame):
    """ A custom tkinter Frame that serves as the home page of the application.

    Attributes:
        parent (tk.Widget): The parent widget of this frame.
        user (User): The user object associated with the home page.
    """

    def __init__(self, parent: tk.Widget, user: User):
        """ Initialize the HomePage.

        Parameters:
            parent (tk.Widget): The parent widget of this frame.
            user (User): The user object associated with the home page.
        """
        super().__init__(parent)
        self.grid(row=0, column=0, sticky='nsew')

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.top_bar = TopBar(self, self.navigate)
        self.top_bar.grid(row=0, column=0, sticky='ew')
        self.user = user

        self.show_notification_page()

        self.project_list = ProjectList(self, self.user)
        self.project_list.grid(row=1, column=0, sticky='nsew')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.history_page = None
        self.calendar_page = None
        self.dashboard_page = None
        self.export_page = None
        self.import_page = None
        self.label_page = None
        self.project_filter_page = None
        self.label_filter_page =  None
        
    def apply_project_filter(self, selected_projects):
            self.project_list.apply_filter(selected_projects)
            tk.messagebox.showinfo("Filtro Aplicado", "Projetos filtrados com sucesso!")

    def apply_label_filter(self, selected_labels):
        self.project_list.apply_label_filter(selected_labels)
        tk.messagebox.showinfo("Filtro de Labels Aplicado", "Projetos filtrados por labels com sucesso!")

    def remove_project_filter(self):
        self.project_list.remove_filter()
        tk.messagebox.showinfo("Filtro Removido", "Todos os projetos estão agora visíveis.")

    def show_home_page(self):
        """
        Display the home page layout.
        """
        if self.calendar_page:
            self.calendar_page.interface.grid_forget()
        if self.dashboard_page:
            self.dashboard_page.grid_forget()
        if self.history_page:
            self.history_page.grid_forget()
        self.top_bar.grid(row=0, column=0, sticky='ew')
        self.project_list.grid(row=1, column=0, sticky='nsew')

    def show_calendar_page(self):
        """
        Display the calendar page layout.
        """
        self.project_list.grid_forget()
        self.top_bar.grid_forget()
        self.calendar_page = CalendarPage(master=self, on_close=self.show_home_page,\
             user = self.user)
        self.calendar_page.interface.grid(row=1, column=0, sticky='nsew')

    def show_dashboard_page(self) -> None:
        """
        Display the dashboard page layout.
        """
        self.project_list.grid_forget()
        self.top_bar.grid_forget()
        if not self.dashboard_page:
            self.dashboard_page = DashboardPage(master=self, on_close=self.show_home_page, user=self.user)
        self.dashboard_page.grid(row=1, column=0)

    def show_history_page(self) -> None:
        """
        Display the history page layout.
        """

        self.project_list.grid_forget()
        self.top_bar.grid_forget()
        if not self.history_page:
            self.history_page = HistoryManagerApp(master=self, on_close=self.show_home_page,\
                 controller=self, user = self.user)
        self.history_page.display_completed_tasks()
        self.history_page.grid(row=1, column=0, sticky='nsew')

    def show_export_page(self):
        """
        Display the export page layout.
        """
        self.export_page = ExportPage(master=self, controller=self, user = self.user,\
             project_list = self.project_list)

    def show_import_page(self) -> None:
        """
        Display the export page layout.
        """
        self.export_page = LoadPage(master=self, controller=self.project_list, user = self.user)

    def show_label_page(self) -> None:
        """
        Display the label page layout.
        """
        self.label_page = LabelManager(parent=self, controller=self, user = self.user)

    def show_filter_project_page(self):
        self.project_filter_page = ProjectFilterPage(master = self, user = self.user, controller=self, on_confirm=self.apply_project_filter)

    def show_label_filter_page(self):
        self.label_filter_page = LabelFilterPage(master = self, user = self.user, controller=self, on_confirm=self.apply_label_filter)
        
    def navigate(self, destination):
        """
        Navigate to a specified page in the application.

        Parameters:
            destination (str): The key representing the page to navigate to.
        """
        print(f"Navigating to {destination}")
        if destination == 'calendario':
            self.show_calendar_page()
        if destination == 'dashboard':
            self.show_dashboard_page()
        if destination == 'historico':
            self.show_history_page()
        if destination == 'exportar':
            self.show_export_page()
        if destination == 'importar':
            self.show_import_page()
        if destination == 'labels':
            self.show_label_page()
        if destination == 'filter_by_projects':
            self.show_filter_project_page()
        if destination == 'filter_by_labels':
            self.show_label_filter_page()
        if destination == 'remove_filter':
            self.remove_project_filter()

    def show_notification_page(self) -> None:
        """ Display the notification page layout.
        """
        notification_window = tk.Toplevel(self)
        NotificationPage(notification_window, self.user, self).pack()
