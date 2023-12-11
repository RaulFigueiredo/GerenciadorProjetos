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
from src import HistorySingleton, Project, Task, User
import unittest
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty, HistorySingleton
from sqlalchemy.orm import sessionmaker
from src.logic.orms.orm import UserORM,SubtaskORM, Base, ProjectORM, TaskORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

class TestHistorySingleton(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = cls.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        db_test_project = ProjectORM(name='Test Project', id_user=db_test_user.id_user, status=False, creation_date=datetime.now())
        cls.session.add(db_test_project)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
        cls.test_project = Project(name=db_test_project.name, user=cls.test_user, id_project=db_test_project.id_project, status=db_test_project.status, creation_date=db_test_project.creation_date, session=cls.session)

    def setUp(self):
        self.history_manager = HistorySingleton()

    def test_access_singleton_instance(self):
        self.assertIs(self.history_manager, HistorySingleton())

    def test_add_and_retrieve_completed_tasks(self):
        test_user = User("username")
        project1 = Project(test_user, "test_project", "test_label", datetime.now(), "test_description")
        task1 = Task(project1, "Task 1", "high", datetime.now(), datetime.now(), "description1", status=True)
        task2 = Task(project1, "Task 2", "high", datetime.now(), datetime.now(), "description2", status=False)
        project1.add_task(task1)
        project1.add_task(task2)

        self.history_manager.add_completed_task([project1])
        completed_tasks = self.history_manager.tasks_completed()

        self.assertIn(task1, completed_tasks)
        self.assertNotIn(task2, completed_tasks)

    def test_add_multiple_projects_with_mixed_tasks(self):
        project1 = Project(self.test_user, "project1", "label1", datetime.now(), "description1")
        project2 = Project(self.test_user, "project2", "label2", datetime.now(), "description2")
        task1 = Task(project1, "Task 1", "high", datetime.now(), datetime.now(), "description1", status=True)
        task2 = Task(project1, "Task 2", "medium", datetime.now(), datetime.now(), "description2", status=False)
        task3 = Task(project2, "Task 3", "low", datetime.now(), datetime.now(), "description3", status=True)
        task4 = Task(project2, "Task 4", "medium", datetime.now(), datetime.now(), "description4", status=False)

        project1.add_task(task1)
        project1.add_task(task2)
        project2.add_task(task3)
        project2.add_task(task4)

        self.history_manager.add_completed_task([project1, project2])
        completed_tasks = self.history_manager.tasks_completed()

        self.assertIn(task1, completed_tasks)
        self.assertIn(task3, completed_tasks)
        self.assertNotIn(task2, completed_tasks)
        self.assertNotIn(task4, completed_tasks)

    def test_add_project_without_completed_tasks(self):
        project = Project(self.test_user, "project", "label", datetime.now(), "description")
        task = Task(project, "Task", "high", datetime.now(), datetime.now(), "description", status=False)
        project.add_task(task)

        self.history_manager.add_completed_task([project])
        completed_tasks = self.history_manager.tasks_completed()

        self.assertNotIn(task, completed_tasks)

    def test_add_project_with_duplicate_tasks(self):
        project = Project(self.test_user, "project", "label", datetime.now(), "description")
        task = Task(project, "Task", "high", datetime.now(), datetime.now(), "description", status=True)
        project.add_task(task)
        project.add_task(task)

        self.history_manager.add_completed_task([project])
        completed_tasks = self.history_manager.tasks_completed()

        self.assertEqual(len(completed_tasks), 4)
        self.assertIn(task, completed_tasks)

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

if __name__ == "__main__":
    unittest.main()