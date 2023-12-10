from src.logic.authentication.authentication import LoginLogic, RegisterLogic
from src.gui.homepage import HomePage
import tkinter as tk
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.users.user import User
from src.logic.orms.orm import UserORM, ProjectORM, TaskORM

class Login(tk.Frame):
    """
    A tkinter Frame for the login interface.

    Attributes:
        parent (tk.Widget): The parent widget.
        on_login (function): A callback function invoked when the login button is clicked.
        on_show_register (function): A callback function to switch to the registration interface.
    """

    def __init__(self, parent, on_login, on_show_register):
        """
        Initialize the login interface.

        Parameters:
            parent (tk.Widget): The parent widget.
            on_login (function): A callback function invoked when the login button is clicked.
            on_show_register (function): A callback function to switch to the registration interface.
        """

        super().__init__(parent, bg='#EAEAEA')
        self.on_login = on_login
        self.on_show_register = on_show_register

        tk.Label(self, text="Login", font=('Arial', 24), bg='#ADD8E6').pack(pady=20)
        tk.Label(self, text="Username:", font=('Arial', 18), bg='#EAEAEA').pack(pady=10)
        self.username_entry = tk.Entry(self, font=('Arial', 18), width=30)
        self.username_entry.pack(pady=10)
        tk.Label(self, text="Password:", font=('Arial', 18), bg='#EAEAEA').pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=('Arial', 18), width=30)
        self.password_entry.pack(pady=10)

        tk.Button(self, text="Login", command=self._on_login, font=('Arial', 18), bg='#7FFF7F', width=20).pack(pady=20)
        tk.Button(self, text="Register", command=self.on_show_register, font=('Arial', 18), bg='#FF7F7F', width=20).pack(pady=10)

        self.status_label = tk.Label(self, text="", font=('Arial', 12), bg='#EAEAEA')
        self.status_label.pack()

    def _on_login(self):
        """
        Internal method to handle the login process when the login button is clicked.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.update_status("Logging in...", "blue")
        self.update_idletasks()  # Force GUI update
        self.after(100, lambda: self.on_login(username, password))

    def update_status(self, message, color="red"):
        """
        Update the status message displayed on the login interface.

        Parameters:
            message (str): The message to display.
            color (str): The color of the message.
        """
        self.status_label.config(text=message, fg=color)

class Register(tk.Frame):
    """
    A tkinter Frame for the user registration interface.

    Attributes:
        parent (tk.Widget): The parent widget.
        on_register (function): A callback function invoked when the register button is clicked.
    """

    def __init__(self, parent, on_register):
        """
        Initialize the registration interface.

        Parameters:
            parent (tk.Widget): The parent widget.
            on_register (function): A callback function invoked when the register button is clicked.
        """

        super().__init__(parent, bg='#EAEAEA')
        self.on_register = on_register

        tk.Label(self, text="Register", font=('Arial', 24), bg='#B19CD9').pack(pady=10)
        tk.Label(self, text="Username:", font=('Arial', 18), bg='#EAEAEA').pack()
        self.username_entry = tk.Entry(self, font=('Arial', 18))
        self.username_entry.pack()
        tk.Label(self, text="Password:", font=('Arial', 18), bg='#EAEAEA').pack()
        self.password_entry = tk.Entry(self, show="*", font=('Arial', 18))
        self.password_entry.pack()
        tk.Label(self, text="Email:", font=('Arial', 18), bg='#EAEAEA').pack()
        self.email_entry = tk.Entry(self, font=('Arial', 18))
        self.email_entry.pack()

        register_button = tk.Button(
            self, 
            text="Register", 
            command=self._on_register,
            bg='#7FFF7F', 
            font=('Arial', 18)
        )
        register_button.pack(pady=10)

        self.status_label = tk.Label(self, text="", font=('Arial', 12), bg='#EAEAEA')
        self.status_label.pack()

    def _on_register(self):
        """
        Internal method to handle the registration process when the register button is clicked.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        self.update_status("Registering...", "blue")
        self.update_idletasks()
        self.after(100, lambda: self.on_register(username, password, email))

    def update_status(self, message, color="red"):
        """
        Update the status message displayed on the registration interface.

        Parameters:
            message (str): The message to display.
            color (str): The color of the message.
        """
        self.status_label.config(text=message, fg=color)

class Authentication:
    """
    A class to manage the authentication process including login, registration, and navigation to the homepage.

    Attributes:
        parent (tk.Widget): The parent widget.
    """

    def __init__(self, parent):
        """
        Initialize the Authentication class.

        Parameters:
            parent (tk.Widget): The parent widget.
        """

        self.parent = parent
        self.login_frame = Login(parent, self.login_user, self.show_register)
        self.register_frame = Register(parent, self.register_user)
        self.user = None
        self.homepage_frame = None

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.show_login()
    #pylint: disable=pointless-string-statement
    """
    - step 1
    def login_user(self, username, password):
        pass

    - step 2
    def login_user(self, username, password):
        user = LoginLogic.login(username, password)

    - step 3
    def login_user(self, username, password):
        user = LoginLogic.login(username, password)
        if user:
            pass
        else:
            pass

    - step 4
    def login_user(self, username, password):
        user = LoginLogic.login(username, password)
        if user:
            self.user = user
        else:
            self.login_frame.update_status("Login failed")

    - step 5
    def login_user(self, username, password):
        user = LoginLogic.login(username, password)
        if user:
            self.user = user
            self.show_homepage()
            return True
        self.login_frame.update_status("Login failed")
        return False
    """
    def login_user(self, username, password):
        """
        Attempt to log in a user with the given username and password.

        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        user = LoginLogic.login(username, password)
        if user:
            self.user = user
            self.show_homepage()
            return True
        self.login_frame.update_status("Login failed")
        return False
    #pylint: disable=pointless-string-statement
    """
    - step 1
    def register_user(self, username, password, email):
        pass

    - step 2
    def register_user(self, username, password, email):
        user = RegisterLogic.register(username, password, email)

    - step 3
    def register_user(self, username, password, email):
        user = RegisterLogic.register(username, password, email)
        if user:
            pass

    - step 4
    def register_user(self, username, password, email):
        user = RegisterLogic.register(username, password, email)
        if user:
            self.user = user
        else:
            self.register_frame.update_status("Registration failed")

    - step 5
    def register_user(self, username, password, email):
        user = RegisterLogic.register(username, password, email)
        if user:
            self.user = user
            self.show_homepage()
            return True
        self.register_frame.update_status("Registration failed")
        return False
    """
    def register_user(self, username, password, email):
        """
        Attempt to register a new user with the given username, password, and email.

        Parameters:
            username (str): The username for the new account.
            password (str): The password for the new account.
            email (str): The email for the new account.
        """
        user = RegisterLogic.register(username, password, email)
        if user:
            self.user = user
            self.show_homepage()
            return True
        self.register_frame.update_status("Registration failed")
    def show_login(self):
        """
        Display the login interface.
        """

        self.register_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky='nsew')

    def show_register(self):
        """
        Display the registration interface.
        """

        self.login_frame.grid_forget()
        self.register_frame.grid(row=0, column=0, sticky='nsew')

    def show_homepage(self):
        """
        Display the homepage interface for the logged-in user.
        """

        self.login_frame.grid_forget()
        self.register_frame.grid_forget()
        self.homepage_frame = HomePage(self.parent, self.user)
        self.homepage_frame.grid(row=0, column=0, sticky='nsew')

    def navigate(self, destination):
        """
        Navigate to a specified destination in the application.

        Parameters:
            destination (str): The destination to navigate to.
        """

        print(f"Navigating to {destination}")