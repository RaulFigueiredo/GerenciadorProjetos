import tkinter as tk
from tkinter import ttk


class AddLabelDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Adicionar Etiqueta")

        tk.Label(self.top, text="Nome da Etiqueta:").pack(padx=10, pady=5)
        self.nome_entry = tk.Entry(self.top)
        self.nome_entry.pack(padx=10, pady=5)

        tk.Label(self.top, text="Cor da Etiqueta:").pack(padx=10, pady=5)
        self.cor_combobox = ttk.Combobox(self.top, values=["blue", "green", "red"], state="readonly")
        self.cor_combobox.pack(padx=10, pady=5)

        self.btn_confirmar = tk.Button(self.top, text="Confirmar", command=self.on_confirm)
        self.btn_confirmar.pack(pady=10)

        self.resultado = None

    def on_confirm(self):
        nome = self.nome_entry.get()
        cor = self.cor_combobox.get()
        self.resultado = (nome, cor)
        self.top.destroy()

    def show(self):
        self.top.grab_set()
        self.top.wait_window()
        return self.resultado
