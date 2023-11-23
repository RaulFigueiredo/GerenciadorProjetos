import tkinter as tk
from src.gui.authentication import Authentication
root = tk.Tk()
root.geometry("800x600")

auth = Authentication(root)

root.mainloop()
