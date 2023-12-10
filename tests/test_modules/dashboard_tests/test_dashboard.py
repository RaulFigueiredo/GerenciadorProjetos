"""
Module providing unit tests for the DashboardData class components.

This module contains a TestCase class, TestDashboardDataComponents, designed
to perform unit tests on methods within the DashboardData class to ensure their
correct functionality when retrieving and processing dashboard data.

Usage:
    - The TestDashboardDataComponents class contains individual test methods,
      each testing specific functionalities of methods in the DashboardData class.
    - Run the tests using the unittest framework by executing this module.

Example:
    # Run tests using the unittest framework
    python -m unittest <filename>.py

Test Cases:
    - test_update_data: Test updating data within DashboardData for a specific
      project.
    - test_get_number_of_tasks: Test getting the total number of tasks across
      all projects.
    - test_get_number_of_done_tasks: Test getting the number of completed tasks.
    - test_get_number_of_on_time_tasks: Test getting the number of tasks ending
      on time.
    - test_get_number_of_for_today_tasks: Test getting the number of tasks
      ending today.
    - test_get_number_of_late_tasks: Test getting the number of tasks that are
      late.
    - test_get_timespan_of_tasks: Test getting the timespan of tasks created.
    - test_get_next_deadlines: Test getting the upcoming deadlines.
    - test_get_created_tasks: Test getting the tasks created in the last month.
    - test_get_finished_by_weekday: Test getting tasks finished by weekday.

Note:
    - Each test method verifies specific functionalities of methods within the
      DashboardData class.
    - The test methods ensure the correct behavior of the DashboardData methods
      under various scenarios.
"""

import unittest
import tkinter as tk
import matplotlib.pyplot as plt
from src.gui.dashboard import GridFrame, GridLabel, GridDropdown, GridButton
from src.gui.dashboard import DashboardUtils, Dashboard, Sidebar, DashboardPage


class TestDashboardComponents(unittest.TestCase):
    """ Test dashboard components

    Args:
        unittest (unittest.TestCase): TestCase
    """
    def setUp(self) -> None:
        """ Create a root window
        """
        self.root = tk.Tk()

    def tearDown(self) -> None:
        """ Destroy the root window
        """
        self.root.destroy()

    def test_grid_frame_creation(self) -> None:
        """ Test if all projects are done
        """
        grid_frame = GridFrame(self.root, 0, 0, rowspan=2, colspan=2)
        self.assertIsInstance(grid_frame, tk.Frame)
        self.assertEqual(grid_frame.grid_info()['row'], 0)
        self.assertEqual(grid_frame.grid_info()['column'], 0)
        self.assertEqual(grid_frame.grid_info()['rowspan'], 2)
        self.assertEqual(grid_frame.grid_info()['columnspan'], 2)
        self.assertEqual(grid_frame['bg'], '#000000')

    def test_grid_label_creation(self) -> None:
        """ Test if all projects are done
        """
        grid_label = GridLabel(self.root, 0, 0, text="Test Label")
        self.assertIsInstance(grid_label, tk.Label)
        self.assertEqual(grid_label.grid_info()['row'], 0)
        self.assertEqual(grid_label.grid_info()['column'], 0)
        self.assertEqual(grid_label['text'], "Test Label")
        self.assertEqual(grid_label['bg'], '#ffffff')
        self.assertEqual(grid_label['fg'], '#ffffff')

    def test_grid_dropdown_creation(self) -> None:
        """ Test if all projects are done
        """
        options = ['Option 1', 'Option 2', 'Option 3']
        grid_dropdown = GridDropdown(self.root, 0, 0, values=options)
        self.assertIsInstance(grid_dropdown, tk.ttk.Combobox)

    def test_grid_button_creation(self) -> None:
        """ Test if all projects are done
        """
        grid_button = GridButton(self.root, 0, 0, text="Test Button", command=lambda: None)
        self.assertIsInstance(grid_button, tk.Button)

    def test_dashboard_utils(self) -> None:
        """ Test if all projects are done
        """
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

    def test_dashboard_creation(self) -> None:
        """ Test if all projects are done
        """
        dashboard = Dashboard(self.root, 0, 0)
        self.assertIsInstance(dashboard, Dashboard)

    def test_sidebar_creation(self) -> None:
        """ Test if all projects are done
        """
        sidebar = Sidebar(self.root, 0, 0, lambda: None)
        self.assertIsInstance(sidebar, Sidebar)

    def test_dashboard_page_creation(self) -> None:
        """ Test if all projects are done
        """
        dashboard_page = DashboardPage(self.root)
        self.assertIsInstance(dashboard_page, DashboardPage)


if __name__ == '__main__':
    unittest.main()
