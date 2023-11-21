from src import CalendarDisplay, TaskDetails, MonthView, MonthYearNavigation

from datetime import date
import tkinter as tk

class CalendarPage:
    def __init__(self, master=None, on_close=None):
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

        self.month_view = MonthView(self.interface.calendar_frame,
                                    self.tasks_dict, self.task_details)
        self.month_year_navigation = MonthYearNavigation(
            self.interface.navigation_frame,
            self.interface.button_back,
            self.interface.label_month_year,
            self.interface.button_forward,
            self.update_calendar
        )
        self.update_calendar(date.today().month, date.today().year)

    def update_calendar(self, month: int, year: int):
        self.month_view.generate_view(month, year)


    def run(self):
        self.interface.window.mainloop()

class StartPage:
    def __init__(self):
        self.create_window()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Página Inicial")

        self.start_button = tk.Button(self.window, text="Abrir Calendário", command=self.open_calendar)
        self.start_button.pack(pady=20)

    def open_calendar(self):
        self.window.destroy()
        calendar_page = CalendarPage(on_close=self.create_window)
        calendar_page.run()


if __name__ == "__main__":
    start_page = StartPage()
    start_page.window.mainloop()