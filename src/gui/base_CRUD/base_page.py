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

        back_button = ttk.Button(self, text="Voltar", command=self.close_window)
        back_button.grid(row=row, column=0, sticky="w", padx=(10, 5), pady=10)

        delete_button = ttk.Button(self, text="Excluir", command=self.confirm_delete)
        delete_button.grid(row=row, column=0, padx=(5, 5), pady=10)
        
        update_button = ttk.Button(
                                self,
                                text="Editar",
                                command=lambda: self.manager.open_update_page(self.item)
                            )
        update_button.grid(row=row, column=0, sticky="e", padx=(5, 10), pady=10)

        if self.item.status:
            unconclusion_button = ttk.Button(self, text="Reativar", command=self.unconclusion)
            unconclusion_button.grid(row=row+1, column=0, pady=10)
        else:
            conclusion_button = ttk.Button(self, text="Concluir", command=self.conclusion)
            conclusion_button.grid(row=row+1, column=0, pady=10)

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

    def on_double_click(self): ...

    def create_widgets(self): ...