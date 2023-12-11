"""
History Manager Factory

This class creates instances of HistoryManagerApp using the Factory pattern.

Classes:
    HistoryManagerFactory: Factory class for creating HistoryManagerApp instances.

Usage:
    Use create_task_manager method to generate a HistoryManagerApp instance.

Returns:
    HistoryManagerApp: HistoryManagerApp instance.

Example:
    factory = HistoryManagerFactory()
    # Get root_window, user, and previous_window from somewhere
    task_manager = factory.create_task_manager(root_window, user, previous_window)
"""

import tkinter as tk
from src.logic.users.user import User
from src.gui.history_page import HistoryManagerApp

class HistoryManagerFactory:
    """ This class will be used to create a HistoryManagerApp instance

    Returns:
        HistoryManagerApp: HistoryManagerApp instance
    """
    @staticmethod
    def create_task_manager(root_window:tk.Tk,user:User,previous_window:tk.Tk) -> HistoryManagerApp:
        """ This method will be used to create a HistoryManagerApp instance

        Args:
            root_window (tk.Tk): Root window
            user (User): User instance
            previous_window (tk.Tk): Previous window

        Returns:
            HistoryManagerApp: HistoryManagerApp instance
        """
        return HistoryManagerApp(master=root_window,user=user,
                    controller=previous_window, on_close=previous_window.destroy)
