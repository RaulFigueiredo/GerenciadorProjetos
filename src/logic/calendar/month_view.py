"""
This module provides the MonthView class for creating and managing a monthly calendar view. 
The class supports displaying days, weekdays, and tasks for each day in a given month and year. 
It integrates with a task details management system to show detailed 
information about tasks on specific dates.
"""

import tkinter as tk
from src.logic.calendar.date_utilities import DateUtilities

class MonthView:
    """
    A class for generating and managing a monthly view

    Attributes:
        calendar_frame (tk.Frame): The frame in which the monthly calendar view is displayed.
        tasks_dict (dict): A dictionary mapping dates to tasks.
        task_details (TaskDetails): An object to manage and display task details.
        monthyear (Tuple[int, int]): A tuple containing the month and year to display.

    Methods:
        generate_view(): Generates the calendar view for a specific month and year.
        clear_view(): Clears the current view in the calendar frame.
        create_day_headers(): Creates headers for the days of the week.
        fill_days_with_tasks(): Populates the calendar with tasks for each day.
        show_task_details_view(day_str): Displays the details for tasks on a given day.
    """

    def __init__(self, calendar_frame: tk.Frame, tasks_dict: dict, task_details, monthyear) -> None:
        """
        Initialize the MonthView object with the calendar frame, tasks dictionary,
        and task details object.

        Args:
            calendar_frame (tk.Frame): The frame for displaying the calendar view.
            tasks_dict (dict): A dictionary mapping dates to tasks.
            task_details (TaskDetails): The object to manage and display details of tasks.
            monthyear (Tuple[int, int]): A tuple containing the month and year to display.
        """
        self.calendar_frame = calendar_frame
        self.tasks_dict = tasks_dict
        self.task_details = task_details
        self.month_year = monthyear

        self.screen_width = self.calendar_frame.winfo_screenwidth()
        self.screen_height = self.calendar_frame.winfo_screenheight()

        self.month = self.month_year[0]
        self.year = self.month_year[1]

    def generate_view(self) -> None:
        """
        Generate the calendar view for the specified month and year.

        This method updates the calendar view, showing days, weekdays, and tasks.
        """
        self.clear_view()
        self.create_day_headers()
        self.fill_days_with_tasks()

    def clear_view(self) -> None:
        """
        Clear all widgets from the calendar frame.

        This method destroys all widgets currently in the calendar_frame, 
        effectively clearing the current monthly view.
        """
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

    def create_day_headers(self) -> None:
        """
        Create headers for each day of the week.

        This method adds labels for Sunday through Saturday at the top of the calendar view.
        """
        day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i, name in enumerate(day_names):
            label = tk.Label(self.calendar_frame, text=name, fg="black")
            label.grid(column=i, row=0, sticky='nsew')

    def fill_days_with_tasks(self) -> None:
        """
        Populate the calendar view with tasks for each day.

        This method arranges tasks in the calendar view based on the current month and year,
        using the tasks_dict to retrieve tasks for each day.
        """
        start_date = DateUtilities.day_month_starts(self.month, self.year)
        number_of_days = DateUtilities.days_in_month(self.month, self.year)
        index = 0
        day = 1
        for row in range(6):
            for column in range(7):
                if start_date <= index <= start_date + number_of_days - 1:
                    day_str = f"{self.year}-{self.month:02d}-{day:02d}"
                    task_info = self.tasks_dict.get(day_str)
                    day_width = int(self.screen_width * 0.008)
                    day_height = int(self.screen_height * 0.004)

                    day_frame = tk.Frame(self.calendar_frame, bd=1, relief='ridge')
                    day_frame.grid(row=row + 2, column=column, sticky='nsew', padx=1, pady=1)
                    day_frame.columnconfigure(0, weight=1)

                    text = tk.Text(day_frame, width=day_width, height=day_height, padx=5, pady=5,
                                borderwidth=0, highlightthickness=0)
                    text.grid(row=1)
                    text.config(state='normal')
                    text.insert('end', "\n")
                    text.config(state='disabled')

                    if task_info:
                        for i, task in enumerate(task_info):
                            text.config(state='normal')
                            text.insert('end', f"{task[0]}\n")
                            text.config(state='disabled')

                            tag_name = f"tag{i}"
                            text.tag_add(tag_name, f"{i+2}.0", f"{i+2}.end")
                            text.tag_config(tag_name, background=task[1], foreground='white')

                    text.bind("<Button-1>", lambda e, d=day_str: self.show_task_details_view(d))

                    day_label = tk.Label(day_frame, text=str(day))
                    day_label.grid(row=0, column=0, sticky='nw')

                    day += 1
                index += 1

    def show_task_details_view(self, day_str: str) -> None:
        """
        Display the task details for a given day.

        Args:
            day_str (str): A string representing the day (YYYY-MM-DD format) to show details for.

        This method uses the task_details object to display details for tasks on the specified day.
        """
        task_info = self.tasks_dict.get(day_str)
        if task_info:
            self.task_details.show_task_details(task_info)
