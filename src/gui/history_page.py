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
from src.logic.users.user import User

class HistoryManagerApp:
    """ This class will be used to create a Tkinter interface to display completed tasks.
    """
    def __init__(self, root_window: tk.Tk, user: User, previous_window: tk.Tk) -> None:
        self.root_window = root_window
        self.user = user
        self.previous_window = previous_window

        self.root_window.title("History of Completed Tasks")
        self.root_window.geometry("600x400")

        self.history = HistorySingleton()
        self.call_add_completed_task(self.call_list_of_projects(self.user))
        self.display_completed_tasks()

        back_button = tk.Button(self.root_window, text="Close", command=self.go_back)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    def display_completed_tasks(self) -> None:
        """ This method will be used to display completed tasks.
        """
        history_label = tk.Label(self.root_window,text="Completed Tasks",font=("Arial", 14, "bold"))
        history_label.grid(row=1, column=1, columnspan=2, pady=10, sticky="ns")

        completed_tasks = self.history.tasks_completed()

        for idx, task in enumerate(completed_tasks, start=2):
            task_info = self.get_task_info(task)
            task_label = tk.Label(
                self.root_window,
                  text=task_info,
                    bg=task.project.label.color,
                      relief="groove"
            )
            task_label.grid(row=idx, column=0, columnspan=2, sticky="ns", padx=10, pady=5)

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
        self.previous_window.deiconify()
        self.root_window.destroy()

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
