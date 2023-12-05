from tkinter import messagebox

class FormMediator:
    def __init__(self, submit_action):
        self.submit_action = submit_action

    def submit(self, data): 
        # se pah vira update(self, sender,data):
        # quando eu fizer o base_managers.py 
        self.submit_action(data)
    
