import tkinter as tk
from src.gui.authentication import Authentication
root = tk.Tk()
root.geometry("1600x900")

auth = Authentication(root)

root.mainloop()
