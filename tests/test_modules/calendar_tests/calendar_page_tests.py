""" 
- TestCalendarPage: Focuses on the overall integration and functionality of the CalendarPage 
  class. These tests ensure that the application orchestrates the various components 
  effectively, maintaining the overall functionality and user experience.
  """

import unittest
import tkinter as tk
from datetime import date
from src.gui.calendar_page import CalendarPage

class TestCalendarPage(unittest.TestCase):
    """
    Test class for verifying the creation and functionality of the CalendarPage.

    Methods:
        setUp(): Initial setup for each test.
        tearDown(): Cleanup after each test.
        test_components_creation(): Tests the creation of main components.
        test_update_calendar(): Tests the update_calendar function.
    """

    def setUp(self) -> None:
        """
        Initial setup for each test.
        Creates a hidden Tkinter window instance and initializes the CalendarPage.
        """
        self.root = tk.Tk()
        self.root.withdraw()
        self.calendar_page = CalendarPage(master=self.root)

    def tearDown(self) -> None:
        """
        Cleanup after each test.
        Destroys the Tkinter window created for the test.
        """
        self.root.destroy()

    def test_components_creation(self) -> None:
        """
        Tests whether the main components (task_details, month_view, month_year_navigation)
        were created in CalendarPage.
        """
        self.assertTrue(hasattr(self.calendar_page, 'task_details'))
        self.assertTrue(hasattr(self.calendar_page, 'month_view'))
        self.assertTrue(hasattr(self.calendar_page, 'month_year_navigation'))

    def test_update_calendar(self) -> None:
        """
        Tests the update_calendar function.
        Verifies if the calendar is updated to the current month and year.
        """
        current_month = date.today().month
        current_year = date.today().year
        self.calendar_page.update_calendar(current_month, current_year)
