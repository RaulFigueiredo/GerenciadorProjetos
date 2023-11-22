"""
This module contains a test suite for the 'History' module.

The 'TestHistory' class contains test cases to ensure the functionality of the
'History' module, specifically focusing on the 'HistorySingleton' class and its methods.

Test Cases:
    - setUp: Initializes the history manager instance and verifies its interface implementation.
    - test_new_add_completed_task_one_project: Tests the addition of completed tasks to the history
manager for a single project. Simulates project creation, task addition, and marks specific tasks
 as completed to validate their inclusion in the completed task list.
    - test_add_completed_task_multiple_projects: Tests the addition of completed tasks to the 
history manager for multiple projects. Simulates the creation of multiple projects with various
tasks and different completion statuses. Validates the accuracy of completed tasks recorded in
the history manager.

Each test case contains detailed steps:
    - Sets up necessary instances and objects.
    - Creates projects, tasks, and sets task completion statuses.
    - Adds tasks to projects and projects to the history manager.
    - Verifies the presence or absence of completed tasks in the history manager based on the
expected completion status.

Usage:
    Run this module to execute the test suite for the 'History' module.
"""

import unittest
from datetime import datetime
from src import HistorySingleton
from src import Project
from src import Task
from src import User


class TestHistory(unittest.TestCase):
    """ This class will be used to test the history module.

    Args:
        unittest (TestCase): Inherits from TestCase in the unittest module.
    """
    def setUp(self) -> None:
        """ This method will be used to initialize the history module.
        """
        self.history_manager = HistorySingleton()

    def test_access_singleton_instance(self) -> None:
        """ This method will be used to test the access of the singleton instance.
        """
        self.assertEqual(self.history_manager, HistorySingleton())

    def test_access_project_list(self) -> None:
        """ This method will be used to test the access of the project list.
        """
        # initialize user and project
        test_user = User("username")
        project1 = Project(test_user,"test_project","test_label",datetime.now(),"test_description")

        # initialize the tasks
        task1 = Task(project1, "Task 1", "high", datetime.now(), datetime.now(), "description1")

        # add the tasks to the project
        project1.add_task(task1)

        # update the status of the task
        project1.tasks[0].update(status=True)

        # test the addition of a completed task to the list
        list_of_projects = [project1]
        self.history_manager.add_completed_task(list_of_projects)
        self.assertEqual(self.history_manager.tasks_completed(), list_of_projects[0].tasks)

    def test_new_add_completed_task_one_project(self) -> None:
        """ This method will be used to test the addition of a completed task to the list.
        It simulates the creation of a project and the addition of a set of completed tasks
        to the list.
        """
        # initialize the user and project
        test_user = User("username")
        project1 = Project(test_user,"test_project","test_label",datetime.now(),"test_description")

        # initialize the tasks
        task1 = Task(project1, "Task 1", "high", datetime.now(), datetime.now(), "description1")
        task2 = Task(project1, "Task 2", "high", datetime.now(), datetime.now(), "description2")

        # add the tasks to the project
        project1.add_task(task1)
        project1.add_task(task2)

        # update the status of the task
        project1.tasks[0].update(status=True)

        # test the addition of a completed task to the list
        list_of_projects = [project1]
        self.history_manager.add_completed_task(list_of_projects)
        self.assertIn(project1.tasks[0], self.history_manager.tasks_completed())
        self.assertNotIn(project1.tasks[1], self.history_manager.tasks_completed())

    def test_add_completed_task_multiple_projects(self) -> None:
        """ This method will be used to test the addition of a completed task to the list.
        It simulates the creation of multiple projects and the addition of a set of completed
        tasks to the list.
        """
        # initialize the projects
        test_user = User("username")
        project1 = Project(test_user,"test_project","test_label",datetime.now(),"test_description")
        project2 = Project(test_user,"test_project","test_label",datetime.now(),"test_description")

        # initialize the tasks
        task1 = Task(project1, "Task 1", "high", datetime.now(), datetime.now(), "description1")
        task2 = Task(project2, "Task 2", "high", datetime.now(), datetime.now(), "description2")
        task3 = Task(project1, "Task 3", "low", datetime.now(), datetime.now(), "description3")
        task4 = Task(project2, "Task 4", "low", datetime.now(), datetime.now(), "description4")

        # add the tasks to project1
        project1.add_task(task1)
        project1.add_task(task3)

        # add the tasks to project2
        project2.add_task(task2)
        project2.add_task(task4)

        # update the status of some tasks
        project1.tasks[0].update(status=True)
        project2.tasks[1].update(status=True)

        # test the addition of a completed task to the list
        list_of_projects = [project1, project2]
        self.history_manager.add_completed_task(list_of_projects)
        self.assertIn(project1.tasks[0], self.history_manager.tasks_completed())
        self.assertIn(project2.tasks[1], self.history_manager.tasks_completed())
        self.assertNotIn(project1.tasks[1], self.history_manager.tasks_completed())
        self.assertNotIn(project2.tasks[0], self.history_manager.tasks_completed())


if __name__ == "__main__":
    unittest.main()
