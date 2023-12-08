import unittest
from unittest.mock import Mock, patch
from src.logic.calendar.month_view import MonthView  # Importação correta da classe MonthView

class TestMonthView(unittest.TestCase):
    """
    Test suite for the MonthView class.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment by initializing the MonthView instance with mock objects.
        """
        self.mock_calendar_frame = Mock()
        self.mock_calendar_frame.winfo_screenwidth.return_value = 800
        self.mock_calendar_frame.winfo_screenheight.return_value = 600
        self.mock_tasks_dict = {}
        self.mock_task_details = Mock()
        self.month_view = MonthView(self.mock_calendar_frame,
                                    self.mock_tasks_dict, self.mock_task_details, (1, 2023))

    def test_clear_view(self) -> None:
        """
        Test the functionality of clearing the view.
        """
        mock_widgets = [Mock(), Mock(), Mock()]
        self.mock_calendar_frame.winfo_children.return_value = mock_widgets

        self.month_view.clear_view()

        for widget in mock_widgets:
            widget.destroy.assert_called_once()

    def test_create_day_headers(self) -> None:
        """
        Test the creation of day headers.
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
        """
        day_with_tasks = "2023-01-01"
        tasks_for_day = [("Task1", "Description1"), ("Task2", "Description2")]
        self.mock_tasks_dict = {day_with_tasks: tasks_for_day}
        self.month_view.tasks_dict = self.mock_tasks_dict

        self.month_view.show_task_details_view(day_with_tasks)

        self.mock_task_details.show_task_details.assert_called_once_with(tasks_for_day)

    def test_show_task_details_without_tasks(self) -> None:
        """
        Test displaying task details for a day without tasks.
        """
        day_without_tasks = "2023-01-02"
        self.mock_tasks_dict = {}
        self.month_view.tasks_dict = self.mock_tasks_dict

        self.month_view.show_task_details_view(day_without_tasks)
        self.mock_task_details.show_task_details.assert_not_called()

if __name__ == '__main__':
    unittest.main()