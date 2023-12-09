import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

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
    
    def set_value(self, value):
        self.entry.delete(0, tk.END)  
        self.entry.insert(0, value)   

class DateField:
    def __init__(self, parent, label, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label).pack(side="left", **padding)

        self.date = DateEntry(self.frame, width=width - 4, background='darkblue',
                                    foreground='white', borderwidth=2, state='readonly',
                                    date_pattern='dd/mm/yy')
        self.date.pack(side="right", **padding)

    def get_value(self):
        date_str = self.date.get()
        return datetime.strptime(date_str, '%d/%m/%y').date()  
    
    def set_value(self, value):
        self.date.set_date(value)  

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

    def set_value(self, value):
        self.combobox.set(value)

class DescriptionText:
    def __init__(self, parent, label, height, width, padding, mediator):
        self.mediator = mediator
        self.frame = ttk.Frame(parent)
        self.frame.pack(side="top", fill="x", **padding)
        tk.Label(self.frame, text=label, font=("Arial", 12, "bold")).pack(side="top", **padding)

        self.text = tk.Text(self.frame, height=height, width=width)
        self.text.pack(side="bottom", **padding)

    def get_value(self):
        return self.text.get("1.0", "end").strip()
    
    def set_value(self, value):
        self.text.delete("1.0", tk.END) 
        self.text.insert("1.0", value)   