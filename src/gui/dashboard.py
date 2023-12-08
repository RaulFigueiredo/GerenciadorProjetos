import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.logic.dashboard.plot import Plot


class GridFrame(tk.Frame):
    def __init__(self, parent, row, col, rowspan=1, colspan=1):
        super().__init__(parent)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#000000")
        self.grid_configure(sticky="nsew")


class GridLabel(tk.Label):
    def __init__(self, parent, row, col, text, rowspan=1, colspan=1):
        super().__init__(parent, text=text)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#ffffff", font=("Monospace", 12, "bold"), fg="#ffffff")
        self.grid_configure(sticky="ew")


class GridDropdown(ttk.Combobox):
    def __init__(self, parent, row, col, values, rowspan=1, colspan=1):
        super().__init__(parent, values=values)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.grid_configure(sticky="ew")


class GridButton(tk.Button):
    def __init__(self, parent, row, col, text, command, rowspan=1, colspan=1):
        super().__init__(parent, text=text, command=command)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)


class DashboardUtils:
    @staticmethod
    def add_plot(parent, plot, row, col, rowspan=1, colspan=1):
        canvas = FigureCanvasTkAgg(plot, master=parent)
        canvas.get_tk_widget().grid(row=row, column=col, columnspan=colspan,
                                    rowspan=rowspan, padx=5, pady=5,
                                    sticky="nsew")
        for i in range(rowspan):
            parent.grid_rowconfigure(row + i, weight=1)
        for i in range(colspan):
            parent.grid_columnconfigure(col + i, weight=1)


class DashboardPlots():
    def __init__(self):
        self.plots = []

    def __iter__(self):
        return iter(self.plots)

    def add_plot(self, plot, row, col, rowspan=1, colspan=1):
        self.plots.append({'plot': plot, 'row': row, 'col': col,
                           'rowspan': rowspan, 'colspan': colspan})


class Dashboard(tk.Frame):
    def __init__(self, parent, row, col, rowspan=1, colspan=1):
        super().__init__(parent)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#eaeaea")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_configure(padx=20, pady=20)

        cards = GridFrame(self, row=0, col=0)
        cards.config(bg="#eaeaea")
        texts = ["Tarefas\n27", "Para Hoje\n4", "Feitas\n12", "Atrasadas\n4"]
        for i in range(len(texts)):
            cards.grid_columnconfigure(i, weight=1)
            label = GridLabel(cards, 0, i, text=texts[i])
            label.config(height=4, fg="#000000")
            label.grid_configure(padx=5, pady=5)

        plots = GridFrame(self, row=1, col=0)
        plots.config(bg="#eaeaea")


        # Fake data #
        tasks = {'Feitas': 10,'Para fazer': 8,'Atrasadas': 3}
        tasks_timespan = {'até 1': 30,'1 a 2': 50,'2 a 3': 1,'3+': 40}
        next_deadlines = {'até 1': 30,'1 a 2 ': 50,'2 a 3': 30,'3+': 9}
        total_tasks = {'01-03-2023': 3,'02-03-2023': 4,'03-03-2023': 6,'04-03-2023': 7,'05-03-2023': 8,'06-03-2023': 11,'07-03-2023': 11,'08-03-2023': 11,'09-03-2023': 12,'10-03-2023': 12,'11-03-2023': 15,'12-03-2023': 18,'13-03-2023': 18,'14-03-2023': 18,'15-03-2023': 18,'16-03-2023': 20,'17-03-2023': 26,'18-03-2023': 30,'19-03-2023': 30,'20-03-2023': 30,'21-03-2023': 30,'22-03-2023': 30,'23-03-2023': 30,'24-03-2023': 30,'25-03-2023': 30,'26-03-2023': 31,'27-03-2023': 33,'28-03-2023': 33,'29-03-2023': 34,'30-03-2023': 36}
        weekday_mean = {'seg': 0.4,'ter': 1.05,'qua': 0.5,'qui': 0.7,'sex': 2,'sab': 3,'dom': 4}

        plot1 = Plot.make_donutplot(tasks, 'Tarefas')
        plot2 = Plot.make_barplot(tasks_timespan, 'Duração das Tarefas (semanas)')
        plot3 = Plot.make_pieplot(next_deadlines, 'Próximos Limites (semanas)')
        plot4 = Plot.make_areaplot(total_tasks, 'Total de Tarefas Criadas')
        plot5 = Plot.make_lineplot(weekday_mean, 'Média de Tarefas Concluídas')

        dash_plots = DashboardPlots()
        dash_plots.add_plot(plot1, 0, 0)
        dash_plots.add_plot(plot2, 0, 1)
        dash_plots.add_plot(plot3, 0, 2)
        dash_plots.add_plot(plot4, 1, 0)
        dash_plots.add_plot(plot5, 1, 1, colspan=2)

        for plot in dash_plots:
            DashboardUtils.add_plot(plots, plot['plot'], plot['row'], plot['col'], plot['rowspan'], plot['colspan'])


class Sidebar(tk.Frame):
    def __init__(self, parent, row, col, back, rowspan=1, colspan=1):
        super().__init__(parent)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#add8e6")
        self.grid_configure(sticky="nsew")
        self.grid_rowconfigure(5, weight=1)

        # Fake data #
        options = ['Todos', 'Projeto 1', 'Projeto 2', 'Etiqueta 1', 'Etiqueta 2']

        label = GridLabel(self, row=0, col=0, text="Projeto/Etiqueta")
        label.config(bg="#add8e6")
        label.grid_configure(sticky="w", padx=(10, 100), pady=(110, 0))

        dropdown = GridDropdown(self, row=1, col=0, values=options)
        dropdown.set("Todos")
        dropdown.grid_configure(padx=10)

        filter_button = GridButton(self, row=4, col=0, text="Filtrar", command=lambda: print('filter'))
        filter_button.grid_configure(padx=10, pady=20, sticky="nsew")

        back_button = GridButton(self, row=5, col=0, text="Voltar", command=back)
        back_button.grid_configure(sticky="sw", padx=10, pady=10)


class DashboardPage(tk.Frame):
    def __init__(self, master, on_close=None):
        super().__init__(master)
        self.configure(bg="#eaeaea")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        Sidebar(self, row=0, col=0, back=on_close)
        Dashboard(self, row=0, col=1, rowspan=2)
