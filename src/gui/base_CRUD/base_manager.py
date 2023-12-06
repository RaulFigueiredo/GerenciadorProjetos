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

    def refresh_parent_page(self): ...

    def open_page(self, item, parent = None): ...

    def open_create_page(self, parent = None): ...

    def open_update_page(self, item, parent = None): ...


