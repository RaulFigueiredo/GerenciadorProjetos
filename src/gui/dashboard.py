"""
Module for creating dashboard elements using tkinter and matplotlib.

This module includes classes and utilities for constructing a dashboard interface
using tkinter for the GUI components and matplotlib for plotting visualizations.

Classes:
- GridFrame: A grid-based frame for organizing GUI elements.
- GridLabel: A label widget integrated into the grid system.
- GridDropdown: A dropdown widget in the grid layout.
- GridButton: A button widget designed to work within a grid.
- DashboardUtils: Utility functions for managing plots within the dashboard.
- DashboardPlots: Manage multiple plots for display within the dashboard.
- Dashboard: Constructs the main dashboard interface.
- Sidebar: Constructs the sidebar interface for the dashboard.
- DashboardPage: Organizes the complete dashboard page with components.

Usage:
This module serves as a collection of tools and components to build a graphical
dashboard interface with customizable plots, labels, buttons, and sidebar elements.
"""

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.logic.dashboard.plot import Plot
from src.logic.dashboard.dashboard_data import DashboardData


class GridFrame(tk.Frame):
    """ Grid frame.

    Args:
        tk (tk.Frame): tk frame
    """
    def __init__(self,parent:callable,row:int,col:int,rowspan:int=1,colspan:int=1) -> None:
        """ Initialize the grid frame.

        Args:
            parent (callable): Parent tk object
            row (int): Row position
            col (int): Column position
            rowspan (int, optional): Rowspan. Defaults to 1.
            colspan (int, optional): Columnspan. Defaults to 1.
        """
        super().__init__(parent)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#000000")
        self.grid_configure(sticky="nsew")

class GridLabel(tk.Label):
    """ Grid label.

    Args:
        tk (tk.Label): Label
    """
    def __init__(self,parent:callable,row:int,col:int,text:str,rowspan:int=1,colspan:int=1) -> None:
        """ Summary of class here.

        Args:
            parent (callable): Parent tk object
            row (int): Row position
            col (int): Column position
            text (str): Text to be displayed
            rowspan (int, optional): Rowspan. Defaults to 1.
            colspan (int, optional): Columnspan. Defaults to 1.
        """
        super().__init__(parent, text=text)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.config(bg="#ffffff", font=("Monospace", 12, "bold"), fg="#ffffff")
        self.grid_configure(sticky="ew")


class GridDropdown(ttk.Combobox):
    """ Grid dropdown.

    Args:
        ttk (ttl.Combobox): Combobox
    """
    def __init__(self,parent: callable, row:int, col:int,\
                  values:object, rowspan:int=1, colspan:int=1) -> None:
        super().__init__(parent, values=values)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        self.grid_configure(sticky="ew")


class GridButton(tk.Button):
    """ Grid button.

    Args:
        tk (tk.Button): Button widget
    """
    def __init__(self,parent: callable,row:int,col:int,text:str,\
                 command:callable,rowspan:int=1,colspan:int=1) -> None:
        super().__init__(parent, text=text, command=command)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)


class DashboardUtils:
    """ Utils for the dashboard.
    """
    @staticmethod
    def add_plot(parent:callable,plot:callable,row:int,col:int,\
                 rowspan:int=1,colspan:int=1) -> None:
        """ Add a plot to the dashboard.

        Args:
            parent (callable): Parent tk object
            plot (callable): Plot
            row (int): Row position
            col (int): Column position
            rowspan (int, optional): Rowspan. Defaults to 1.
            colspan (int, optional): Columnspan. Defaults to 1.
        """
        canvas = FigureCanvasTkAgg(plot, master=parent)
        canvas.get_tk_widget().grid(row=row, column=col, columnspan=colspan,
                                    rowspan=rowspan, padx=5, pady=5,
                                    sticky="nsew")
        for i in range(rowspan):
            parent.grid_rowconfigure(row + i, weight=1)
        for i in range(colspan):
            parent.grid_columnconfigure(col + i, weight=1)

class DashboardPlots():
    """ Plots for the dashboard.
    """
    def __init__(self) -> None:
        """ Initialize the plots.
        """
        self.plots = []

    def __iter__(self) -> iter:
        """ Iterator for the plots.

        Returns:
            iter: Iterator
        """
        return iter(self.plots)

    def add_plot(self, plot: callable, row:int, col:int, rowspan:int=1, colspan:int=1) -> None:
        """ Add a plot to the dashboard.
        Args:
            plot (callable): Plot
            row (int): Row position
            col (int): Column position
            rowspan (int, optional): Rowspan. Defaults to 1.
            colspan (int, optional): Columnspan. Defaults to 1.
        """
        self.plots.append({'plot': plot, 'row': row, 'col': col,
                           'rowspan': rowspan, 'colspan': colspan})


class Dashboard(tk.Frame):
    """ Dashboard.

    Args:
        tk (tk.Frame): tk frame
    """
    def __init__(
            self,
            parent: tk.Tk,
            row: int,
            col: int,
            dashboard_data: callable,
            rowspan: int=1,
            colspan: int =1
        ) -> None:
        """ Summary of class here.

        Args:
            parent (tk.Tk): Parent tk object
            row (int): Row position
            col (int): Column position
            dashboard_data (callable): Dashboard data
            rowspan (int, optional): Row span. Defaults to 1.
            colspan (int, optional): Colunm spam . Defaults to 1.
        """
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

        texts = [f"Tarefas\n{tasks}", f"Para Hoje\n{for_today}",\
                  f"Feitas\n{done}", f"Atrasadas\n{late}"]

        for i, _ in enumerate(texts):
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
            DashboardUtils.add_plot(plots, plot['plot'], plot['row'],\
                     plot['col'], plot['rowspan'], plot['colspan'])


class Sidebar(tk.Frame):
    """

    Args:
        tk (_type_):
    """
    def __init__(
            self,
            parent: tk.Tk,
            row: int,
            col: int,
            back: callable,
            dashboard_data: callable,
            rowspan: int=1,
            colspan: int =1
        ) -> None:
        """ Summary of class here.

        Args:
            parent (tk.Tk): Parent tk object
            row (int): Row position
            col (int): Column position
            back (callable): Back function
            dashboard_data (callable): Dashboard data
            rowspan (int, optional): Row span. Defaults to 1.
            colspan (int, optional): Colunm spam . Defaults to 1.
        """
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

    def update_dashboard(self, selected_project: callable) -> None:
        """ Update the dashboard with the selected project.

        Args:
            selected_project (callable): The selected project.
        """
        self.dashboard_data.update_data(selected_project)
        self.parent.winfo_children()[1].destroy()
        Dashboard(self.parent, row=0, col=1, dashboard_data=self.dashboard_data, rowspan=2)

class DashboardPage(tk.Frame):
    """ Summary of class here.

    Args:
        tk (tk): tk object
    """
    def __init__(self, master: tk.Tk, user: callable, on_close: callable=None) -> None:
        super().__init__(master)
        self.configure(bg="#eaeaea")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        dashboard_data = DashboardData(user)
        Sidebar(self, row=0, col=0, back=on_close, dashboard_data=dashboard_data)
        Dashboard(self, row=0, col=1, dashboard_data=dashboard_data, rowspan=2)
