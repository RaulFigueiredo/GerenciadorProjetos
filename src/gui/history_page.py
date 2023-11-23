"""History Manager Application

This module implements a simple Tkinter-based interface to display completed
tasks using the HistoryManagerApp class.


Classes:
    HistoryManagerApp: Creates a Tkinter interface to display completed tasks.

Usage:
    Run the script to open the Tkinter window displaying completed tasks.

"""
import tkinter as tk
from src.logic.history.task_history import HistorySingleton
from tkinter import ttk
from src.logic.users.user import User

class HistoryManagerApp(tk.Frame):
    """ This class will be used to create a Tkinter interface to display completed tasks.
    """
    def __init__(self, master, controller, user) -> None:
        super().__init__(master)
        self.user = user
        self.controller = controller
        self.history = HistorySingleton()

        self.create_widgets()

    def create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)

        #self.history = HistorySingleton()
        #self.call_add_completed_task(self.call_list_of_projects(self.user))
        self.display_completed_tasks()

        back_button = ttk.Button(self, text="Back", command=self.controller.show_third_page)
        back_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    def display_completed_tasks(self) -> None:
        """ This method will be used to display completed tasks.
        """
        self.call_add_completed_task(self.user.projects)

        history_label = tk.Label(self,text="Completed Tasks",font=("Arial", 14, "bold"))
        history_label.grid(row=1, column=1, columnspan=2, pady=10, sticky="ns")

        completed_tasks = self.history.tasks_completed()

        # itereting over the list of completed tasks and displaying them
        for index, task in enumerate(completed_tasks):
            task_info = self.get_task_info(task)
            task_label = tk.Label(self, text=task_info, font=("Arial", 12))
            task_label.grid(row=index+2, column=1, columnspan=2, sticky="ns")

    def get_task_info(self, task: object) -> str:
        """ This method will be used to get the task information.

        Args:
            task (_type_): Task instance

        Returns:
            str: Task information
        """
        key, value = task.project.name, task.name
        return f"{key}: \t{value} - " + task.conclusion_date.strftime("%d/%m/%Y")

    def go_back(self) -> None:
        """ This method will be used to go back to the previous window.
        """
        self.controller.deiconify()
        self.destroy()

    def call_list_of_projects(self, user: User) -> list:
        """ This method will be used to call the list of projects.

        Returns:
            list: List of projects
        
        Obs:
            Alter it to call the list of projects from the database.
        """
        return user.projects

    def call_add_completed_task(self, list_of_projects: list) -> None:
        """ This method will be used to call the add_completed_task method
        from the HistorySingleton class.

        Args:
            list_of_projects (list): List of projects
        """
        self.history.add_completed_task(list_of_projects)