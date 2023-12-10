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

from src.logic.authentication.authentication import LoginLogic
from src.logic.dashboard.dashboard_data import DashboardData


class TestDashboardDataComponents(unittest.TestCase):
    """ Test dashboard data components

    Args:   
        unittest (unittest.TestCase): TestCase
    """
    user = LoginLogic.login('John Doe', 'pwd123')

    def setUp(self) -> None:
        """ Set up the test
        """
        self.dashboard_data = DashboardData(self.user)

    def test_update_data(self) -> None:
        """ Test if all projects are done
        """
        self.dashboard_data.update_data("Project 1")
        self.assertLessEqual(len(self.dashboard_data.projects), 1)

    def test_get_number_of_tasks(self) -> None:
        """ Test if all projects are done
        """
        tasks = []
        for project in self.dashboard_data.projects:
            tasks += [task for task in project.tasks]
        self.assertEqual(self.dashboard_data.get_number_of_tasks(), len(tasks))

    def test_get_number_of_done_tasks(self) -> None:
        """ Test if all projects are done 
        """
        self.assertIsInstance(self.dashboard_data.get_number_of_done_tasks(), int)

    def test_get_number_of_on_time_tasks(self) -> None:
        """ Test if all projects are done 
        """
        self.assertIsInstance(self.dashboard_data.get_number_of_on_time_tasks(), int)

    def get_number_of_for_today_tasks(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_number_of_for_today_tasks(), int)

    def test_get_number_of_late_tasks(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_number_of_late_tasks(), int)

    def test_get_timespan_of_tasks(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_timespan_of_tasks(), dict)

    def test_get_next_deadlines(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_next_deadlines(), dict)

    def test_get_created_tasks(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_created_tasks(), dict)

    def test_get_finished_by_weekday(self) -> None:
        """ Test if all projects are done
        """
        self.assertIsInstance(self.dashboard_data.get_finished_by_weekday(), dict)


if __name__ == '__main__':
    unittest.main()
