import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EditLabelDialog:
    def __init__(self, parent, nome_atual, cor_atual):
        self.top = tk.Toplevel(parent)
        self.top.title("Editar Etiqueta")
        self.top.geometry("425x550+400+50")  


        self.top.configure(bg='lightgray')
        frame = tk.Frame(self.top, bg='lightgray', pady=5)
        frame.pack(padx=10, pady=10, fill=tk.X)

        tk.Label(frame, text="Nome da Etiqueta:", bg='lightgray').pack(padx=10, pady=5)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.insert(0, nome_atual)
        self.nome_entry.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(frame, text="Cor da Etiqueta:", bg='lightgray').pack(padx=10, pady=5)
        self.cor_combobox = ttk.Combobox(frame, values=["bluee", "green", "red"], state="readonly")
        self.cor_combobox.set(cor_atual)
        self.cor_combobox.pack(padx=10, pady=5, fill=tk.X)

        self.btn_confirmar = tk.Button(frame, text="Confirmar", command=self.on_confirm)
        self.btn_confirmar.pack(pady=10)

        self.resultado = None

    def on_confirm(self):
        nome = self.nome_entry.get().strip()
        cor = self.cor_combobox.get()

        if not nome:
            messagebox.showwarning("Aviso", "O nome da etiqueta não pode estar vazio.", parent=self.top)
            return

        if not cor:
            messagebox.showwarning("Aviso", "Por favor, selecione uma cor.", parent=self.top)
            return

        self.resultado = (nome, cor)
        self.top.destroy()

    def show(self):
        self.top.grab_set()
        self.top.wait_window()
        return self.resultado