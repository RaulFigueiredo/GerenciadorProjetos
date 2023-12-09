"""
    This module contains unit tests for the Notification class,
validating its functionality in managing and notifying users about task-related events.

    The TestNotification class within this module extends the unittest.
TestCase class to perform various test cases.

Test Cases:
    - test_check_notification_date(): 
Checks if tasks with the current day's notification date are correctly added to
 the notification_date_tasks set.

    - test_check_due_date_urgent():
Tests the classification of tasks with urgent priority due the next day, ensuring
 they are added to the urgent_tasks set.

    - test_check_due_date_today():
Verifies if tasks due on the current day are added to the due_date_tasks set as expected.

    - test_check_due_date_passed():
Validates the handling of tasks overdue before the current day, ensuring they are added
 to the due_date_tasks set appropriately.

Each test method simulates different scenarios for task due dates, priorities, and notification
 dates, assessing the correct categorization of tasks by the Notification class.

These tests validate the behavior of the Notification class under various conditions to ensure
 its functionality aligns with expected behaviors.

"""

import unittest
import datetime
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.notifications.notification import Notification

class TestNotification(unittest.TestCase):
    """ This class will be used to test the notification class

    Args:
        unittest (unittest.TestCase): This class will be used to test the notification class
    """
    def setUp(self):
        """ This method will be used to set up the notification test
        """
        self.user = User(name='test_user')
        self.project = Project(self.user, name='test_project')
        self.task = Task(self.project, name='test_task1')
        self.today = datetime.date.today()
        self.notification = Notification(self.user)

    def test_check_notification_date(self):
        """ This method will be used to check the notification date of the tasks
        """
        self.task.update(notification_date=self.today)
        self.notification.check_notification_date()
        self.assertIn(self.task, self.notification.notification_date_tasks)

    def test_check_due_date_urgent(self):
        """ This method will be used to check the due date of the tasks,
        considering the priority of the task
        """
        self.task.update(end_date=self.today + datetime.timedelta(days=1), priority='Urgente')
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.urgent_tasks)
        self.assertNotIn(self.task, self.notification.due_date_tasks)

    def test_check_due_date_today(self):
        """ This method will be used to check the due date of the tasks,
        considering today's date
        """
        self.task.update(end_date=self.today)
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.due_date_tasks)
        self.assertNotIn(self.task, self.notification.urgent_tasks)

    def test_check_due_date_passed(self):
        """ This method will be used to check the due date of the tasks,
        considering a previous date
        """
        self.task.update(end_date=self.today - datetime.timedelta(days=1))
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.due_date_tasks)
        self.assertNotIn(self.task, self.notification.urgent_tasks)

if __name__ == '__main__':
    unittest.main()
