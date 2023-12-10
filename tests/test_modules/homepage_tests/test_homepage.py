"""
Unit tests for HomePage, TopBar, and ProjectList classes in the application's GUI. These tests aim to ensure that the user interface components function as expected, responding correctly to user interactions and data changes.

Classes:
- TestTopBar: Tests for the TopBar class, focusing on navigation button functionalities.
- TestProjectList: Tests for the ProjectList class, focusing on project display and interaction functionalities.
- TestHomePage: Tests for the HomePage class, focusing on navigation and page display functionalities.

Methods:
- setUp and tearDown: Setup and cleanup methods for each test case.
- test_navigation_buttons (TestTopBar): Tests that the navigation buttons in the TopBar correctly call the provided callback function with the expected arguments.
- test_show_project_page (TestProjectList): Tests the functionality of displaying a selected project page.
- test_navigation_to_pages (TestHomePage): Tests navigation to different pages from the HomePage.
- test_show_home_page (TestHomePage): Tests that the HomePage displays correctly when called.
"""


import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from src.gui.homepage import HomePage, TopBar, ProjectList
from src.logic.users.user import User

class TestTopBar(unittest.TestCase):
    """
    Tests for the TopBar class of the application's GUI.

    This class tests if the navigation buttons in the TopBar correctly trigger navigation callbacks with expected arguments.
    """

    def setUp(self):
        """ Set up the test environment for TopBar. """
        self.root = tk.Tk()
        self.on_navigate = MagicMock()
        self.top_bar = TopBar(self.root, self.on_navigate, '#5a6e7f', 'white')
        
    def test_navigation_buttons(self):
        """ Test if navigation buttons correctly trigger navigation callbacks. """
        # Trigger each button and verify if the callback is called with the correct argument
        dashboard_button = self.top_bar.grid_slaves(row=0, column=1)[0]
        dashboard_button.invoke()
        self.on_navigate.assert_called_with('dashboard')

        calendar_button = self.top_bar.grid_slaves(row=0, column=2)[0]
        calendar_button.invoke()
        self.on_navigate.assert_called_with('calendario')

        history_button = self.top_bar.grid_slaves(row=0, column=3)[0]
        history_button.invoke()
        self.on_navigate.assert_called_with('historico')

        export_button = self.top_bar.grid_slaves(row=0, column=4)[0]
        export_button.invoke()
        self.on_navigate.assert_called_with('exportar')

        import_button = self.top_bar.grid_slaves(row=0, column=5)[0]
        import_button.invoke()
        self.on_navigate.assert_called_with('importar')

        labels_button = self.top_bar.grid_slaves(row=0, column=6)[0]
        labels_button.invoke()
        self.on_navigate.assert_called_with('labels')

        filter_project_button = self.top_bar.grid_slaves(row=0, column=7)[0]
        filter_project_button.invoke()
        self.on_navigate.assert_called_with('filter_by_projects')

        filter_label_button = self.top_bar.grid_slaves(row=0, column=8)[0]
        filter_label_button.invoke()
        self.on_navigate.assert_called_with('filter_by_labels')

        remove_filter_button = self.top_bar.grid_slaves(row=0, column=9)[0]
        remove_filter_button.invoke()
        self.on_navigate.assert_called_with('remove_filter')

    def tearDown(self):
        """ Clean up after tests. """
        self.root.destroy()

class TestProjectList(unittest.TestCase):
    """
    Tests for the ProjectList class of the application's GUI.

    This class tests the functionality of displaying projects and handling user interactions with the project list.
    """
    def setUp(self):
        """ Set up the test environment for ProjectList. """
        self.root = tk.Tk()
        self.user = User('TestUser')
        self.project_list = ProjectList(self.root, self.user)

    def test_show_project_page(self):
        """ Test the functionality of displaying a selected project page. """
        # Mock the open_page method of the project_manager
        self.project_list.project_manager.open_page = MagicMock()

        # Simulate selecting and opening a project
        project = MagicMock()
        self.project_list.show_project_page(project)
        self.project_list.project_manager.open_page.assert_called_with(project)

    def tearDown(self):
        """ Clean up after tests. """
        self.root.destroy()

class TestHomePage(unittest.TestCase):
    """
    Tests for the HomePage class of the application's GUI.

    This class tests the navigation functionalities to different pages from the HomePage and checks the display of the HomePage.
    """
    def setUp(self):
        """ Set up the test environment for HomePage. """
        self.root = tk.Tk()
        self.user = User('TestUser')
        self.home_page = HomePage(self.root, self.user)

    def test_navigation_to_pages(self):
        """ Test navigation to different pages from the HomePage. """
        # Mock the methods for navigating to different pages
        self.home_page.show_calendar_page = MagicMock()
        self.home_page.navigate('calendario')
        self.home_page.show_calendar_page.assert_called()

        self.home_page.show_dashboard_page = MagicMock()
        self.home_page.navigate('dashboard')
        self.home_page.show_dashboard_page.assert_called()

        self.home_page.show_history_page = MagicMock()
        self.home_page.navigate('historico')
        self.home_page.show_history_page.assert_called()

        self.home_page.show_export_page = MagicMock()
        self.home_page.navigate('exportar')
        self.home_page.show_export_page.assert_called()

        self.home_page.show_import_page = MagicMock()
        self.home_page.navigate('importar')
        self.home_page.show_import_page.assert_called()

        self.home_page.show_label_page = MagicMock()
        self.home_page.navigate('labels')
        self.home_page.show_label_page.assert_called()

        self.home_page.show_filter_project_page = MagicMock()
        self.home_page.navigate('filter_by_projects')
        self.home_page.show_filter_project_page.assert_called()

        self.home_page.show_label_filter_page = MagicMock()
        self.home_page.navigate('filter_by_labels')
        self.home_page.show_label_filter_page.assert_called()

        self.home_page.remove_project_filter = MagicMock()
        self.home_page.navigate('remove_filter')
        self.home_page.remove_project_filter.assert_called()

    def tearDown(self):
        """ Clean up after tests. """
        self.root.destroy()

class TestHomePage(unittest.TestCase):
    """
    Tests for the HomePage class of the application's GUI.
    """
    def setUp(self):
        """ Set up the test environment for HomePage. """
        self.root = tk.Tk()
        # Provide all necessary data for User creation
        self.mock_user = User("Test User", "testPassword")
        self.home_page = HomePage(self.root, self.mock_user)

    def tearDown(self):
        """ Clean up after tests."""
        self.root.destroy()

    def test_navigate_to_calendar(self):
        """ Test that the navigate method correctly calls the show_calendar_page method."""
        with patch.object(self.home_page, 'show_calendar_page') as mock_method:
            self.home_page.navigate('calendario')
            mock_method.assert_called_once()

    def test_navigate_to_dashboard(self):
        """ Test that the navigate method correctly calls the show_dashboard_page method."""
        with patch.object(self.home_page, 'show_dashboard_page') as mock_method:
            self.home_page.navigate('dashboard')
            mock_method.assert_called_once()

    def test_navigate_to_history(self):
        """ Test that the navigate method correctly calls the show_history_page method."""
        with patch.object(self.home_page, 'show_history_page') as mock_method:
            self.home_page.navigate('historico')
            mock_method.assert_called_once()

    def test_navigate_to_export(self):
        """ Test that the navigate method correctly calls the show_export_page method."""
        with patch.object(self.home_page, 'show_export_page') as mock_method:
            self.home_page.navigate('exportar')
            mock_method.assert_called_once()

    def test_navigate_to_import(self):
        """ Test that the navigate method correctly calls the show_import_page method."""
        with patch.object(self.home_page, 'show_import_page') as mock_method:
            self.home_page.navigate('importar')
            mock_method.assert_called_once()

    def test_navigate_to_labels(self):
        """ Test that the navigate method correctly calls the show_label_page method."""
        with patch.object(self.home_page, 'show_label_page') as mock_method:
            self.home_page.navigate('labels')
            mock_method.assert_called_once()

    def test_navigate_to_filter_project(self):
        """ Test that the navigate method correctly calls the show_filter_project_page method."""
        with patch.object(self.home_page, 'show_filter_project_page') as mock_method:
            self.home_page.navigate('filter_by_projects')
            mock_method.assert_called_once()

    def test_navigate_to_filter_label(self):
        """ Test that the navigate method correctly calls the show_label_filter_page method."""
        with patch.object(self.home_page, 'show_label_filter_page') as mock_method:
            self.home_page.navigate('filter_by_labels')
            mock_method.assert_called_once()

    def test_remove_filter(self):
        """ Test that the navigate method correctly calls the remove_project_filter method."""
        with patch.object(self.home_page, 'remove_project_filter') as mock_method:
            self.home_page.navigate('remove_filter')
            mock_method.assert_called_once()

    def test_show_home_page(self):
        """ Test that the HomePage displays correctly. """
        self.home_page.update_idletasks()  # Force GUI update
        self.assertTrue(self.home_page.top_bar.winfo_ismapped())

if __name__ == '__main__':
    unittest.main()
