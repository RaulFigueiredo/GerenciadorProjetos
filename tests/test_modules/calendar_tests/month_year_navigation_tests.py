""" 
- TestMonthYearNavigationLogic: Tests the logic for navigating through months and years in 
  the calendar. This includes ensuring that navigation controls work correctly and that 
  transitions between months and years are handled smoothly.
"""

from unittest.mock import Mock
import unittest
from src import MonthYearNavigation

class TestMonthYearNavigationLogic(unittest.TestCase):
    """
    Test suite for the MonthYearNavigation class.

    This suite includes tests for navigating through months and years, covering cases for both
    forward and backward month changes, and updating the display of the current month and year.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment by initializing the MonthYearNavigation
        instance with mock objects.
        """
        self.mock_button_back = Mock()
        self.mock_label_month_year = Mock()
        self.mock_button_forward = Mock()
        self.mock_update_callback = Mock()

        self.navigation = MonthYearNavigation(self.mock_button_back, self.mock_button_back,
                                              self.mock_label_month_year, self.mock_button_forward,
                                              self.mock_update_callback)

    def test_change_month_forward(self) -> None:
        """
        Test the functionality of changing the month forward.

        This test checks if the month is correctly incremented when moving forward, and if the
        year remains the same when not crossing the year boundary.
        """
        for initial_month in range(1, 12):
            self.navigation.month = initial_month
            self.navigation.year = 2023
            expected_month = initial_month + 1
            expected_year = 2023

            new_month, new_year = self.navigation.change_month(1)
            self.assertEqual((new_month, new_year), (expected_month, expected_year))

    def test_change_month_backward(self) -> None:
        """
        Test the functionality of changing the month backward.

        This test checks if the month is correctly decremented when moving backward, and if the
        year remains the same when not crossing the year boundary.
        """
        for initial_month in range(2, 13):
            self.navigation.month = initial_month
            self.navigation.year = 2023
            expected_month = initial_month - 1
            expected_year = 2023

            new_month, new_year = self.navigation.change_month(-1)
            self.assertEqual((new_month, new_year), (expected_month, expected_year))

    def test_update_display(self) -> None:
        """
        Test the update of the month and year display.

        This test checks if the display label is correctly updated for different months and years,
        and verifies if the update callback function is called with the correct parameters.
        """
        test_cases = [(1, 2023, "Janeiro"), (2, 2023, "Fevereiro"), (12, 2022, "Dezembro")]
        for month, year, expected_month_name in test_cases:
            with self.subTest(month=month, year=year):
                written_month, returned_year = self.navigation.update_display(month, year)

                self.mock_label_month_year.config.assert_called_with(
                    text=f"{expected_month_name} {year}")
                self.mock_update_callback.assert_called_with(month, year)
                self.assertEqual(written_month, expected_month_name)
                self.assertEqual(returned_year, year)
