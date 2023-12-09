import unittest
import tkinter as tk
import matplotlib.pyplot as plt
from src.gui.dashboard import GridFrame, GridLabel, GridDropdown, GridButton
from src.gui.dashboard import DashboardUtils, Dashboard, Sidebar, DashboardPage


class TestDashboardComponents(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    def test_grid_frame_creation(self):
        grid_frame = GridFrame(self.root, 0, 0, rowspan=2, colspan=2)
        self.assertIsInstance(grid_frame, tk.Frame)
        self.assertEqual(grid_frame.grid_info()['row'], 0)
        self.assertEqual(grid_frame.grid_info()['column'], 0)
        self.assertEqual(grid_frame.grid_info()['rowspan'], 2)
        self.assertEqual(grid_frame.grid_info()['columnspan'], 2)
        self.assertEqual(grid_frame['bg'], '#000000')

    def test_grid_label_creation(self):
        grid_label = GridLabel(self.root, 0, 0, text="Test Label")
        self.assertIsInstance(grid_label, tk.Label)
        self.assertEqual(grid_label.grid_info()['row'], 0)
        self.assertEqual(grid_label.grid_info()['column'], 0)
        self.assertEqual(grid_label['text'], "Test Label")
        self.assertEqual(grid_label['bg'], '#ffffff')
        self.assertEqual(grid_label['fg'], '#ffffff')

    def test_grid_dropdown_creation(self):
        options = ['Option 1', 'Option 2', 'Option 3']
        grid_dropdown = GridDropdown(self.root, 0, 0, values=options)
        self.assertIsInstance(grid_dropdown, tk.ttk.Combobox)

    def test_grid_button_creation(self):
        grid_button = GridButton(self.root, 0, 0, text="Test Button", command=lambda: None)
        self.assertIsInstance(grid_button, tk.Button)

    def test_dashboard_utils(self):
        # Create a parent frame to add the plot
        parent_frame = tk.Frame(self.root)
        parent_frame.grid(row=0, column=0)

        # Create a canvas to simulate a plot
        test_plot = plt.subplots()[0]

        # Use DashboardUtils to add the plot to the parent frame
        DashboardUtils.add_plot(parent_frame, test_plot, row=0, col=0)

        # Check if the plot is added to the parent frame
        children = parent_frame.winfo_children()
        canvas_exists = any(isinstance(child, tk.Canvas) for child in children)
        self.assertTrue(canvas_exists)

    def test_dashboard_creation(self):
        dashboard = Dashboard(self.root, 0, 0)
        self.assertIsInstance(dashboard, Dashboard)

    def test_sidebar_creation(self):
        sidebar = Sidebar(self.root, 0, 0, lambda: None)
        self.assertIsInstance(sidebar, Sidebar)

    def test_dashboard_page_creation(self):
        dashboard_page = DashboardPage(self.root)
        self.assertIsInstance(dashboard_page, DashboardPage)


if __name__ == '__main__':
    unittest.main()
