"""
This module contains the DateUtilities class, which provides various static
methods for handling date calculations and calendar functionalities.

The DateUtilities class includes methods to determine leap years, calculate the starting
day of the week for any given month and year, and determine the number of days in a month.
"""

class DateUtilities:
    """
    A class providing utilities for date manipulation in our calendar application.
    """

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Determine if a given year is a leap year.

        Args:
            year (int): The year to be checked.

        Returns:
            bool: True if the year is a leap year, False otherwise.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def day_month_starts(month: int, year: int) -> int:
        """
        Calculate the day of the week the first of a month falls on.

        Args:
            month (int): The month (1-12).
            year (int): The year.

        Returns:
            int: An integer representing the day of the week (0 for Sunday, 6 for Saturday).
        """
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        # Zeller's congruence formula
        f = 1
        h = (f + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7
        day_of_week = (h + 6) % 7

        return day_of_week

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        """
        Calculate the number of days in a given month of a given year.

        Args:
            month (int): The month (1-12).
            year (int): The year.

        Returns:
            int: The number of days in the specified month.
        """
        if month in [1, 3, 5, 7, 8, 10, 12]:
            number_days = 31
        elif month in [4, 6, 9, 11]:
            number_days = 30
        else:
            number_days = 29 if DateUtilities.is_leap_year(year) else 28

        return number_days
