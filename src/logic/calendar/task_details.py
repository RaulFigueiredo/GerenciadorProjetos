import tkinter as tk

class TaskDetails:
    def __init__(self, details_frame, details_text, details_scroll, close_button):
        self.details_frame = details_frame
        self.details_text = details_text
        self.details_scroll = details_scroll
        self.close_button = close_button
        self.close_button.configure(command=self.close_details)


    def show_task_details(self, task_info):
        self.details_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.clear_details()
        if task_info:
            self.details_text.config(state='normal')
            for task in task_info:
                self.details_text.insert('end', f"Projeto: {task[4]}\n")
                self.details_text.insert('end', f"Tarefa: {task[0]}\n")
                self.details_text.insert('end', f"Descrição: {task[3]}\n\n")
            self.details_text.config(state='disabled')
            
            self.details_text.grid(row=0, column=0, sticky='nsew')
            self.details_scroll.grid(row=0, column=1, sticky='ns')

        closeButton = tk.Button(self.details_frame, text="Fechar", command=self.close_details)
        closeButton.grid(row=1, column=0, columnspan=2, sticky='ne') 
            

    def clear_details(self):
        self.details_text.config(state='normal')
        self.details_text.delete('1.0', tk.END)
        self.details_text.config(state='disabled')

    def close_details(self):
        self.details_frame.grid_remove()