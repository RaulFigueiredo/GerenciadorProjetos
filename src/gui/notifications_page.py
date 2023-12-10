"""
    This module creates a Tkinter interface to display notifications for tasks.

    It imports necessary modules and creates instances of users, labels, projects, and tasks
for demonstration purposes.

    It defines a `NotificationPage` class that inherits from Tkinter's `Frame` class.
The class provides methods to create a GUI displaying different categories of tasks
such as urgent tasks, tasks due for today, and tasks with notifications for the day.

"""
import tkinter as tk
from tkinter import ttk
from src.logic.notifications.notification import Notification

class NotificationPage(tk.Frame):
    """This class creates a Tkinter interface to display notifications.

    Args:
        master (tkinter.Tk): The root window.
        user (User): An instance of the User class.
        controller (Controller): An instance of the controller class.

    Attributes:
        user (User): An instance of the User class.
        controller (Controller): An instance of the controller class.
    """
    def __init__(self, master: tk, user: callable, controler:tk):
        """ Initializes the NotificationPage class.

        Args:
            master (tkinter.Tk): The root window.
            user (User): An instance of the User class.
            controller (Controller): An instance of the controller class.
        """
        super().__init__(master)
        self.user = user
        self.controller = controler
        self.create_widgets()
        # size of the window
        self.master.geometry("600x400")
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.master.title("Notificações")

    def create_widgets(self) -> None:
        """ This method will be used to create the widgets.
        """
        notfi = Notification(self.user)
        notfi.check_notification_date()
        notfi.check_due_date()

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(6, weight=1)

        name_label = tk.Label(self, text="Aba de Notificações", font=("Arial", 24))
        name_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        urgent_frame = ttk.Frame(self)
        urgent_frame.grid(row=1, column=0, sticky="ew", padx=10)
        urgent_frame.grid_columnconfigure(0, weight=1)

        label_urgent = tk.Label(urgent_frame, text="Tarefa Urgente", font=("Arial", 12, "bold"))
        label_urgent.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        for index, task in enumerate(notfi.urgent_tasks):
            task_info = self.get_task_info(task)
            task_label = tk.Label(urgent_frame, text=task_info, font=("Arial", 12))
            task_label.grid(row=index+1, column=0, sticky="w", padx=5, pady=5)

        due_date_frame = ttk.Frame(self)
        due_date_frame.grid(row=2, column=0, sticky="ew", padx=10)
        due_date_frame.grid_columnconfigure(0, weight=1)

        label_due_date = tk.Label(due_date_frame, text="Entrega para hoje",font=("Arial",12,"bold"))
        label_due_date.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        for index, task in enumerate(notfi.due_date_tasks):
            task_info = self.get_task_info(task)
            task_label = tk.Label(due_date_frame, text=task_info, font=("Arial", 12))
            task_label.grid(row=index+1, column=0, sticky="w", padx=5, pady=5)

        notification_date_frame = ttk.Frame(self)
        notification_date_frame.grid(row=3, column=0, sticky="ew", padx=10)
        notification_date_frame.grid_columnconfigure(0, weight=1)

        label_notification_date = tk.Label(notification_date_frame,
                                            text="Notificação para hoje",font=("Arial",12,"bold"))
        label_notification_date.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        for index, task in enumerate(notfi.notification_date_tasks):
            task_info = self.get_task_info(task)
            task_label = tk.Label(notification_date_frame, text=task_info, font=("Arial", 12))
            task_label.grid(row=index+1, column=0, sticky="w", padx=5, pady=5)

        tasks_frame = ttk.Frame(self)
        tasks_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 0))
        tasks_frame.grid_columnconfigure(1, weight=1)

        back_button = ttk.Button(self, text="Voltar", command=self.on_close)
        back_button.grid(row=5, column=0, sticky="ew", padx=10, pady=10)

    def on_close(self) -> None:
        """ This method will be used to close the window.
        """
        self.master.destroy()

    def get_task_info(self, task: object) -> str:
        """ Gets information about a task.

        Args:
            task (object): An instance of the Task class.

        Returns:
            str: Information about the task.
        """
        key, value = task.project.name, task.name
        return f"{key}: \t{value} \t" + task.end_date.strftime("%d/%m/%Y")
