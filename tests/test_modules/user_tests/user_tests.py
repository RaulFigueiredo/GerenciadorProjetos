import unittest
from unittest.mock import Mock
from src import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Test User")

    def test_initialization(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.labels, [])
        self.assertEqual(self.user.projects, [])

    def test_add_label(self):
        mock_label = Mock()
        self.user.add_label(mock_label)
        self.assertEqual(self.user.labels, [mock_label])

    def test_add_two_labels(self):
        mock_label1 = Mock()
        mock_label2 = Mock()
        self.user.add_label(mock_label1)
        self.user.add_label(mock_label2)
        self.assertEqual(self.user.labels, [mock_label1, mock_label2])

    def test_remove_label(self):
        mock_label = Mock()
        self.user.add_label(mock_label)
        self.user.remove_label(mock_label)
        self.assertEqual(self.user.labels, [])

    def test_remove_two_labels(self):
        mock_label1 = Mock()
        mock_label2 = Mock()
        self.user.add_label(mock_label1)
        self.user.add_label(mock_label2)
        self.user.remove_label(mock_label1)
        self.user.remove_label(mock_label2)
        self.assertEqual(self.user.labels, [])

    def test_add_project(self):
        mock_project = Mock()
        self.user.add_project(mock_project)
        self.assertEqual(self.user.projects, [mock_project])

    def test_add_two_projects(self):
        mock_project1 = Mock()
        mock_project2 = Mock()
        self.user.add_project(mock_project1)
        self.user.add_project(mock_project2)
        self.assertEqual(self.user.projects, [mock_project1, mock_project2])


    def test_remove_project(self):
        mock_project = Mock()
        self.user.add_project(mock_project)
        self.user.remove_project(mock_project)
        self.assertEqual(self.user.projects, [])

    def test_remove_two_projects(self):
        mock_project1 = Mock()
        mock_project2 = Mock()
        self.user.add_project(mock_project1)
        self.user.add_project(mock_project2)
        self.user.remove_project(mock_project1)
        self.user.remove_project(mock_project2)
        self.assertEqual(self.user.projects, [])

if __name__ == '__main__':
    unittest.main()