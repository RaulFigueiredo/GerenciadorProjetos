import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class EntryField:
    def __init__(self, parent, label, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)
        self.entry = tk.Entry(self.frame, width=width)
        self.entry.pack(side="right", **padding)

    def get_value(self):
        return self.entry.get().strip()


class DateField:
    def __init__(self, parent, label, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)

        self.date = DateEntry(self.frame, width=width - 4, background='darkblue',
                                    foreground='white', borderwidth=2, state='readonly')
        self.date.pack(side="right", **padding)

    def get_value(self):
        return self.date.get()


class LabelCombobox:
    def __init__(self, parent, label, labels, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)

        self.labels = [""] + labels
        self.combobox = ttk.Combobox(self.frame, values=self.labels, width=width - 4, state="readonly")
        self.combobox.pack(side="right", **padding)

    def get_value(self):
        return self.combobox.get()


class DescriptionText:
    def __init__(self, parent, label, height, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="top", **padding)

        self.text = tk.Text(self.frame, height=height, width=width)
        self.text.pack(side="bottom", **padding)

    def get_value(self):
        return self.text.get("1.0", "end").strip()
