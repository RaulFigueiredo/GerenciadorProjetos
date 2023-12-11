"""
Module Name: GUI Initialization

Description:
This script initializes the graphical user interface (GUI) for the project management system.

- Imports the 'tkinter' library as 'tk'.
- Imports the 'Authentication' class from 'src.gui.authentication'.
- Initiates the main Tkinter application window with a title and specific dimensions (1600x900).
- Creates an instance of the 'Authentication' class, passing the root window.
- Enters the main event loop to start the GUI execution.

This script is responsible for launching the GUI and authentication interface for 
the project management system.
"""

import tkinter as tk
from src.gui.authentication import Authentication
root = tk.Tk()
root.title("Gerenciador de Projetos")
root.geometry("1600x900")

auth = Authentication(root)

root.mainloop()
