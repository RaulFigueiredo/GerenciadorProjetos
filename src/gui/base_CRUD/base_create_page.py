import tkinter as tk

class BaseCreatePage(tk.Frame):
    def __init__(self, master, mediator, parent):
        super().__init__(master)
        self.mediator = mediator
        self.parent = parent

    def get_buttons(self):
        # Criacao de um frame adicional para os botoes
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botao de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botao para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=self.close_window)
        close_button.grid(row=0, column=0, padx=5)

    def submit(self):
        data = self.prepare_data()
        self.mediator.create(data)
        self.close_window()

    def close_window(self):
        self.master.destroy()

    def create_widgets(self): ...
    
    def prepare_data(self): ... 
