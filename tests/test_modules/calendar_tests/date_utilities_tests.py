"""
- TestDateUtilities: Verifies the accuracy of date-related calculations, such as leap year 
  determination, day-of-the-week calculations, and days-in-month computations. These tests 
  are crucial for ensuring the reliability of date manipulations within the application.
"""
import unittest
from src import DateUtilities

class TestDateUtilities(unittest.TestCase):
    """
    Test suite for the DateUtilities class.

    This suite includes tests for leap year determination, starting day of a month, and the
    number of days in a month, covering a variety of years and months.
    """

    def test_is_leap_year(self) -> None:
        """
        Test the leap year determination functionality.

        This test checks if the method correctly identifies leap years and non-leap years,
        including edge cases like years divisible by 100 but not by 400.
        """
        self.assertTrue(DateUtilities.is_leap_year(2000))
        self.assertTrue(DateUtilities.is_leap_year(2004))

        self.assertFalse(DateUtilities.is_leap_year(1900))
        self.assertFalse(DateUtilities.is_leap_year(2001))

    def test_day_month_starts(self) -> None:
        """
        Test the calculation of the starting day of a month.

        This test verifies if the method correctly calculates the day of the week a given month
        starts on, for various months and years.
        """
        self.assertEqual(DateUtilities.day_month_starts(1, 2020), 3)
        self.assertEqual(DateUtilities.day_month_starts(2, 2021), 1)

        self.assertNotEqual(DateUtilities.day_month_starts(1, 2020), 2)
        self.assertNotEqual(DateUtilities.day_month_starts(2, 2021), 5)

    def test_days_in_month(self) -> None:
        """
        Test the calculation of the number of days in a month.

        This test checks if the method accurately returns the correct number of days for
        different months and years, including leap years.
        """
        self.assertEqual(DateUtilities.days_in_month(1, 2021), 31)
        self.assertEqual(DateUtilities.days_in_month(7, 2021), 31)

        self.assertEqual(DateUtilities.days_in_month(4, 2021), 30)
        self.assertEqual(DateUtilities.days_in_month(11, 2021), 30)

        self.assertEqual(DateUtilities.days_in_month(2, 2021), 28)
        self.assertEqual(DateUtilities.days_in_month(2, 2020), 29)
