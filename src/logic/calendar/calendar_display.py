"""
This module provides a graphical user interface.

The main class, CalendarDisplay, creates a window with a navigation bar,
a view of the current month, and a task details section. The user can navigate
through months and interact with tasks.
"""

import tkinter as tk
from typing import Callable as function

class CalendarDisplay():
    """
    A class for creating and managing the main window of a calendar application.

    Attributes:
        window (tk.Tk): The main window of the application.
        navigation_frame (tk.Frame): Frame for navigation controls.
        button_back (tk.Button): Button to navigate to the previous month.
        label_month_year (tk.Label): Label displaying the current month and year.
        button_forward (tk.Button): Button to navigate to the next month.
        back_button (tk.Button): Button to go back from the current view.
        calendar_frame (tk.Frame): Frame for displaying the calendar view.
        details_frame (tk.Frame): Frame for showing task details.
        details_text (tk.Text): Text widget for displaying task details.
        details_scroll (tk.Scrollbar): Scrollbar for the details text widget.
        close_button (tk.Button): Button to close the task details section.

    Methods:
        close_calendar(): Closes the calendar window and executes
        the on_close callback, if provided.
        create_navigation_frame(): Creates and configures the navigation frame.
        create_month_view(): Creates and configures the month view frame.
        create_task_details(): Creates and configures the task details frame.
    """

    def __init__(self, master: tk.Tk = None, on_close: function = None) -> None:
        """
        Initialize the CalendarDisplay window.

        Args:
            master (tk.Tk, optional): The master widget. Defaults to a new tk.Tk() if None.
            on_close (function, optional): A callback function to execute when the window is closed.
        """
        self.window = master if master else tk.Tk()
        self.on_close = on_close
        self.window.title("Calendário")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = 100
        position_y = 100

        self.window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=0)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.config(bg='lightblue')

        self.create_navigation_frame()
        self.create_month_view()
        self.create_task_details()

    def close_calendar(self) -> None:
        """
        Close the calendar window and execute the on_close callback if provided.
        """
        self.window.destroy()
        if self.on_close:
            self.on_close()

    def create_navigation_frame(self) -> None:
        """
        Create and configure the navigation frame within the main window.
        """

        self.navigation_frame = tk.Frame(self.window)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_columnconfigure(1, weight=1)

        self.button_back = tk.Button(self.navigation_frame, text="<")
        self.button_back.grid(column=0, row=0)

        self.label_month_year = tk.Label(self.navigation_frame, font=("Arial", 20), bg='lightblue')
        self.label_month_year.grid(column=1, row=0)

        self.button_forward = tk.Button(self.navigation_frame, text=">")
        self.button_forward.grid(column=2, row=0)
        self.back_button = tk.Button(self.navigation_frame, text="Voltar",
                                     command=self.close_calendar)
        self.back_button.grid(column=0, row=1, sticky="w")

    def create_month_view(self) -> None:
        """
        Create and configure the month view frame within the main window.
        """
        self.calendar_frame = tk.Frame(self.window)
        self.calendar_frame.grid(row=1, column=0, sticky='nsew')

    def create_task_details(self) -> None:
        """
        Create and configure the task details frame within the main window.
        """

        self.details_frame = tk.Frame(self.window, bg='white')
        self.details_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.details_text = tk.Text(self.details_frame, wrap='word', height=40, width=30)
        self.details_scroll = tk.Scrollbar(self.details_frame, command=self.details_text.yview)
        self.details_text.configure(yscrollcommand=self.details_scroll.set)

        self.details_text.grid(row=0, column=0, sticky='nsew')
        self.details_scroll.grid(row=0, column=1, sticky='ns')

        self.details_frame.grid_rowconfigure(0, weight=1)
        self.details_frame.grid_columnconfigure(0, weight=1)

        self.close_button = tk.Button(self.details_frame, text="Fechar")
        self.close_button.grid(row=1, column=0, columnspan=2, sticky='ne')
