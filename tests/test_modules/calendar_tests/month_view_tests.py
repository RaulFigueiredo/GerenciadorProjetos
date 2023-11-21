"""
TestMonthView: Concentrates on testing the month view component of the calendar application. 
  It ensures that the view correctly displays the monthly layout, handles task details 
  appropriately, and updates the display as needed.
"""
import unittest
from unittest.mock import Mock, patch
from src import MonthView

class TestMonthView(unittest.TestCase):
    """
    Test suite for the MonthView class.

    This suite includes tests for clearing the view, creating day headers, and showing task
    details, both with and without tasks present.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment by initializing the MonthView instance with mock objects.
        """
        self.mock_calendar_frame = Mock()
        self.mock_tasks_dict = {}
        self.mock_task_details = Mock()
        self.month_view = MonthView(self.mock_calendar_frame,
                                    self.mock_tasks_dict, self.mock_task_details)

    def test_clear_view(self) -> None:
        """
        Test the functionality of clearing the view.

        This test checks if the MonthView correctly clears all child widgets from the calendar
        frame, ensuring a clean slate for displaying new content.
        """
        mock_widgets = [Mock(), Mock(), Mock()]
        self.mock_calendar_frame.winfo_children.return_value = mock_widgets

        self.month_view.clear_view()

        for widget in mock_widgets:
            widget.destroy.assert_called_once()

    def test_create_day_headers(self) -> None:
        """
        Test the creation of day headers.

        This test verifies if the MonthView correctly creates and positions headers for each day
        of the week in the calendar view.
        """
        with patch('tkinter.Label') as mock_label_class:
            self.month_view.create_day_headers()

            expected_day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            for i, name in enumerate(expected_day_names):
                mock_label_class.assert_any_call(self.mock_calendar_frame, text=name, fg="black")

            for i, _ in enumerate(expected_day_names):
                mock_label_class.return_value.grid.assert_any_call(column=i, row=0, sticky='nsew')

    def test_show_task_details_with_tasks(self) -> None:
        """
        Test displaying task details for a day with tasks.

        This test checks if the MonthView correctly calls the show_task_details method with
        the appropriate task information when a day with tasks is selected.
        """
        day_with_tasks = "2023-01-01"
        tasks_for_day = [("Task1", "Description1"), ("Task2", "Description2")]
        self.mock_tasks_dict = {day_with_tasks: tasks_for_day}
        self.month_view.tasks_dict = self.mock_tasks_dict

        self.month_view.showTaskDetails(day_with_tasks)

        self.mock_task_details.show_task_details.assert_called_once_with(tasks_for_day)

    def test_show_task_details_without_tasks(self) -> None:
        """
        Test displaying task details for a day without tasks.

        This test verifies if the MonthView correctly avoids calling the show_task_details
        method when a day without tasks is selected.
        """
        day_without_tasks = "2023-01-02"
        self.mock_tasks_dict = {}
        self.month_view.tasks_dict = self.mock_tasks_dict

        self.month_view.showTaskDetails(day_without_tasks)

        self.mock_task_details.show_task_details.assert_not_called()
