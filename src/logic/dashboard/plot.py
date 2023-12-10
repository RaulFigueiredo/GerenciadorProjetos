"""
Module providing a Plot class for generating various types of plots using Matplotlib.

This module contains a class, Plot, with static methods to generate different types of plots:
    - Line plot using make_lineplot()
    - Bar plot using make_barplot()
    - Area plot using make_areaplot()
    - Pie plot using make_pieplot()
    - Donut plot using make_donutplot()

Usage:
    - Call the static methods of the Plot class to generate different types of plots by providing:
        - Data as a dictionary to be plotted.
        - Title for the plot.
    - Each method returns a Matplotlib Figure object containing the generated plot.

Example:
    # Create a line plot
    line_plot_data = {'Jan': 10, 'Feb': 15, 'Mar': 20, 'Apr': 25}
    line_plot = Plot.make_lineplot(line_plot_data, 'Monthly Progress')

    # Create a bar plot
    bar_plot_data = {'Category A': 30, 'Category B': 40, 'Category C': 20}
    bar_plot = Plot.make_barplot(bar_plot_data, 'Category Distribution')

    # Create an area plot
    area_plot_data = {'Jan': 10, 'Feb': 15, 'Mar': 20, 'Apr': 25}
    area_plot = Plot.make_areaplot(area_plot_data, 'Monthly Trends')

    # Create a pie plot
    pie_plot_data = {'Category A': 30, 'Category B': 40, 'Category C': 20}
    pie_plot = Plot.make_pieplot(pie_plot_data, 'Category Percentage')

    # Create a donut plot
    donut_plot_data = {'Category A': 30, 'Category B': 40, 'Category C': 20}
    donut_plot = Plot.make_donutplot(donut_plot_data, 'Category Distribution')

Note:
    - Ensure the provided data is in the form of a dictionary.
    - Each method returns a Matplotlib Figure object, which can be further customized
or displayed as desired.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


class Plot:
    """ Plot class

    Returns:
        _type_: Plots
    """
    @staticmethod
    def set_style() -> None:
        """ Set the style of the plot
        """
        plt.close()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().set_facecolor('#FFFFFF')
        plt.gcf().set_facecolor('#FFFFFF')
        plt.tick_params(axis='x', which='both', colors='grey', bottom=False,
                        top=False)
        plt.tick_params(axis='y', which='both', colors='grey', left=False,
                        right=False)
        plt.grid(True, linestyle='-', axis='y', linewidth=0.5,
                 color='grey', alpha=0.5)

    @staticmethod
    def make_lineplot(data: dict, title: str) -> plt.Figure:
        """ Make a line plot

        Args:
            data (dict): Data to be plotted
            title (str): Title of the plot

        Returns:
            plt.Figure: The line plot
        """
        plt.close()
        x, y = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.plot(x, y)
        ax.scatter(x, y)
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_barplot(data: dict, title: str) -> plt.Figure:
        """ Make a bar plot

        Args:
            data (dict): Data to be plotted
            title (str): Title of the plot

        Returns:
            plt.Figure: The bar plot
        """
        plt.close()
        sorted_ = sorted(data.items(), key=lambda item: item[1], reverse=True)
        labels = [i[0] for i in sorted_]
        values = [i[1] for i in sorted_]
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(labels, values, zorder=4)
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_areaplot(data: dict, title: str) -> plt.Figure:
        """ Make an area plot

        Args:
            data (dict): Data to be plotted
            title (str): Title of the plot

        Returns:
            plt.Figure: The area plot
        """
        plt.close()
        x, y = list(data.keys()), list(data.values())
        x = [datetime.datetime.strptime(date, '%d-%m-%Y') for date in x]
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.fill_between(x, y, zorder=4, alpha=0.8)
        ax.plot(x, y, zorder=4, alpha=1)
        ax.set_xticks(ax.get_xticks()[::len(ax.get_xticks()) // 4])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_pieplot(data: dict, title: str) -> plt.Figure:
        """ Make a pie plot

        Args:
            data (dict): Data to be plotted
            title (str): Title of the plot

        Returns:
            plt.Figure: The pie plot
        """
        plt.close()
        labels, values = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        try:
            _, cat_labels, val_labels = ax.pie(values, labels=labels,
                                            autopct='%1.0f%%')
            for label in cat_labels:
                label.set_color('grey')
            for label in val_labels:
                label.set_fontsize(8)
                label.set_color('black')
        except ValueError as e:
            print(e)
        ax.set_title(title)
        return fig

    @staticmethod
    def make_donutplot(data: dict, title: str) -> plt.Figure:
        """ Make a donut plot

        Args:
            data (dict): Data to be plotted
            title (str): Title of the plot

        Returns:
            plt.Figure: The donut plot
        """
        plt.close()
        labels, values = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        try:
            _, cat_labels, val_labels = ax.pie(values, labels=labels,
                                            startangle=-40,
                                            wedgeprops=dict(width=0.4),
                                            autopct='%1.0f%%', pctdistance=0.8)
            for label in cat_labels:
                label.set_color('grey')
            for label in val_labels:
                label.set_fontsize(8)
                label.set_color('black')
        except ValueError as e:
            print(e)

        ax.set_title(title)
        return fig
