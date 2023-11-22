"""
- TestCalendarDisplay: Validates the initialization and configuration of the calendar 
  display. It ensures that all UI components are correctly created and laid out, 
  contributing to a cohesive and functional user display.
"""
import unittest
import tkinter as tk
from src import CalendarDisplay


class TestCalendarDisplay(unittest.TestCase):
    """
    Test class for verifying the creation and functionality of the calendar display.

    Methods:
        setUp(): Initial setup for each test.
        tearDown(): Cleanup after each test.
        test_navigation_frame_creation(): Tests the creation of the navigation frame.
        test_month_view_creation(): Tests the creation of the month view frame.
        test_task_details_creation(): Tests the creation of the task details frame.
        test_buttons_creation(): Tests the creation of buttons.
    """

    def setUp(self) -> None:
        """
        Initial setup for each test.
        Creates a hidden Tkinter window instance and initializes the calendar display.
        """
        self.root = tk.Tk()
        self.root.withdraw()  # Hides the main root window
        self.calendar_display = CalendarDisplay(master=self.root)

    def tearDown(self) -> None:
        """
        Cleanup after each test.
        Destroys the Tkinter window created for the test.
        """
        self.root.destroy()

    def test_navigation_frame_creation(self) -> None:
        """
        Tests whether the navigation_frame was created and is an instance of tk.Frame.
        """
        self.assertTrue(hasattr(self.calendar_display, 'navigation_frame'))
        self.assertIsInstance(self.calendar_display.navigation_frame, tk.Frame)

    def test_month_view_creation(self) -> None:
        """
        Tests whether the calendar_frame was created and is an instance of tk.Frame.
        """
        self.assertTrue(hasattr(self.calendar_display, 'calendar_frame'))
        self.assertIsInstance(self.calendar_display.calendar_frame, tk.Frame)

    def test_task_details_creation(self) -> None:
        """
        Tests whether the details_frame was created and is an instance of tk.Frame.
        """
        self.assertTrue(hasattr(self.calendar_display, 'details_frame'))
        self.assertIsInstance(self.calendar_display.details_frame, tk.Frame)

    def test_buttons_creation(self) -> None:
        """
        Tests whether the buttons (button_back, button_forward, close_button, back_button)
        were created and are instances of tk.Button.
        """
        self.assertTrue(hasattr(self.calendar_display, 'button_back'))
        self.assertTrue(hasattr(self.calendar_display, 'button_forward'))
        self.assertTrue(hasattr(self.calendar_display, 'close_button'))
        self.assertTrue(hasattr(self.calendar_display, 'back_button'))

        self.assertIsInstance(self.calendar_display.button_back, tk.Button)
        self.assertIsInstance(self.calendar_display.button_forward, tk.Button)
        self.assertIsInstance(self.calendar_display.close_button, tk.Button)
        self.assertIsInstance(self.calendar_display.back_button, tk.Button)
