"""
This module provides the main structure for a calendar application using tkinter.
It includes the CalendarPage class for displaying the calendar with tasks
"""

from datetime import date
import tkinter as tk
from typing import Callable as function
from src import CalendarDisplay, TaskDetails, MonthView, MonthYearNavigation
from src.logic.users.user import User

class CalendarPage:
    """
    A class that represents the main page of a calendar application using Tkinter.

    This class integrates various components like CalendarDisplay, TaskDetails, and MonthView
    to provide a full-fledged calendar interface with task management capabilities.

    Attributes:
        interface (CalendarDisplay): The main calendar display component.
        tasks_dict (dict): Dictionary mapping dates to tasks and their details.
        task_details (TaskDetails): The component to display details of tasks.
        month_year_navigation (MonthYearNavigation): Component for navigating through
    months and years.
        month_view (MonthView): The view displaying the calendar for a specific month.

    Methods:
        __init__(self, master=None, on_close: Callable = None): Constructor of the class.
        update_calendar(self, month: int, year: int): Updates the calendar view for 
a given month and year.
        run(self): Placeholder method for future functionality.
    """
    def __init__(self, user: User , master: tk.Tk = None, on_close: function = None) -> None:
        """
        Initializes the CalendarPage with a given master widget and a callback for closure.

        Args:
            master (tk.Tk): The main window of the Tkinter application.
            on_close (Callable): Function to be called when the calendar page is closed.
        """
        self.interface = CalendarDisplay(master, on_close=on_close)
        self.user = user
        self.tasks_dict = self.create_task_dict()


        self.task_details = TaskDetails(
            self.interface.details_frame,
            self.interface.details_text,
            self.interface.details_scroll,
            self.interface.close_button
        )

        self.task_details.close_details()


        self.month_year_navigation = MonthYearNavigation(
            self.interface.navigation_frame,
            self.interface.button_back,
            self.interface.label_month_year,
            self.interface.button_forward,
            self.update_calendar
        )
        self.update_calendar(date.today().month, date.today().year)
    def create_task_dict(self) -> dict:
        """ Creates a dictionary mapping dates to tasks and their details.

        Returns:
            dict: A dictionary mapping dates to tasks and their details.
        """
        tasks_dict = {}
        color_dict = {"verde": "green", "azul": "blue", "vermelho": "red", "amarelo": "yellow", "laranja": "orange"}
        for project in self.user.projects:
            if project.label is None:
                label = ''
                color = 'gray'
            else:
                print('color: ', project.label)
                label = project.label.name
                color = color_dict[project.label.color]

            for task in project.tasks:
                name = task.name
                description = task.description
                task_date = None
                if task.end_date is not None:
                    task_date = task.end_date.strftime('%Y-%m-%d')
                project_name = project.name
                if task_date in tasks_dict:
                    tasks_dict[task_date].append((name, color, label, description, project_name))
                else:
                    tasks_dict[task_date] = [(name, color, label, description, project_name)]
        print(tasks_dict)
        return tasks_dict
    def update_calendar(self, month: int, year: int) -> None:
        """Updates the calendar view for a given month and year."""
        self.tasks_dict = self.create_task_dict()
        month_year_tuple = (month, year)
        self.month_view = MonthView(self.interface.calendar_frame,
                                    self.tasks_dict, self.task_details, month_year_tuple)

        self.month_view.generate_view()
