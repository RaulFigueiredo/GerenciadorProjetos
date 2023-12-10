"""Module: forms_base

This module contains classes representing various user interface widgets used in the application.

Classes:
    - EntryField: Represents a simple entry field.
    - DateField: Represents a field for selecting dates.
    - LabelCombobox: Represents a labeled combobox.
    - DescriptionText: Represents a labeled text area.

Attributes:
    - tk: The tkinter library used for GUI elements.
    - datetime: The datetime library for date manipulation.
    - ttk: The themed tkinter library for stylized widgets.
    - DateEntry: A themed date entry widget.

Example Usage:
    # Usage example of the classes in this module
    entry = EntryField(parent, label, width, padding, mediator)
    entry_value = entry.get_value()
    entry.set_value("New Value")

    date = DateField(parent, label, width, padding, mediator)
    date_value = date.get_value()
    date.set_value("New Date")

    combobox = LabelCombobox(parent, label, labels, width, padding, mediator)
    combobox_value = combobox.get_value()
    combobox.set_value("New Value")

    description = DescriptionText(parent, label, height, width, padding, mediator)
    description_value = description.get_value()
    description.set_value("New Text")
"""

import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry

class EntryField:
    """ Class: EntryField
    """
    def __init__(
            self,
            parent: tk,
            label: object,
            width: int,
            padding: int,
            mediator: object
        ):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)
        self.entry = tk.Entry(self.frame, width=width)
        self.entry.pack(side="right", **padding)

    def get_value(self):
        """ Gets the value of the entry field.

        Returns:
            _type_: The value of the entry field.
        """
        return self.entry.get().strip()

    def set_value(self, value: str) -> None:
        """ Sets the value of the entry field.

        Args:
            value (str): The value to be set.
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)  

class DateField:
    """ Class: DateField
    """
    def __init__(
            self,
            parent: tk,
            label: object,
            width: int,
            padding: int,
            mediator: object
        ):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)

        self.date = DateEntry(self.frame, width=width - 4, background='darkblue',
                                    foreground='white', borderwidth=2, state='readonly',
                                    date_pattern='dd/mm/yyyy')
        self.date.pack(side="right", **padding)

    def get_value(self) -> datetime.date:
        """ Gets the value of the date field.

        Returns:
            datetime.date: The value of the date field.
        """
        date_str = self.date.get()
        return datetime.strptime(date_str, '%d/%m/%Y').date()

    def set_value(self, value: str) -> None:
        """ Sets the value of the date field.

        Args:
            value (str): The value to be set.
        """
        self.date.set_date(value)

class LabelCombobox:
    """ Class: LabelCombobox
    """
    def __init__(
            self,
            parent: tk,
            label: object,
            labels: object,
            width: int,
            padding: int,
            mediator: object
        ):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)

        self.labels = [""] + labels
        self.combobox = ttk.Combobox(self.frame, values=self.labels,\
                                      width=width - 4, state="readonly")
        self.combobox.pack(side="right", **padding)

    def get_value(self) -> str:
        """ Gets the value of the combobox.

        Returns:
            str: The value of the combobox.
        """
        return self.combobox.get()

    def set_value(self, value: str) -> None:
        """ Sets the value of the combobox.

        Args:
            value (str): The value to be set.
        """
        self.combobox.set(value)

class DescriptionText:
    """ Class: DescriptionText
    """
    def __init__(
        self,
        parent: tk,
        label: object,
        height: int,
        width: int,
        padding: int,
        mediator: object
    ) -> None:
        """ Creates a text widget with a label.

        Args:
            parent (tk): Parent widget.
            label (object): Label of the text widget.
            height (int): Height of the text widget.
            width (int): Width of the text widget.
            padding (int): Padding of the text widget.
            mediator (object): Mediator of the text widget.
        """

        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label, font=("Arial", 12, "bold")).pack(side="top", **padding)

        self.text = tk.Text(self.frame, height=height, width=width)
        self.text.pack(side="bottom", **padding)

    def get_value(self) -> str:
        """ Gets the text of the text widget.

        Returns:
            str: The text of the text widget.
        """
        return self.text.get("1.0", "end").strip()

    def set_value(self, value: str) -> None:
        """ Sets the text of the text widget.

        Args:
            value (str): The text to be set.
        """
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", value)
