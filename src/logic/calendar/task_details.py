"""
This module implements the TaskDetails class
The TaskDetails class is responsible for managing and displaying task details in the user interface.
It offers functionalities to show and close task details, using TkInter widgets such as Frame,
Text, Scrollbar, and Button. This module is designed to be
integrated into a broader calendar application.
"""

import tkinter as tk
from typing import List, Tuple, Optional

class TaskDetails:
    """
    A class to manage and display task details within a TkInter application.

    Attributes:
        details_frame (tk.Frame): A TkInter frame widget to contain task details.
        details_text (tk.Text): A TkInter text widget to display task information.
        details_scroll (tk.Scrollbar): A scrollbar for the text widget.
        close_button (tk.Button): A button to close the task details view.

    Methods:
        show_task_details(task_info): Display the details of tasks.
        clear_details(): Clear the task details from the display.
        close_details(): Hide the task details frame.
    """

    def __init__(self, details_frame: tk.Frame, details_text: tk.Text,
                 details_scroll: tk.Scrollbar, close_button: tk.Button) -> None:
        """
        Initialize the TaskDetails object with provided TkInter widgets.

        Args:
            details_frame (tk.Frame): The frame to hold task details.
            details_text (tk.Text): The text widget for displaying task details.
            details_scroll (tk.Scrollbar): The scrollbar for the text widget.
            close_button (tk.Button): The button to close the details view.
        """
        self.details_frame = details_frame
        self.details_text = details_text
        self.details_scroll = details_scroll
        self.close_button = close_button
        self.close_button.configure(command=self.close_details)

    def show_task_details(self, task_info: Optional[List[Tuple[str]]]) -> None:
        """
        Display the details of tasks in the details frame.

        Args:
            task_info (List[Tuple[str]]): A list of task details, each task is a tuple.


        The method updates the text widget with the task details and makes
        the details frame visible.
        """
        self.details_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.clear_details()
        if task_info:
            self.details_text.config(state='normal')
            for task in task_info:
                self.details_text.insert('end', f"Projeto: {task[4]}\n")
                self.details_text.insert('end', f"Tarefa: {task[0]}\n")
                self.details_text.insert('end', f"Descrição: {task[3]}\n\n")
            self.details_text.config(state='disabled')

            self.details_text.grid(row=0, column=0, sticky='nsew')
            self.details_scroll.grid(row=0, column=1, sticky='ns')

        close_button = tk.Button(self.details_frame, text="Fechar", command=self.close_details)
        close_button.grid(row=1, column=0, columnspan=2, sticky='ne')

    def clear_details(self) -> None:
        """
        Clear the task details from the display.

        This method resets the text widget to be empty.
        """
        self.details_text.config(state='normal')
        self.details_text.delete('1.0', tk.END)
        self.details_text.config(state='disabled')

    def close_details(self) -> None:
        """
        Hide the task details frame.

        This method is typically connected to a button to close the details view.
        """
        self.details_frame.grid_remove()
