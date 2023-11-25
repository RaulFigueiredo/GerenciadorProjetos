import tkinter as tk
from src.gui.label_edit import EditLabelDialog
from src.gui.label_create import AddLabelDialog
from src import User, Label
from tkinter import messagebox
from tkinter import ttk


class LabelPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.controller.title("Gerenciador de Etiquetas")
        self.controller.geometry("425x550+400+50")  # Define o tamanho e a posição da janela

        self.user = User(name='John Doe')

        # Configurações de estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', font=('Arial', 10), padding=5)
        Label(self.user, name='Trabalho', color='blue')
        Label(self.user, name='Estudos', color='green')
        Label(self.user, name='Lazer', color='red')


        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.label_list = tk.Listbox(main_frame, height=10, width=50)
        self.label_list.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        self.add_button = ttk.Button(main_frame, text="Adicionar Etiqueta", command=self.add_label)
        self.add_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.edit_button = ttk.Button(main_frame, text="Editar Etiqueta", command=self.edit_label)
        self.edit_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.remove_button = ttk.Button(main_frame, text="Remover Etiqueta", command=self.remove_label)
        self.remove_button.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
        
       
        self.back_button = ttk.Button(main_frame, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        self.back_button.grid(row=4, column=0, padx=5, pady=5, sticky='ew')
        
        self.update_label_list()

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

    def add_label(self):
        dialog = AddLabelDialog(self.controller)
        result = dialog.show()

        if result:
            name, color = result

            if not name.strip():
                messagebox.showwarning("Aviso", "O campo de nome não pode estar em branco.")
                return

            if any(label.name == name for label in self.user.labels):
                messagebox.showwarning("Aviso", "Já existe uma etiqueta com este nome.")
                return

            
            Label(self.user, name=name, color=color)
            self.update_label_list()

    def remove_label(self):
        selected = self.label_list.curselection()

        if selected:
            full_label_text = self.label_list.get(selected[0])
            label_name = full_label_text.split(" (Cor:")[0]

       
            label_to_remove = next((label for label in self.user.labels if label.name == label_name), None)

            if label_to_remove:
                self.user.remove_label(label_to_remove) 
                self.update_label_list()
            else:
                messagebox.showinfo("Erro", "Etiqueta não encontrada.")
        else:
            messagebox.showinfo("Seleção", "Selecione uma etiqueta para remover.")

    def update_label_list(self):
        self.label_list.delete(0, tk.END)
        for label in self.user.labels:
            label_text = f"{label.name} (Cor: {label.color})"
            self.label_list.insert(tk.END, label_text)

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        
        self.go_to_label_page_button = ttk.Button(self, text="Gerenciar Etiquetas",
                                                  command=lambda: controller.show_frame("LabelPage"))
        self.go_to_label_page_button.pack(pady=20)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("300x200")

        self.frames = {}

        for F in (StartPage, LabelPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


app = MainApp()
app.mainloop()