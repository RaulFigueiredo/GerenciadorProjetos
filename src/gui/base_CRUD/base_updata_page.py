import tkinter as tk

class BaseUpdatePage(tk.Frame):
    def __init__(self, master, mediator, controller, item):
        super().__init__(master)
        self.mediator = mediator
        self.controler = controller
        self.item = item

    def get_buttons(self):
        # Criação de um frame adicional para os botões
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10)

        # Botão de envio
        submit_button = tk.Button(button_frame, text="Salvar", command=self.submit)
        submit_button.grid(row=0, column=1, padx=5)

        # Botão para fechar a janela
        #close_button = tk.Button(button_frame, text="Sair", command=lambda: self.controler.task_manager.open_page(self.task))
        close_button = tk.Button(button_frame, text="Sair",  command=self.master.destroy)
        close_button.grid(row=0, column=0, padx=5)


    def submit(self):
        data = self.prepare_data()
        self.mediator.submit(data)
        self.master.destroy()

    def create_widgets(self): ...

    def prepare_data(self): ...