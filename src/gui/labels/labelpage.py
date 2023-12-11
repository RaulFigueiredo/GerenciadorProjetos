"""
Module Name: LabelManager Module

Description:
This module contains a class, `LabelManager`, which is a Tkinter Frame
class for a label management interface. It provides functionalities for
users to add, edit, and remove labels associated with a user.

Classes:
- LabelManager: Manages the interface for label addition, editing, and removal.

Attributes:
- parent (tk.Widget): The parent widget for this frame.
- controller: The controller managing this frame.
- user: The user associated with this frame.

Dependencies:
- tkinter: Library for GUI elements.
- tkinter.messagebox: For displaying warning messages in the Tkinter interface.
- tkinter.ttk: For themed Tkinter widgets.
- src.gui.labels.label_edit: EditLabelDialog class from the 'label_edit' module.
- src.gui.labels.label_create: AddLabelDialog class from the 'label_create' module.
- src: ItemFactory from the 'src' module.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from src.gui.labels.label_edit import EditLabelDialog
from src.gui.labels.label_create import AddLabelDialog
from src import ItemFactory

class LabelManager(tk.Toplevel):
    """
    A Tkinter Frame class for a label management interface.

    Allows users to add, edit, and remove labels associated with a user.

    Attributes:
        parent (tk.Widget): The parent widget for this frame.
        controller: The controller managing this frame.
    """

    def __init__(self, parent: tk.Widget, controller, user) -> None:
        """
        Initializes a new instance of LabelManager.

        Parameters:
            parent (tk.Widget): The parent widget for this frame.
            controller: The controller managing this frame.
            user: The user associated with this frame.
        """
        if hasattr(controller, 'label_page_window') and controller.label_page_window:
            controller.label_page_window.destroy()

        super().__init__(parent)
        self.controller = controller
        self.user = user
        self.title("Gerenciador de Etiquetas")
        self.geometry("425x380+400+50")
        self.create_widgets()
        self.center_window(425, 380)

        self.controller.label_page_window = self

    def create_widgets(self) -> None:
        """ Creates and arranges the widgets for this frame.
        """
        self.button_style = ttk.Style()
        self.button_style.configure('LabelManager.TButton', font=('Arial', 10), padding=5)

        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)

        label_title = tk.Label(main_frame, text="Etiquetas Disponíveis", font=('Arial', 20))
        label_title.grid(row=0, column=0, padx=10, pady=(10, 0))

        self.label_list = tk.Listbox(main_frame, height=10, width=50)
        self.label_list.grid(row=1, column=0, padx=10, pady=10)

        self.add_button = ttk.Button(main_frame, text="Adicionar Etiqueta",\
                     style='LabelManager.TButton', command=self.add_label)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.edit_button = ttk.Button(main_frame, text="Editar Etiqueta",\
                     style='LabelManager.TButton', command=self.edit_label)
        self.edit_button.grid(row=3, column=0, padx=5, pady=5)

        self.remove_button = ttk.Button(main_frame, text="Remover Etiqueta",\
                     style='LabelManager.TButton', command=self.remove_label)
        self.remove_button.grid(row=4, column=0, padx=5, pady=5)

        self.update_label_list()


    # pylint: disable=pointless-string-statement
    """
    - step 1
    def edit_label(self):
        pass

    - step 2
    def edit_label(self):
        selected = self.label_list.curselection()

    - step 3
    def edit_label(self):
        selected = self.label_list.curselection()
        if selected:
            pass

    - step 4
    def edit_label(self):
        selected = self.label_list.curselection()
        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Cor:")[0]
        else:
            messagebox.showinfo("Seleção", "Selecione uma etiqueta para editar.")

    - step 5
    def edit_label(self):
        selected = self.label_list.curselection()
        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Cor:")[0]
            label_to_edit = next((label for label in self.user.labels if label.name == label_name), None)
        else:
            messagebox.showinfo("Seleção", "Selecione uma etiqueta para editar.")

    - step 6
    def edit_label(self):
        selected = self.label_list.curselection()
        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Cor:")[0]
            label_to_edit = next((label for label in self.user.labels if label.name == label_name), None)
            if label_to_edit:
                dialog = EditLabelDialog(self.controller, label_to_edit.name, label_to_edit.color)
                dialog.show()
        else:
            messagebox.showinfo("Seleção", "Selecione uma etiqueta para editar.")

    - step 7
    def edit_label(self):
        selected = self.label_list.curselection()
        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Cor:")[0]
            label_to_edit = next((label for label in self.user.labels if label.name == label_name), None)
            if label_to_edit:
                dialog = EditLabelDialog(self.controller, label_to_edit.name, label_to_edit.color)
                result = dialog.show()
                if result:
                    new_name, new_color = result
                    label_to_edit.name = new_name
                    label_to_edit.color = new_color
                    self.update_label_list()
        else:
            messagebox.showinfo("Seleção", "Selecione uma etiqueta para editar.")
    """

    def edit_label(self) -> None:
        """ Edits the selected label after user interaction.
        """
        selected = self.label_list.curselection()

        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Color:")[0]

            label_to_edit = next((label for label\
                     in self.user.labels if label.name == label_name), None)

            if label_to_edit:
                existing_label_names = [label.name for\
                         label in self.user.labels if label.name != label_name]
                dialog = EditLabelDialog(self.controller,
                         label_to_edit.name, label_to_edit.color, existing_label_names)
                result = dialog.show()

                if result:
                    new_name, new_color = result
                    label_to_edit.update(name=new_name, color=new_color)

                    self.update_label_list()
        else:
            messagebox.showinfo("Selecionar", "Por favor, selecione uma etiqueta para editar")


    def add_label(self):
        """
        Adds a new label after user interaction.
        """
        dialog = AddLabelDialog(self.controller)
        result = dialog.show()

        if result:
            name, color = result

            if not name.strip():
                messagebox.showwarning("Aviso", "O campo de nome não pode estar vazio")
                return

            if any(label.name == name for label in self.user.labels):
                messagebox.showwarning("Aviso", "Uma etiqueta com esse nome já existe")
                return

            ItemFactory.create_item(item_type='label', user=self.user, name=name, color=color)
            self.update_label_list()

    def remove_label(self):
        """ Removes the selected label after user interaction.
        """
        selected = self.label_list.curselection()

        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Color:")[0]

            label_to_remove = next((label for label in\
                     self.user.labels if label.name == label_name), None)

            if label_to_remove:
                # self.user.remove_label(label_to_remove)
                label_to_remove.delete()
                self.update_label_list()
            else:
                messagebox.showinfo("Erro", "Etiqueta não encontrada")
        else:
            messagebox.showinfo("Seleção", "Por favor, selecione uma etiqueta para remover")

    # pylint: disable=pointless-string-statement
    """
    - step 1
    def update_label_list(self):
        pass

    - step 2
    def update_label_list(self):
        self.label_list.delete(0, tk.END)

    - step 3
    def update_label_list(self):
        self.label_list.delete(0, tk.END)
        for label in self.user.labels:
            pass

    - step 4
    def update_label_list(self):
        self.label_list.delete(0, tk.END)
        for label in self.user.labels:
            label_text = f"{label.name} (Cor: {label.color})"
            pass

    - step 5
    def update_label_list(self):
        self.label_list.delete(0, tk.END)
        for label in self.user.labels:
            label_text = f"{label.name} (Cor: {label.color})"
            self.label_list.insert(tk.END, label_text)
    """
    def update_label_list(self) -> None:
        """
        Updates the list of labels displayed in the interface.
        """
        self.label_list.delete(0, tk.END)
        for label in self.user.labels:
            label_text = f"{label.name} (Color: {label.color})"
            self.label_list.insert(tk.END, label_text)

    def center_window(self, width:int, height:int) -> None:
        """
        Centers the window on the screen.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
