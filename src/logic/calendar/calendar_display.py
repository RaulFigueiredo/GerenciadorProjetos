import tkinter as tk

class CalendarDisplay():
    def __init__(self, master=None, on_close=None):
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

    def close_calendar(self):
        self.window.destroy()
        if self.on_close:
            self.on_close()

    def create_navigation_frame(self):
        self.navigation_frame = tk.Frame(self.window)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_columnconfigure(1, weight=1)

        self.button_back = tk.Button(self.navigation_frame, text="<")
        self.button_back.grid(column=0, row=0)

        self.label_month_year = tk.Label(self.navigation_frame, font=("Arial", 20), bg='lightblue')
        self.label_month_year.grid(column=1, row=0)

        self.button_forward = tk.Button(self.navigation_frame, text=">")
        self.button_forward.grid(column=2, row=0)
        self.back_button = tk.Button(self.navigation_frame, text="Voltar", command=self.close_calendar)
        self.back_button.grid(column=0, row=1, sticky="w")

    def create_month_view(self):
        self.calendar_frame = tk.Frame(self.window)
        self.calendar_frame.grid(row=1, column=0, sticky='nsew')

    def create_task_details(self):

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