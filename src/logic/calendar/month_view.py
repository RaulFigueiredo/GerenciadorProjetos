import tkinter as tk
from src.logic.calendar.date_utilities import DateUtilities

class MonthView:
    def __init__(self, calendar_frame, tasks_dict, task_details):
        self.calendar_frame = calendar_frame
        self.tasks_dict = tasks_dict
        self.task_details = task_details


    def generate_view(self, month, year):
        self.month = month
        self.year = year
        self.clear_view()
        self.create_day_headers()
        self.fill_days_with_tasks()

    def clear_view(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

    def create_day_headers(self):
        day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i, name in enumerate(day_names):
            label = tk.Label(self.calendar_frame, text=name, fg="black")
            label.grid(column=i, row=0, sticky='nsew')

    def fill_days_with_tasks(self):
        start_date = DateUtilities.day_month_starts(self.month, self.year)
        number_of_days = DateUtilities.days_in_month(self.month, self.year)
        index = 0
        day = 1
        for row in range(6):
            for column in range(7):
                if index >= start_date and index <= start_date + number_of_days - 1:
                    dayStr = f"{self.year}-{self.month:02d}-{day:02d}"
                    taskInfo = self.tasks_dict.get(dayStr)

                    dayFrame = tk.Frame(self.calendar_frame, bd=1, relief='ridge') 
                    dayFrame.grid(row=row + 2, column=column, sticky='nsew', padx=1, pady=1)
                    dayFrame.columnconfigure(0, weight=1)

                    text = tk.Text(dayFrame, width=15, height=5, padx=5, pady=5, borderwidth=0, highlightthickness=0)
                    text.grid(row=1)
                    text.config(state='normal')
                    text.insert('end', "\n")  
                    text.config(state='disabled')

                    if taskInfo:
                        for i, task in enumerate(taskInfo):
                            text.config(state='normal')
                            text.insert('end', f"{task[0]}\n")
                            text.config(state='disabled')

                            tag_name = f"tag{i}"
                            text.tag_add(tag_name, f"{i+2}.0", f"{i+2}.end")
                            text.tag_config(tag_name, background=task[1], foreground='white')

                    text.bind("<Button-1>", lambda e, d=dayStr: self.showTaskDetails(d))

                    dayLabel = tk.Label(dayFrame, text=str(day))
                    dayLabel.grid(row=0, column=0, sticky='nw')

                    day += 1
                index += 1

    def showTaskDetails(self, dayStr):
        taskInfo = self.tasks_dict.get(dayStr)
        if taskInfo:
            self.task_details.show_task_details(taskInfo)
