"""
This module contains unit tests for the LoginLogic class in the authentication logic of the application. The tests verify the login functionality using the unittest framework.

The module aims to ensure that the LoginLogic class correctly handles user authentication, including successful login attempts with correct credentials and failed login attempts with incorrect credentials.

Classes:
- TestLoginLogic: Contains test cases for the LoginLogic class.

Methods:
- test_login_successful: Tests successful user login with correct credentials.
- test_login_failed: Tests failed user login with incorrect credentials.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.logic.authentication.authentication import LoginLogic

class TestLoginLogic(unittest.TestCase):
    """
    Test cases for the LoginLogic class.

    This class tests the login functionality provided by the LoginLogic class, verifying both successful and failed login attempts.
    """

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_login_successful(self, mock_session):
        """
        Tests successful user login with correct credentials.

        This test ensures that the login method returns a valid user object when provided with correct username and password.
        """
        # Setup mock session and query
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(name='test_user', password='password123')

        result = LoginLogic.login('test_user', 'password123')
        self.assertIsNotNone(result)

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_login_failed(self, mock_session):
        """
        Tests failed user login with incorrect credentials.

        This test ensures that the login method returns None when provided with incorrect username and password, indicating a failed login attempt.
        """

        # Setup mock session and query
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None

        result = LoginLogic.login('wrong_user', 'wrong_password')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
