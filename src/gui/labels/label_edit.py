import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
This module provides a dialog interface for editing label properties
It allows users to change the name and color of a label in a graphical user interface.
"""

class EditLabelDialog:
    """
    A class to create an edit label dialog in a Tkinter graphical interface.

    Attributes:
        parent (tk.Widget): The parent widget for this dialog.
        current_name (str): The current name of the label to be edited.
        current_color (str): The current color of the label to be edited.
    """

    def __init__(self, parent: tk.Widget, current_name: str, current_color: str, existing_labels: list) -> None:
        """
        Initializes a new instance of EditLabelDialog.

        Parameters:
            parent (tk.Widget): The parent widget for this dialog.
            current_name (str): The current name of the label.
            current_color (str): The current color of the label.
            existing_labels (list): List of existing label names.
        """
        self.top = tk.Toplevel(parent)
        self.top.title("Editar Etiqueta")
        self.top.geometry("425x550+400+50")
        self.top.configure(bg='lightgray')

        self.existing_labels = existing_labels
        self.original_name = current_name

        frame = tk.Frame(self.top, bg='lightgray', pady=5)
        frame.pack(padx=10, pady=10, fill=tk.X)

        tk.Label(frame, text="Nome da Etiqueta:", bg='lightgray').pack(padx=10, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.insert(0, current_name)
        self.name_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(frame, text="Cor da Etiqueta:", bg='lightgray').pack(padx=10, pady=5)
        self.color_combobox = ttk.Combobox(frame, values=["azul", "verde", "vermelho"], state="readonly")
        self.color_combobox.set(current_color)
        self.color_combobox.pack(padx=10, pady=5, fill=tk.X)

        self.confirm_button = tk.Button(frame, text="Confirmar", command=self.on_confirm)
        self.confirm_button.pack(pady=10)

        self.result = None

        self.result = None

    def on_confirm(self) -> None:
        """
        Handles the confirmation event of the dialog, validating the input and returning the result.
        """
        name = self.name_entry.get().strip()
        color = self.color_combobox.get()

        if not name:
            messagebox.showwarning("Aviso", "O nome da etiqueta não pode estar vazio", parent=self.top)
            return

        if name in self.existing_labels and name != self.original_name:
            messagebox.showwarning("Aviso", "Esse nome de etiqueta já existe", parent=self.top)
            return

        self.result = (name, color)
        self.top.destroy()

    def show(self) -> tuple:
        """
        Displays the dialog and waits until it is closed.

        Returns:
            tuple: The name and color of the label, if confirmed, or None.
        """
        self.top.grab_set()
        self.top.wait_window()
        return self.result
