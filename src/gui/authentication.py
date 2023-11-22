from src.logic.authentication.authentication import LoginLogic, RegisterLogic
from src.gui.homepage import HomePage
import tkinter as tk

class Login(tk.Frame):
    def __init__(self, parent, on_login, on_show_register):
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

    def _on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.on_login(username, password)

class Register(tk.Frame):
    def __init__(self, parent, on_register):
        super().__init__(parent, bg='#EAEAEA')

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
            command=lambda: on_register(
                self.username_entry.get(), 
                self.password_entry.get(), 
                self.email_entry.get()
            ),
            bg='#7FFF7F', 
            font=('Arial', 18)
        )
        register_button.pack(pady=10)
        
class Authentication:
    def __init__(self, parent):
        self.parent = parent
        self.login_frame = Login(parent, self.login_user, self.show_register)
        self.register_frame = Register(parent, self.register_user)
        self.homepage_frame = HomePage(parent)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.show_login()

    def login_user(self, username, password):
        if LoginLogic.login(username, password):
            self.show_homepage()
        else:
            print("Login failed")

    def register_user(self, username, password, email):
        if RegisterLogic.register(username, password, email):
            self.show_homepage()
        else:
            print("Registration failed")

    def show_login(self):
        self.register_frame.grid_forget()
        self.homepage_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky='nsew')

    def show_register(self):
        self.login_frame.grid_forget()
        self.homepage_frame.grid_forget()
        self.register_frame.grid(row=0, column=0, sticky='nsew')

    def show_homepage(self):
        self.login_frame.grid_forget()
        self.register_frame.grid_forget()
        self.homepage_frame.grid(row=0, column=0, sticky='nsew')

    def navigate(self, destination):
        print(f"Navigating to {destination}")