import tkinter as tk
from tkinter import ttk
import datetime
from src.logic.notifications.notifications2 import Notification
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.items.label import Label

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
    def __init__(self, master, user, controler):
        """ Initializes the NotificationPage class.

        Args:
            master (tkinter.Tk): The root window.
            user (User): An instance of the User class.
            controller (Controller): An instance of the controller class.
        """
        super().__init__(master)
        self.user = user
        self.controller = controler
