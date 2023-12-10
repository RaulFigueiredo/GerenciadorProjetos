"""
This module defines the MonthYearNavigation class
It provides functionality for navigating through months and years, with forward and back buttons,
and a display label for the current month and year. The class updates the calendar view upon
navigation changes. Designed to be integrated into larger TkInter calendar applications.
"""

from datetime import date
from typing import Tuple, Callable as function
import tkinter as tk

class MonthYearNavigation:
    """
    A class to manage navigation through months and years in a calendar interface.

    Attributes:
        navigation_frame (tk.Widget): The frame widget containing the navigation controls.
        button_back (tk.Button): Button to navigate to the previous month.
        label_month_year (tk.Label): Label displaying the current month and year.
        button_forward (tk.Button): Button to navigate to the next month.
        update_callback (function): Callback function to update the calendar display.
        month (int): Current month being displayed.
        year (int): Current year being displayed.

    Methods:
        update_display(month, year): Updates the display with the given month and year.
        change_month(direction): Changes the current month based on the direction.
    """

    def __init__(self, navigation_frame: tk.Widget, button_back: tk.Button,
                 label_month_year: tk.Label, button_forward: tk.Button,
                 update_callback: function) -> None:
        """
        Initialize the MonthYearNavigation object with provided navigation controls and callback.

        Args:
            navigation_frame (tk.Widget): Frame widget containing the navigation controls.
            button_back (tk.Button): Button to move to the previous month.
            label_month_year (tk.Label): Label to display the current month and year.
            button_forward (tk.Button): Button to move to the next month.
            update_callback (function): Callback to update the calendar 
                                        when the month or year changes.
        """

        self.navigation_frame = navigation_frame
        self.button_back = button_back
        self.label_month_year = label_month_year
        self.button_forward = button_forward
        self.update_callback = update_callback
        self.month = date.today().month
        self.year = date.today().year

        self.button_back.configure(command=lambda: self.update_display(*self.change_month(-1)))
        self.button_forward.configure(command=lambda: self.update_display(*self.change_month(1)))
        self.update_display(self.month, self.year)

    def update_display(self, month: int, year: int) -> Tuple[str, int]:
        """
        Update the month and year display and trigger the update callback.

        Args:
            month (int): Month to display.
            year (int): Year to display.

        Returns:
            Tuple[str, int]: The written month and year.

        This method updates the label_month_year with the new month and year, 
        and calls the update_callback function to update the calendar display.
        """
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        written_month = months[month - 1]
        self.label_month_year.config(text=f"{written_month} {year}")
        self.update_callback(month, year)

        return written_month, year

    def change_month(self, direction: int) -> Tuple[int, int]:
        """
        Change the current month based on the given direction.

        Args:
            direction (int): The direction to change the month. 
                             -1 for the previous month, +1 for the next month.

        Returns:
            Tuple[int, int]: The new month and year after the change.

        This method adjusts the current month and year, wrapping around the 
        calendar year as necessary.
        """
        self.month += direction
        if self.month > 12:
            self.month = 1
            self.year += 1
        elif self.month < 1:
            self.month = 12
            self.year -= 1
        return self.month, self.year
