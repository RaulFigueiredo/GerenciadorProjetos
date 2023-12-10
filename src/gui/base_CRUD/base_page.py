import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BasePage(tk.Frame):
    def __init__(self, master, home, manager, item):
        super().__init__(master)
        self.home = home
        self.manager = manager
        self.item = item

    def get_buttons(self,row=7):
        button_frame = tk.Frame(self)
        button_frame.grid(row=row, column=0, sticky="ew", padx=10, pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        # Botão Voltar no canto esquerdo do Frame
        back_button = ttk.Button(button_frame, text="Voltar", command=self.close_window)
        back_button.grid(row=0, column=0, sticky="w")

        # Botão Excluir no centro do Frame
        delete_button = ttk.Button(button_frame, text="Excluir", command=self.confirm_delete)
        delete_button.grid(row=0, column=1)

        # Botão Editar no canto direito do Frame
        update_button = ttk.Button(
            button_frame,
            text="Editar",
            command=lambda: self.manager.open_update_page(self.item)
        )
        update_button.grid(row=0, column=2, sticky="e")

        # Nova frame para os botões Concluir e Desatualizar
        conclusion_frame = tk.Frame(self)
        conclusion_frame.grid(row=row+1, column=0, sticky="ew", padx=10, pady=10)
        conclusion_frame.grid_columnconfigure(0, weight=1)
        conclusion_frame.grid_columnconfigure(1, weight=1)

        # Botão Desatualizar ao lado esquerdo do botão Concluir
        undo_update_button = ttk.Button(conclusion_frame, text="Desfazer", command=self.undo_update)
        undo_update_button.grid(row=0, column=0)

        # Botão Concluir ao lado direito do botão Desatualizar
        if self.item.status:
            unconclusion_button = ttk.Button(conclusion_frame, text="Reativar", command=self.unconclusion)
            unconclusion_button.grid(row=0, column=1)
        else:
            conclusion_button = ttk.Button(conclusion_frame, text="Concluir", command=self.conclusion)
            conclusion_button.grid(row=0, column=1)

    def confirm_delete(self):
        response = messagebox.askyesno("Confirmar Exclusão",
                                       "Tem certeza de que deseja excluir este item?")
        if response:
            self.delete()  
            self.close_window()  

    def delete(self):
        self.item.delete()
        self.manager.refresh_parent_page()

    def conclusion(self):
        self.item.conclusion()
        self.manager.refresh_parent_page()
        self.close_window()

    def unconclusion(self):
        self.item.unconclusion()
        self.manager.refresh_parent_page()
        self.close_window()

    def close_window(self):
        self.master.destroy()

    def undo_update(self):
        if self.item.has_memento():
            self.item.restore_from_memento()
            self.manager.refrash_page()
            messagebox.showinfo("Sucesso", "Atualização desfeita com sucesso")
        else:
            messagebox.showerror("Erro", "Não há atualizações para desfazer")

    def on_double_click(self): ...

    def create_widgets(self): ...