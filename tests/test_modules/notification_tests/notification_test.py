"""
    Test module for notification class.
"""

import unittest
import datetime
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.notifications.notification import Notification

class TestNotification(unittest.TestCase):
    def setUp(self):
        self.user = User(name='test_user')
        self.project = Project(self.user, name='test_project')
        self.task = Task(self.project, name='test_task1')
        self.today = datetime.date.today()
        self.notification = Notification(self.user)

    def test_check_notification_date(self):
        self.task.update(notification_date=self.today)
        self.notification.check_notification_date()
        self.assertIn(self.task, self.notification.notification_date_tasks)

    def test_check_due_date_urgent(self):
        self.task.update(end_date=self.today + datetime.timedelta(days=1), priority='Urgente')
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.urgent_tasks)
        self.assertNotIn(self.task, self.notification.due_date_tasks)

    def test_check_due_date_today(self):
        self.task.update(end_date=self.today)
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.due_date_tasks)
        self.assertNotIn(self.task, self.notification.urgent_tasks)

    def test_check_due_date_passed(self):
        self.task.update(end_date=self.today - datetime.timedelta(days=1))
        self.notification.check_due_date()
        self.assertIn(self.task, self.notification.due_date_tasks)
        self.assertNotIn(self.task, self.notification.urgent_tasks)

if __name__ == '__main__':
    unittest.main()
