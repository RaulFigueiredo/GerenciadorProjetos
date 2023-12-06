from tkinter import messagebox

class FormMediator:
    def __init__(self, submit_action):
        self.submit_action = submit_action

    def create(self, data): 
        print(data)
        item_type = data['item_type']
        del data['item_type']

        self.submit_action(item_type, data)

    def update(self, data): 
        # se pah vira update(self, sender,data):
        # quando eu fizer o base_managers.py 
        self.submit_action(data)
