import unittest
from datetime import date
from src import Project, Label
from src.logic.filter.filter import Filter
from src.logic.authentication.authentication import LoginLogic


class TestFilterMethods(unittest.TestCase):
    user = LoginLogic.login('John Doe', 'pwd123')

    def setUp(self):
        self.filter = Filter(self.user)

    def test_filter_project_by_name(self):
        result = self.filter.filter_project_by_name(self.user.projects[0].name)
        self.assertIsInstance(result, Project)
        self.assertEqual(result.name, self.user.projects[0].name)

    def test_filter_projects_by_creation_date(self):
        lower_limit = date(2023, 1, 1)
        upper_limit = date(2023, 2, 1)
        result = self.filter.filter_projects_by_creation_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.creation_date >= lower_limit
                                   and project.creation_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_end_date(self):
        lower_limit = date(2023, 2, 1)
        upper_limit = date(2023, 3, 1)
        result = self.filter.filter_projects_by_end_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.end_date >= lower_limit
                                   and project.end_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_conclusion_date(self):
        lower_limit = date(2023, 2, 15)
        upper_limit = date(2023, 3, 15)
        result = self.filter.filter_projects_by_conclusion_date(lower_limit, upper_limit)
        self.assertIsInstance(result, list)
        inside_interval = []
        for project in result:
            inside_interval.append(project.conclusion_date >= lower_limit
                                   and project.conclusion_date <= upper_limit)
        self.assertTrue(all(inside_interval))

    def test_filter_projects_by_status(self):
        result = self.filter.filter_projects_by_status(True)
        self.assertIsInstance(result, list)
        self.assertTrue(all(list(map(lambda x: x.status, result))))

    def test_filter_labels_by_name(self):
        result = self.filter.filter_label_by_name(self.user.labels[0].name)
        self.assertIsInstance(result, Label)
        self.assertEqual(result.name, self.user.labels[0].name)


if __name__ == '__main__':
    unittest.main()
