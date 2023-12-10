"""Module: Input Fields

This module provides classes for different types of input fields to be used in GUI forms.

Classes:
    EntryField: Represents a simple entry field.
    DateField: Represents a field for selecting dates.
    LabelCombobox: Represents a labeled combobox for selections.
    DescriptionText: Represents a text field for descriptions.

Functions:
    - No module-level functions documented -

Example Usage:
    # Example usage of EntryField class
    root = tk.Tk()
    mediator = Mediator()
    entry_field = EntryField(root, "Name:", 20, {'padx': 10, 'pady': 5}, mediator)
    value = entry_field.get_value()
"""

import tkinter as tk
from tkinter import ttk

from src.gui.mediator import FormMediator

class EntryField:
    """ Represents a simple entry field.
    """
    def __init__(self, parent, label, width, padding, mediator):
        """Represents a simple entry field.

        Args:
            parent (object): Parent window.
            label (object): Label of the entry field.
            width (object): Width of the entry field.
            padding (object): Padding of the entry field.
            mediator (object): Mediator of the entry field.
        """

class DateField:
    """ Represents a field for selecting dates.
    """
    def __init__(self, parent, label, width, padding, mediator):
        """Represents a field for selecting dates.

        Args:
            parent (object): Parent window.
            label (object): Label of the date field.
            width (object): Width of the date field.
            padding (object): Padding of the date field.
            mediator (object): Mediator of the date field.
        """

class LabelCombobox:
    """ Represents a labeled combobox for selections.
    """
    def __init__(
            self,
            parent:object,
            label: str,
            labels:object,
            width:int,
            padding:int,
            mediator:int
        ):
        """Represents a labeled combobox for selections.

        Args:
            parent (object): Parent window.
            label (object): Label of the combobox.
            labels (object): Labels of the combobox.
            width (object): Width of the combobox.
            padding (object): Padding of the combobox.
            mediator (object): Mediator of the combobox.
        """
class DescriptionText:
    """ Represents a text field for descriptions.
    """
    def __init__(
            self,
            parent: object,
            label: str,
            height: int,
            width:int,
            padding: int,
            mediator: FormMediator
        ):
        """Represents a text field for descriptions.

        Args:
            parent (object): Parent window.
            label (object): Label of the text field.
            height (object): Height of the text field.
            width (object): Width of the text field.
            padding (object): Padding of the text field.
            mediator (object): Mediator of the text field.
        """
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label, font=("Arial", 12, "bold")).pack(side="top", **padding)

        self.text = tk.Text(self.frame, height=height, width=width)
        self.text.pack(side="bottom", **padding)

    def get_value(self) -> str:
        """ Gets the value of the text field.

        Returns:
            str: Value of the text field.
        """
        return self.text.get("1.0", "end").strip()

    def set_value(self, value: str) -> None:
        """ Sets the value of the text field.

        Args:
            value (object): Value to be set.
        """
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", value)
