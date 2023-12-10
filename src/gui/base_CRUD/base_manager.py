from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists

class BaseDisplayManager:
    def __init__(self, home):
        self.home = home
        self.top_window = None

    def submit_item(self, item_type, data):
        try:
            ItemFactory.create_item(item_type, **data)
            self.refresh_parent_page()
            self.top_window.destroy()
            print("Submetido:", data)
        except ItemNameBlank as e:
            if not messagebox.showerror("Erro", e):
                return
        except ItemNameAlreadyExists as e:
            if not messagebox.showerror("Erro", e):
                return

    def update_item(self, data):
        self.item.update(**data)
        self.refresh_parent_page()
        print("Atualizado:", data)

    def resize_page(self):
        # Atualiza a janela para calcular o tamanho necessário com base no conteúdo
        self.top_window.update_idletasks()
        self.top_window.minsize(self.top_window.winfo_width(), self.top_window.winfo_height())

        # Centraliza a janela na tela
        width = self.top_window.winfo_width() 
        height = self.top_window.winfo_height()
        x = (self.top_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top_window.winfo_screenheight() // 2) - (height // 2)
        self.top_window.geometry(f'{width}x{height}+{x}+{y}')

        # Faz a janela abrir na hora certa
        self.top_window.update_idletasks()
        self.top_window.deiconify()

    def refresh_parent_page(self): ...

    def open_page(self, item, parent = None): ...

    def open_create_page(self, parent = None): ...

    def open_update_page(self, item, parent = None): ...

    def refrash_page(self): ...
