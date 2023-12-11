"""
Module: plot_functions

This module contains classes and functions to create different types of plots using Matplotlib.
It also includes unit tests to validate the functionality of these plotting methods.

Classes:
    - Plot: Class containing static methods to generate line plots, bar plots, 
area plots, pie plots, and donut plots.

Functions:
    - test_set_style: Test to validate the set_style() function for configuring plot aesthetics.
    - test_make_lineplot: Test to ensure proper creation of line plots.
    - test_make_barplot: Test to verify the creation of bar plots.
    - test_make_areaplot: Test to validate the creation of area plots.
    - test_make_pieplot: Test to ensure the creation of pie plots.
    - test_make_donutplot: Test to verify the creation of donut plots.
"""

import unittest
import matplotlib.pyplot as plt
from src.logic.dashboard.plot import Plot


class TestPlotFunctions(unittest.TestCase):
    """ Test plot functions

    Args:
        unittest (unittest.TestCase): TestCase
    """

    def test_set_style(self) -> None:
        """ Test if set_style() modifies plot settings correctly
        """
        # Test if set_style() modifies plot settings correctly
        Plot.set_style()

        # Assert style changes
        self.assertFalse(plt.gca().spines['top'].get_visible())
        self.assertFalse(plt.gca().spines['right'].get_visible())
        self.assertFalse(plt.gca().spines['left'].get_visible())
        self.assertFalse(plt.gca().spines['bottom'].get_visible())

    def test_make_lineplot(self) -> None:
        """ Test if make_lineplot() creates a line plot with expected title
        """
        data = {'A': 1, 'B': 2, 'C': 3}
        title = 'Line Plot Test'
        fig = Plot.make_lineplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.lines), 1)

    def test_make_barplot(self) -> None:
        """ Test if make_barplot() creates a bar plot with expected title
        """
        data = {'A': 1, 'B': 2, 'C': 3}
        title = 'Bar Plot Test'
        fig = Plot.make_barplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.patches), len(data))  # Check if number of bars matches data points

    def test_make_areaplot(self) -> None:
        """ Test if make_areaplot() creates an area plot with expected title
        """
        data = {'01-01-2023': 10, '02-01-2023': 20, '03-01-2023': 15,
                '04-01-2023': 20, '05-01-2023': 20}
        title = 'Area Plot Test'
        fig = Plot.make_areaplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.collections), 1)

    def test_make_pieplot(self) -> None:
        """ Test if make_pieplot() creates a pie plot with expected title
        """
        data = {'Category A': 40, 'Category B': 30, 'Category C': 20, 'Category D': 10}
        title = 'Pie Plot Test'
        fig = Plot.make_pieplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.patches), len(data))

    def test_make_donutplot(self) -> None:
        """ Test if make_donutplot() creates a donut plot with expected title
        """
        # Test if make_donutplot() creates a donut plot with expected title
        data = {'Category A': 40, 'Category B': 30, 'Category C': 20, 'Category D': 10}
        title = 'Donut Plot Test'
        fig = Plot.make_donutplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.patches), len(data))


if __name__ == '__main__':
    unittest.main()
