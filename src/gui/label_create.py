import tkinter as tk
from tkinter import ttk

"""
This module provides a dialog interface for adding new labels
It allows users to input a name and select a color for a new label in a graphical user interface.
"""

class AddLabelDialog:
    """
    A class for creating an add label dialog in a Tkinter graphical interface.

    This dialog allows users to enter a name and select a color for a new label.

    Attributes:
        parent (tk.Widget): The parent widget for this dialog.
    """

    def __init__(self, parent: tk.Widget) -> None:
        """
        Initializes a new instance of AddLabelDialog.

        Parameters:
            parent (tk.Widget): The parent widget for this dialog.
        """
        self.top = tk.Toplevel(parent)
        self.top.title("Add Label")

        tk.Label(self.top, text="Label Name:").pack(padx=10, pady=5)
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack(padx=10, pady=5)

        tk.Label(self.top, text="Label Color:").pack(padx=10, pady=5)
        self.color_combobox = ttk.Combobox(self.top, values=["blue", "green", "red"], state="readonly")
        self.color_combobox.pack(padx=10, pady=5)

        self.confirm_button = tk.Button(self.top, text="Confirm", command=self.on_confirm)
        self.confirm_button.pack(pady=10)

        self.result = None

    def on_confirm(self) -> None:
        """
        Handles the confirmation event of the dialog, capturing the entered name and selected color.
        """
        name = self.name_entry.get()
        color = self.color_combobox.get()
        self.result = (name, color)
        self.top.destroy()

    def show(self) -> tuple:
        """
        Displays the dialog and waits until it is closed.

        Returns:
            tuple: The entered name and selected color, if confirmed, or None.
        """
        self.top.grab_set()
        self.top.wait_window()
        return self.result
