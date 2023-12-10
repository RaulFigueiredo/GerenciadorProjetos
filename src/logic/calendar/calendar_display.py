"""
This module provides a graphical user interface.

The main class, CalendarDisplay, creates a window with a navigation bar,
a view of the current month, and a task details section. The user can navigate
through months and interact with tasks.
"""

import tkinter as tk
from typing import Callable as function

class CalendarDisplay(tk.Frame):
    """
    A class representing a calendar display using Tkinter.
    
    This class is responsible for creating the graphical interface of the calendar, including
    navigation between months, monthly view, and task details.
    
    Attributes:
        master (tk.Tk): The main window of the Tkinter application.
        on_close (Callable): Function to be called when the calendar is closed.
        navigation_frame (tk.Frame): Frame for navigation buttons.
        button_back (tk.Button): Button to move to the previous month.
        label_month_year (tk.Label): Label to display the current month and year.
        button_forward (tk.Button): Button to move to the next month.
        back_button (tk.Button): Button to return to the previous screen.
        calendar_frame (tk.Frame): Frame for the monthly calendar view.
        details_frame (tk.Frame): Frame for task details.
        details_text (tk.Text): Text field for task details.
        details_scroll (tk.Scrollbar): Scrollbar for the task details text field.
        close_button (tk.Button): Button to close the task details.
    
    Methods:
        __init__(self, master=None, on_close: Callable = None): Constructor of the class.
        close_calendar(self): Closes the calendar.
        create_navigation_frame(self): Creates the navigation frame.
        create_month_view(self): Creates the monthly view.
        create_task_details(self): Creates the task details.
    """

    def __init__(self, master=None, on_close: function = None):
        """Initializes the CalendarDisplay.
        
        Args:
            master (tk.Tk): The main window of the Tkinter application.
            on_close (Callable): Function to be called when the calendar is closed.
        """
        super().__init__(master)
        print(master)
        self.config(bg='lightblue')
        self.on_close = on_close

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Configurações de layout do Frame
        self.config(bg='lightblue')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.create_navigation_frame()
        self.create_month_view()
        self.create_task_details()


    def close_calendar(self) -> None:
        """
        Close the calendar window and execute the on_close callback if provided.
        """
        self.master.destroy()  # Destruir a janela principal

        if self.on_close:
            self.on_close()

    def create_navigation_frame(self) -> None:
        """
        Create and configure the navigation frame within the main window.
        """
        self.navigation_frame = tk.Frame(self)  # Referência ao próprio Frame
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_columnconfigure(1, weight=1)

        self.button_back = tk.Button(self.navigation_frame, text="<")
        self.button_back.grid(column=0, row=0)

        self.label_month_year = tk.Label(self.navigation_frame, font=("Arial", 20), bg='lightblue')
        self.label_month_year.grid(column=1, row=0)

        self.button_forward = tk.Button(self.navigation_frame, text=">")
        self.button_forward.grid(column=2, row=0)
        self.back_button = tk.Button(self.navigation_frame, text="Voltar",
                                     command=self.on_close)
        self.back_button.grid(column=0, row=1, sticky="w")

    def create_month_view(self) -> None:
        """
        Create and configure the month view frame within the main window.
        """

        self.calendar_frame = tk.Frame(self)  # Referência ao próprio Frame
        self.calendar_frame.grid(row=1, column=0, sticky='nsew')

    def create_task_details(self) -> None:
        """
        Create and configure the task details frame within the main window.
        """
        self.details_frame = tk.Frame(self, bg='white')  # Referência ao próprio Frame
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
