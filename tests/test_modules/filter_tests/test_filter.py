"""
Module providing unit tests for the methods in the Filter class.

This module contains a TestCase class, TestFilterMethods, designed to perform
unit tests on methods within the Filter class to ensure their correct
functionality when filtering projects and tasks based on various criteria.

Usage:
    - The TestFilterMethods class contains individual test methods, each testing
specific functionalities of
      the methods in the Filter class.
    - Run the tests using the unittest framework by executing this module.

Example:
    # Run tests using the unittest framework
    python -m unittest <filename>.py

Test Cases:
    - test_filter_project_by_name: Test filtering a project by its name.
    - test_filter_project_by_similar_name: Test filtering projects by a similar name.
    - test_filter_projects_by_creation_date: Test filtering projects by creation date range.
    - test_filter_projects_by_end_date: Test filtering projects by end date range.
    - test_filter_projects_by_conclusion_date: Test filtering projects by conclusion date range.
    - test_filter_projects_by_status: Test filtering projects by status.
    - test_filter_projects_by_label_name: Test filtering projects by label name.
    - test_filter_tasks_by_creation_date: Test filtering tasks by creation date range.
    - test_filter_tasks_by_end_date: Test filtering tasks by end date range.
    - test_filter_tasks_by_conclusion_date: Test filtering tasks by conclusion date range.
    - test_filter_tasks_by_status: Test filtering tasks by status.

Note:
    - Each test method checks specific functionalities by providing test data and
asserting the expected results.
    - The test methods ensure the correct behavior of the methods within the Filter
class under various scenarios.
"""


import unittest
from datetime import date
from src import Project
from src.logic.filter.filter import Filter
from src.logic.authentication.authentication import LoginLogic


class TestFilterMethods(unittest.TestCase):
    """ Test filter methods

    Args:
        unittest (unittest.TestCase): TestCase
    """
    user = LoginLogic.login('John Doe', 'pwd123')

    def setUp(self):
        self.filter = Filter(self.user)

    def test_filter_project_by_name(self) -> None:
        """ Test if all projects are done
        """
        result = self.filter.filter_project_by_name(self.user.projects[0].name)
        self.assertIsInstance(result, Project)
        self.assertEqual(result.name, self.user.projects[0].name)

    def test_filter_project_by_similar_name(self) -> None:
        """ Test if all projects are done
        """
        result = self.filter.filter_projects_by_similar_name(self.user.projects[0].name[:-1])
        self.assertIsInstance(result, list)
        self.assertEqual(result[0].name, self.user.projects[0].name)

    def test_filter_projects_by_creation_date(self) -> None:
        """ Test if all projects are done
        """
        lower_limit = date(2023, 1, 1)
        upper_limit = date(2023, 2, 1)
        result = self.filter.filter_projects_by_creation_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.creation_date >= lower_limit
                                   and project.creation_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_end_date(self) -> None:
        """ Test if all projects are done
        """
        lower_limit = date(2023, 2, 1)
        upper_limit = date(2023, 3, 1)
        result = self.filter.filter_projects_by_end_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.end_date >= lower_limit
                                   and project.end_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_conclusion_date(self) -> None:
        """ Test if all projects are done
        """
        lower_limit = date(2023, 2, 15)
        upper_limit = date(2023, 3, 15)
        result = self.filter.filter_projects_by_conclusion_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.conclusion_date >= lower_limit
                                   and project.conclusion_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_status(self) -> None:
        """ Test if all projects are done
        """
        result = self.filter.filter_projects_by_status(True)
        self.assertIsInstance(result, list)
        self.assertTrue(all(list(map(lambda x: x.status, result))))

    def test_filter_projects_by_label_name(self) -> None:
        """ Test if all projects are done
        """
        result = self.filter.filter_projects_by_label_name('Faculdade')
        self.assertIsInstance(result, list)
        self.assertTrue(all(list(map(lambda x: x.label.name == 'Faculdade', result))))

    def test_filter_tasks_by_creation_date(self) -> None:
        """ Test if all tasks are done
        """
        lower_limit = date(2023, 2, 15)
        upper_limit = date(2023, 3, 15)
        result = self.filter.filter_tasks_by_creation_date(self.user.projects,
                     lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for task in result:
            inside_interval.append(task.creation_date >= lower_limit
                                   and task.creation_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_tasks_by_end_date(self) -> None:
        """ Test if all tasks are done
        """
        lower_limit = date(2023, 2, 15)
        upper_limit = date(2023, 3, 15)
        result = self.filter.filter_tasks_by_end_date(self.user.projects, lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for task in result:
            inside_interval.append(task.end_date >= lower_limit
                                   and task.end_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_tasks_by_conclusion_date(self) -> None:
        """ Test if all tasks are done
        """
        lower_limit = date(2023, 2, 15)
        upper_limit = date(2023, 3, 15)
        result = self.filter.filter_tasks_by_conclusion_date(self.user.projects,\
                     lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for task in result:
            inside_interval.append(task.conclusion_date >= lower_limit
                                   and task.conclusion_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_tasks_by_status(self) -> None:
        """ Test if all tasks are done
        """
        result = self.filter.filter_tasks_by_status(self.user.projects, False)
        self.assertTrue(all(list(map(lambda x: not x.status, result))))


if __name__ == '__main__':
    unittest.main()
