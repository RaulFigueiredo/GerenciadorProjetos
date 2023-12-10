import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.logic.dashboard.plot import Plot
from src.logic.dashboard.dashboard_data import DashboardData


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
    def __init__(self, parent, row, col, dashboard_data, rowspan=1, colspan=1):
        super().__init__(parent)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#eaeaea")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_configure(padx=20, pady=20)

        cards = GridFrame(self, row=0, col=0)
        cards.config(bg="#eaeaea")

        tasks = dashboard_data.get_number_of_tasks()
        for_today = dashboard_data.get_number_of_for_today_tasks()
        done = dashboard_data.get_number_of_done_tasks()
        late = dashboard_data.get_number_of_late_tasks()

        texts = [f"Tarefas\n{tasks}", f"Para Hoje\n{for_today}", f"Feitas\n{done}", f"Atrasadas\n{late}"]
        for i in range(len(texts)):
            cards.grid_columnconfigure(i, weight=1)
            label = GridLabel(cards, 0, i, text=texts[i])
            label.config(height=4, fg="#000000")
            label.grid_configure(padx=5, pady=5)

        plots = GridFrame(self, row=1, col=0)
        plots.config(bg="#eaeaea")


        # Fake data #
        tasks = {'Feitas': done,
                 'Para fazer': dashboard_data.get_number_of_on_time_tasks(),
                 'Atrasadas': late}
        tasks_timespan = dashboard_data.get_timespan_of_tasks()
        next_deadlines = dashboard_data.get_next_deadlines()
        total_tasks = dashboard_data.get_created_tasks()
        finished_by_week_day = dashboard_data.get_finished_by_weekday()

        plot1 = Plot.make_donutplot(tasks, 'Tarefas')
        plot2 = Plot.make_barplot(tasks_timespan, 'Duração das Tarefas (semanas)')
        plot3 = Plot.make_pieplot(next_deadlines, 'Próximos Limites (semanas)')
        plot4 = Plot.make_areaplot(total_tasks, 'Total de Tarefas Criadas')
        plot5 = Plot.make_lineplot(finished_by_week_day, 'Tarefas Concluídas')

        dash_plots = DashboardPlots()
        dash_plots.add_plot(plot1, 0, 0)
        dash_plots.add_plot(plot2, 0, 1)
        dash_plots.add_plot(plot3, 0, 2)
        dash_plots.add_plot(plot4, 1, 0)
        dash_plots.add_plot(plot5, 1, 1, colspan=2)

        for plot in dash_plots:
            DashboardUtils.add_plot(plots, plot['plot'], plot['row'], plot['col'], plot['rowspan'], plot['colspan'])


class Sidebar(tk.Frame):
    def __init__(self, parent, row, col, back, dashboard_data, rowspan=1, colspan=1):
        super().__init__(parent)
        self.parent = parent
        self.dashboard_data = dashboard_data
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#add8e6")
        self.grid_configure(sticky="nsew")
        self.grid_rowconfigure(5, weight=1)

        options = ['Todos'] + [project.name for project in dashboard_data.projects]

        label = GridLabel(self, row=0, col=0, text="Projeto")
        label.config(bg="#add8e6")
        label.grid_configure(sticky="w", padx=(10, 100), pady=(110, 0))

        dropdown = GridDropdown(self, row=1, col=0, values=options)
        dropdown.set("Todos")
        dropdown.grid_configure(padx=10)

        filter_button = GridButton(self, row=4, col=0, text="Filtrar",
                                   command=lambda: self.update_dashboard(dropdown.get()))
        filter_button.grid_configure(padx=10, pady=20, sticky="nsew")

        back_button = GridButton(self, row=5, col=0, text="Voltar", command=back)
        back_button.grid_configure(sticky="sw", padx=10, pady=10)
    
    def update_dashboard(self, selected_project):
        self.dashboard_data.update_data(selected_project)
        self.parent.winfo_children()[1].destroy()
        Dashboard(self.parent, row=0, col=1, dashboard_data=self.dashboard_data, rowspan=2)



class DashboardPage(tk.Frame):
    def __init__(self, master, user, on_close=None):
        super().__init__(master)
        self.configure(bg="#eaeaea")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        dashboard_data = DashboardData(user)
        Sidebar(self, row=0, col=0, back=on_close, dashboard_data=dashboard_data)
        Dashboard(self, row=0, col=1, dashboard_data=dashboard_data, rowspan=2)
