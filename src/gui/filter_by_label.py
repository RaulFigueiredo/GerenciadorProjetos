"""
Module Name: Label Filter Page

Description:
This module manages a graphical window used for filtering labels. It presents users with
options to select specific labels for filtering based on their preferences.

- Imports the 'tkinter' library.
- Defines the 'LabelFilterPage' class for managing the label filtering window.

- Initializes the window with parameters like the master window, current user, controller,
  and a callback function for confirmation.
- Allows users to select labels for filtering and confirm their selection.

Methods:
    - __init__(master, user, controller, on_confirm): Initializes the label filter window.
    - create_widgets(): Creates widgets for the page (labels, listbox, and confirm button).
    - confirm_selection(): Confirms the selection of labels and closes the window.
    - center_window(width, height): Centers the window on the screen based on width and height.
    - on_window_close(): Handles the window closure and sets the controller's window to None.
"""


import tkinter as tk

class LabelFilterPage(tk.Toplevel):
    """ Class for the label filter window.

    Args:
        tk (tk.Toplevel): Toplevel window.
    """
    def __init__(self, master, user, controller, on_confirm):
        if hasattr(controller, 'label_filter_page_window') and controller.label_filter_page_window:
            controller.label_filter_page_window.destroy()

        super().__init__(master)
        self.user = user
        self.controller = controller
        self.on_confirm = on_confirm

        self.title("Filtrar por Etiquetas")
        self.configure(bg="white")
        self.create_widgets()
        self.center_window(320, 320)

        controller.label_filter_page_window = self

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def create_widgets(self) -> None:
        """ Creates the widgets for the page.
        """
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(padx=10, pady=10)

        label_title = tk.Label(main_frame, text="Filtrar por etiquetas",
                     font=("Arial", 16), bg="white")
        label_title.pack(pady=(0, 5))

        label_subtitle = tk.Label(main_frame, text="Selecione as etiquetas para filtrar",
                     font=("Arial", 12), bg="white")
        label_subtitle.pack(pady=(0, 10))

        self.listbox = tk.Listbox(main_frame, selectmode='multiple')
        self.listbox.pack(fill="both", expand=True)

        for label in self.user.labels:
            self.listbox.insert(tk.END, label.name)

        confirm_button = tk.Button(main_frame, text="Confirmar Seleção",
                     command=self.confirm_selection)
        confirm_button.pack(pady=10)

    def confirm_selection(self) -> None:
        """ Callback function for when the user confirms the selection.
        """
        selected_labels = [self.user.labels[idx] for idx in self.listbox.curselection()]
        self.on_confirm(selected_labels)
        self.destroy()

    def center_window(self, width:int, height:int) -> None:
        """ Centers the window on the screen.

        Args:
            width (int): Window width.
            height (int): Height width.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        _x = int((screen_width / 2) - (width / 2))
        _y = int((screen_height / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{_x}+{_y}')

    def on_window_close(self) -> None:
        """ Callback function for when the window is closed.
        """
        if self.controller.label_filter_page_window is self:
            self.controller.label_filter_page_window = None
        self.destroy()
