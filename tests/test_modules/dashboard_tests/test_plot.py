import unittest
import matplotlib.pyplot as plt
from src.logic.dashboard.plot import Plot


class TestPlotFunctions(unittest.TestCase):

    def test_set_style(self):
        # Test if set_style() modifies plot settings correctly
        Plot.set_style()

        # Assert style changes
        self.assertFalse(plt.gca().spines['top'].get_visible())
        self.assertFalse(plt.gca().spines['right'].get_visible())
        self.assertFalse(plt.gca().spines['left'].get_visible())
        self.assertFalse(plt.gca().spines['bottom'].get_visible())

    def test_make_lineplot(self):
        # Test if make_lineplot() creates a line plot with expected title
        data = {'A': 1, 'B': 2, 'C': 3}
        title = 'Line Plot Test'
        fig = Plot.make_lineplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.lines), 1)

    def test_make_barplot(self):
        # Test if make_barplot() creates a bar plot with expected title
        data = {'A': 1, 'B': 2, 'C': 3}
        title = 'Bar Plot Test'
        fig = Plot.make_barplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.patches), len(data))  # Check if number of bars matches data points

    def test_make_areaplot(self):
        # Test if make_areaplot() creates an area plot with expected title
        data = {'2023-01-01': 10, '2023-01-02': 20, '2023-01-03': 15, '2023-01-04': 20, '2023-01-05': 20}
        title = 'Area Plot Test'
        fig = Plot.make_areaplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.collections), 1)  # Check if there's one area plot

    def test_make_pieplot(self):
        # Test if make_pieplot() creates a pie plot with expected title
        data = {'Category A': 40, 'Category B': 30, 'Category C': 20, 'Category D': 10}
        title = 'Pie Plot Test'
        fig = Plot.make_pieplot(data, title)

        # Assert plot creation and properties
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), title)
        self.assertEqual(len(ax.patches), len(data))  # Check if number of wedges matches data points

    def test_make_donutplot(self):
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
