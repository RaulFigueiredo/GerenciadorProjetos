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

if __name__ == '__main__':
    unittest.main()
