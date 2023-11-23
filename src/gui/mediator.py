from tkinter import messagebox

class FormMediator:
    def __init__(self, submit_action):
        self.submit_action = submit_action
        self.fields = {}

    def add_field(self, field_name, field):
        self.fields[field_name] = field

    def notify(self, sender, event, data=None):
        if event == "update" and data is not None:
            if self.validate_fields(data):
                self.submit_action(data)

        elif event == "submit" and data is not None:
            if self.validate_fields(data):
                self.submit_action(data)

    def submit(self):
        data = {field_name: field.get_value() for field_name, field in self.fields.items()}
        if self.validate_fields(data):
            self.submit_action(data)
            

    def validate_fields(self, data):
        # Exemplo de validação: verificar se o campo Nome não está vazio
        name = data.get("name")
        if not name or not name.strip():
            messagebox.showerror("Erro", "O campo 'Nome' é obrigatório.")
            return False
        return True
