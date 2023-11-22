"""
This module provides the main structure for a calendar application using tkinter.
It includes the CalendarPage class for displaying the calendar with tasks
"""

from datetime import date
import tkinter as tk
from src import CalendarDisplay, TaskDetails, MonthView, MonthYearNavigation
from typing import Callable as function

class CalendarPage:
    """
    A class for creating and managing a calendar page in the application.

    This class is responsible for the overall management of the calendar interface. 
    It includes functionalities for displaying the calendar, navigating through months 
    and years, and handling interactions with task details.

    Attributes:
        interface (CalendarDisplay): The main calendar display interface.
        tasks_dict (dict): A dictionary storing tasks with their details,
        used for populating the calendar with tasks.
        task_details (TaskDetails): The task details component of the calendar,
        used for displaying and managing task information.
        month_year_navigation (MonthYearNavigation): The navigation component for
        changing months and years, allowing user interaction for calendar navigation.

    Methods:
        update_calendar(month, year): Updates the calendar display based on the
        specified month and year, refreshing the task view.
        run(): Starts the main event loop for the calendar interface,
        keeping the application window active.
    """

    def __init__(self, master: tk.Widget = None, on_close: function = None) -> None:
        """
        Initialize the CalendarPage

        Args:
            master (tk.Widget, optional): The master widget. Defaults to None.
            on_close (function, optional): Callback function to execute when
            the calendar page closes. Defaults to None.
        """
        self.interface = CalendarDisplay(master, on_close=on_close)

        self.tasks_dict = {
            '2023-08-25': [('Atualizar dados', 'lightblue', 'TAG1', 'Descrição 3', 'Projeto A')],  
            '2023-11-05': [('limpar tapete', 'black', 'TAG1', 'Descrição 4', 'Projeto B')],   
            '2023-10-06': [('jogar no macaco', 'black', 'TAG1', 'Descrição 2', 'Projeto B')],   
            '2023-10-05': [('treinar perna', 'purple', 'TAG1', 'Descrição 21', 'Projto D'), 
            ('atividade de ciencia de redes', 'blue', 'TAG1', 'Desação 24', 'Projeto A'),
            ('vida bl', 'green', 'TAG1', 'Descrição 42', 'Projeto A'), ('Tare casa', 'red', 'TAG1',
            'Descrição 512', 'Projdsadasdas fdsa dsa adsdas dasd sa dsadasdsadeto A'),
            ('Tarefa de casa', 'red', 'TAG1', 'Descrição 512', 'ProjA')],
            '2023-11-22': [('crud etiquetas', 'red', 'TAG1', 'Descrição 213', 'Projeto A'),
                            ('atualizxa excel2', 'blue', 'TAG2', 'Descrição 214', 'Projeto B')],
            '2023-11-28': [('Tarefa xisquedele', 'green', 'TAG3', 'Descrição 2513', 'Projeto C')]
        }

        self.task_details = TaskDetails(
            self.interface.details_frame,
            self.interface.details_text,
            self.interface.details_scroll,
            self.interface.close_button
        )

        self.month_year_navigation = MonthYearNavigation(
            self.interface.navigation_frame,
            self.interface.button_back,
            self.interface.label_month_year,
            self.interface.button_forward,
            self.update_calendar
        )
        self.update_calendar(date.today().month, date.today().year)

    def update_calendar(self, month: int, year: int) -> None:
        """
        Update the calendar display based on the specified month and year.

        Args:
            month (int): The month to display.
            year (int): The year to display.
        """
        month_year_tuple = (month, year)  # Criando a tupla com month e year
        self.month_view = MonthView(self.interface.calendar_frame,
                                    self.tasks_dict, self.task_details, month_year_tuple)

        self.month_view.generate_view()


    def run(self) -> None:
        """
        Run the main event loop for the calendar interface.
        """
        self.interface.window.mainloop()

class StartPage:
    def __init__(self):
        self.create_window()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Página Inicial")

        self.start_button = tk.Button(self.window, text="Abrir Calendário",
                                      command=self.open_calendar)
        self.start_button.pack(pady=20)

    def open_calendar(self):
        self.window.destroy()
        calendar_page = CalendarPage(on_close=self.create_window)
        calendar_page.run()


if __name__ == "__main__":
    start_page = StartPage()
    start_page.window.mainloop()
