from tkinter import messagebox
import tkinter as tk

class LabelFilterPage(tk.Toplevel):
    def __init__(self, master, user, controller, on_confirm):
        if hasattr(controller, 'label_filter_page_window') and controller.label_filter_page_window:
            controller.label_filter_page_window.destroy()

        super().__init__(master)
        self.user = user
        self.controller = controller
        self.on_confirm = on_confirm

        self.title("Filtrar por Etiquetas")
        self.configure(bg="white")
        self.create_widgets()
        self.center_window(320, 320)

        controller.label_filter_page_window = self

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)
    
    def create_widgets(self):
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(padx=10, pady=10)

        label_title = tk.Label(main_frame, text="Filtrar por etiquetas", font=("Arial", 16), bg="white")
        label_title.pack(pady=(0, 5))

        label_subtitle = tk.Label(main_frame, text="Selecione as etiquetas para filtrar", font=("Arial", 12), bg="white")
        label_subtitle.pack(pady=(0, 10))

        self.listbox = tk.Listbox(main_frame, selectmode='multiple')
        self.listbox.pack(fill="both", expand=True)

        for label in self.user.labels:
            self.listbox.insert(tk.END, label.name)

        confirm_button = tk.Button(main_frame, text="Confirmar Seleção", command=self.confirm_selection)
        confirm_button.pack(pady=10)

    def confirm_selection(self):
        selected_labels = [self.user.labels[idx] for idx in self.listbox.curselection()]
        self.on_confirm(selected_labels)
        self.destroy()
    
    def center_window(self, width:int, height:int) -> None:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{x}+{y}')

    def on_window_close(self):
        if self.controller.label_filter_page_window is self:
            self.controller.label_filter_page_window = None
        self.destroy()