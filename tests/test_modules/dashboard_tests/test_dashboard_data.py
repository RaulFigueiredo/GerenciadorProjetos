import unittest
import datetime
from src.logic.authentication.authentication import LoginLogic
from src.logic.dashboard.dashboard_data import DashboardData


class TestDashboardDataComponents(unittest.TestCase):
    user = LoginLogic.login('John Doe', 'pwd123')
    
    def setUp(self):
        self.dashboard_data = DashboardData(self.user)

    def test_update_data(self):
        self.dashboard_data.update_data("Project 1")
        self.assertLessEqual(len(self.dashboard_data.projects), 1)

    def test_get_number_of_tasks(self):
        tasks = []
        for project in self.dashboard_data.projects:
            tasks += [task for task in project.tasks]
        self.assertEqual(self.dashboard_data.get_number_of_tasks(), len(tasks))
    
    def test_get_number_of_done_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_number_of_done_tasks(), int)

    def test_get_number_of_on_time_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_number_of_on_time_tasks(), int)

    def get_number_of_for_today_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_number_of_for_today_tasks(), int)

    def test_get_number_of_late_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_number_of_late_tasks(), int)

    def test_get_timespan_of_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_timespan_of_tasks(), dict)

    def test_get_next_deadlines(self):
        self.assertIsInstance(self.dashboard_data.get_next_deadlines(), dict)
    
    def test_get_created_tasks(self):
        self.assertIsInstance(self.dashboard_data.get_created_tasks(), dict)
    
    def test_get_finished_by_weekday(self):
        self.assertIsInstance(self.dashboard_data.get_finished_by_weekday(), dict)


if __name__ == '__main__':
    unittest.main()
