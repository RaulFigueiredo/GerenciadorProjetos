import unittest
from unittest.mock import Mock
from src.logic.authentication.authentication import instance_user

class TestInstanceUser(unittest.TestCase):

    def test_instance_user(self):
        db_user = Mock()
        db_user.name = 'test_user'
        db_user.projects = []
        db_user.labels = []

        user = instance_user(db_user)
        self.assertEqual(user.name, 'test_user')

if __name__ == '__main__':
    unittest.main()
