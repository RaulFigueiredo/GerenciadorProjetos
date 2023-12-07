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
    A class that represents the main page of a calendar application using Tkinter.

    This class integrates various components like CalendarDisplay, TaskDetails, and MonthView
    to provide a full-fledged calendar interface with task management capabilities.

    Attributes:
        interface (CalendarDisplay): The main calendar display component.
        tasks_dict (dict): Dictionary mapping dates to tasks and their details.
        task_details (TaskDetails): The component to display details of tasks.
        month_year_navigation (MonthYearNavigation): Component for navigating through months and years.
        month_view (MonthView): The view displaying the calendar for a specific month.

    Methods:
        __init__(self, master=None, on_close: Callable = None): Constructor of the class.
        update_calendar(self, month: int, year: int): Updates the calendar view for a given month and year.
        run(self): Placeholder method for future functionality.
    """
    def __init__(self, master: tk.Tk = None, on_close: function = None) -> None:
        """
        Initializes the CalendarPage with a given master widget and a callback for closure.

        Args:
            master (tk.Tk): The main window of the Tkinter application.
            on_close (Callable): Function to be called when the calendar page is closed.
        """
        self.interface = CalendarDisplay(master, on_close=on_close)

        self.tasks_dict = {
            '2023-08-25': [('Atualizar dados', 'lightblue', 'TAG112', 'Descrição 3', 'Projeto AP')],  
            '2023-11-05': [('limpar tapete da sala', 'black', 'TAG1', 'Descrição 4', 'Projeto BQ')],   
            '2023-10-06': [('jogar futebol com os amigos', 'black', 'TAG1', 'Descrição 2', 'Projeto BE')],   
            '2023-10-05': [('treinar perna', 'purple', 'TAG15', 'Descrição 21', 'Projto DA'), 
            ('atividade de ciencia de redes', 'blue', 'TAG1432', 'Desação 24', 'Projeto AC'),
            ('vida bl', 'green', 'TAG1754', 'Descrição 42', 'Projeto A'), ('Limpar cozinha', 'red', 'TAG34141',
            'Descrição 512', 'Projeto A'),
            ('Tarefa de casa', 'red', 'TAG1512', 'Descrição 512', 'ProjA')],
            '2023-11-22': [('crud etiquetas', 'red', 'TAG1', 'Descrição 213', 'Projeto AZ'),
                            ('atualizxa excel2', 'blue', 'TAG15422', 'Descrição 214', 'Projeto BC')],
            '2023-11-28': [('Tarefa xisquedele', 'green', 'TAG313', 'Descrição 2513', 'Projeto CG')]
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
        """Updates the calendar view for a given month and year."""
        month_year_tuple = (month, year)  
        self.month_view = MonthView(self.interface.calendar_frame,
                                    self.tasks_dict, self.task_details, month_year_tuple)

        self.month_view.generate_view()

class StartPage:


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Página Inicial")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        # Definir a geometria da janela
        self.window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        self.create_widgets()
        self.calendar_page = None

    def create_widgets(self):
        self.start_button = tk.Button(self.window, text="Abrir Calendário",
                                      command=self.open_calendar)
        self.start_button.pack(pady=20)

    def open_calendar(self):
        self.start_button.pack_forget()
        if not self.calendar_page:
            self.calendar_page = CalendarPage(master=self.window, on_close=self.show_start_button)
        self.calendar_page.interface.pack(fill='both', expand=True)

    def show_start_button(self):
        if self.calendar_page:
            self.calendar_page.interface.pack_forget()
        self.start_button.pack(pady=20)

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    start_page = StartPage()
    start_page.mainloop()