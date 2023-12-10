"""
Module Name: Module Name Here

Description:
This module contains classes and functions related to building a Tkinter
graphical interface for a dashboard application.

Classes:
- GridFrame: Represents a grid-based frame for organizing elements.
- GridLabel: Represents a labeled grid element.
- GridDropdown: Represents a dropdown widget within a grid.
- GridButton: Represents a button within a grid.
- DashboardUtils: Provides utility functions for the dashboard.
- DashboardPlots: Manages plots for the dashboard.
- Dashboard: Constructs the main dashboard interface.
- Sidebar: Represents the sidebar interface.
- DashboardPage: Constructs the dashboard page.

Dependencies:
- tkinter: Library for GUI elements.
- matplotlib.backends.backend_tkagg.FigureCanvasTkAgg: Used for embedding
Matplotlib plots in Tkinter.
- src.logic.dashboard.plot.Plot: Plotting functions for the dashboard.
- src.logic.dashboard.dashboard_data.DashboardData: Data management for the dashboard.
"""

import tkinter as tk
from tkinter import ttk

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
        self.top.title("Adicionar Etiqueta")

        self.top.geometry("300x300")

        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = (screen_width - 300) // 2
        y = (screen_height - 150) // 2

        self.top.geometry(f"+{x}+{y}")

        tk.Label(self.top, text="Nome da etiqueta:").pack(padx=10, pady=(15, 5))
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack(padx=10, pady=5)

        tk.Label(self.top, text="Cor da etiqueta:").pack(padx=10, pady=5)
        self.color_combobox = ttk.Combobox(self.top,
                 values=["azul", "verde", "vermelho"], state="readonly")
        self.color_combobox.pack(padx=10, pady=5)

        self.confirm_button = tk.Button(self.top, text="Confirmar", command=self.on_confirm)
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
