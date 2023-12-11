"""
Module Name: Project Filter Page

Description:
This module presents a window for filtering projects. It creates a graphical interface
to allow users to select projects for filtering based on specific criteria.

- Imports the 'tkinter' library.
- Defines the 'ProjectFilterPage' class for managing the project filtering window.

- Initializes the window with the necessary parameters such as the master window, current user,
  controller, and a callback function for confirmation.
- Provides functionality for users to select projects and confirm their selection.

Methods:
    - __init__(master, user, controller, on_confirm): Initializes the project filter window.
    - create_widgets(): Creates widgets for the page (labels, listbox, and confirm button).
    - confirm_selection(): Confirms the selection of projects and closes the window.
    - center_window(width, height): Centers the window on the screen based on width and height.
    - on_window_close(): Destroys the window and sets the controller's window to None on close.
"""

import tkinter as tk

class ProjectFilterPage(tk.Toplevel):
    """ Class for the project filter window.

    Args:
        tk (_type_): _description_
    """
    def __init__(self, master: tk, user: callable, controller: tk, on_confirm: callable) -> None:
        """ Creates a new window for filtering projects.

        Args:
            master (_type_): Master window.
            user (_type_): Current user.
            controller (_type_): Controller for the page.
            on_confirm (_type_): Callback function for when the user confirms the selection.
        """
        if hasattr(controller, 'project_filter_page_window')\
              and controller.project_filter_page_window:
            controller.project_filter_page_window.destroy()

        super().__init__(master)
        self.user = user
        self.controller = controller
        self.on_confirm = on_confirm

        self.title("Filtrar Projetos")
        self.configure(bg="white")
        self.create_widgets()
        self.center_window(320, 320)

        controller.project_filter_page_window = self

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def create_widgets(self) -> None:
        """ Creates the widgets for the page.
        """
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(padx=10, pady=10)

        label_title = tk.Label(main_frame, text="Filtrar por projetos",\
                     font=("Arial", 16), bg="white")
        label_title.pack(pady=(0, 5))

        label_subtitle = tk.Label(main_frame, text="Selecione os projetos para filtrar",\
                     font=("Arial", 12), bg="white")
        label_subtitle.pack(pady=(0, 10))

        self.listbox = tk.Listbox(main_frame, selectmode='multiple')
        self.listbox.pack(fill="both", expand=True)

        for project in self.user.projects:
            self.listbox.insert(tk.END, project.name)

        confirm_button = tk.Button(main_frame, text="Confirmar Seleção",\
                     command=self.confirm_selection)
        confirm_button.pack(pady=10)

    def confirm_selection(self) -> None:
        """ Confirms the selection of projects and closes the window.
        """
        selected_projects = [self.user.projects[idx] for idx in self.listbox.curselection()]
        self.on_confirm(selected_projects)
        self.destroy()

    def center_window(self, width:int, height:int) -> None:
        """ Centers the window on the screen.

        Args:
            width (int): Window width.
            height (int): Window height.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        _x = int((screen_width / 2) - (width / 2))
        _y = int((screen_height / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{_x}+{_y}')

    def on_window_close(self) -> None:
        """ Destroys the window and sets the controller's window to None.
        """
        if hasattr(self.controller, 'project_filter_page_window'):
            self.controller.project_filter_page_window = None

        self.destroy()
