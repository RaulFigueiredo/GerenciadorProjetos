"""
This module contains unit tests for the instance_user function in the authentication logic of a GUI application. The tests are built using the unittest framework.

The module focuses on testing the functionality that creates a user instance from a database user object. It ensures that the user instance is created correctly with the appropriate attributes.

Classes:
- TestInstanceUser: Contains test cases for the instance_user function.

Methods:
- test_instance_user: Verifies that a user instance is correctly created from a database user object.
"""

import unittest
from unittest.mock import Mock
from src.logic.authentication.authentication import instance_user

class TestInstanceUser(unittest.TestCase):
    """
    Test cases for the instance_user function.

    This class tests the instance_user function, which is responsible for creating a user instance from a database user object.
    """
    def test_instance_user(self):
        """
        Tests the creation of a user instance from a database user object.

        This test ensures that the user instance is created with the correct attributes matching those of the database user object.
        """
        db_user = Mock()
        db_user.name = 'test_user'
        db_user.projects = []
        db_user.labels = []

        user = instance_user(db_user)
        self.assertEqual(user.name, 'test_user')

if __name__ == '__main__':
    unittest.main()
