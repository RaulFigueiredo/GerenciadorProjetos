import tkinter as tk

class BaseUpdatePage(tk.Frame):
    def __init__(self, master, manager, mediator, item,parent):
        super().__init__(master)
        self.manager = manager
        self.mediator = mediator
        self.item = item
        self.parent = parent

    def get_buttons(self):
        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        close_button = tk.Button(button_frame, text="Sair", command=lambda: self.manager.open_page(self.item,self.parent))
        close_button.grid(row=0, column=0, padx=5)


    def submit(self):
        data = self.prepare_data()
        self.mediator.update(data)
        self.manager.open_page(self.item,self.parent)

    def create_widgets(self): ...

    def prepare_data(self): ...