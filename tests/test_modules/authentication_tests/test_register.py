"""
This module contains unit tests for the RegisterLogic class in the authentication logic of the application. These tests are designed to ensure that the registration functionality works correctly, handling both successful and failed registration attempts.

The tests simulate scenarios such as successful user registration with new credentials and failed registration attempts when a user with the given username already exists.

Classes:
- TestRegisterLogic: Contains test cases for the RegisterLogic class.

Methods:
- test_register_successful: Tests successful user registration with unique credentials.
- test_register_failed_user_exists: Tests failed user registration when a user with the provided username already exists.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.logic.authentication.authentication import RegisterLogic

class TestRegisterLogic(unittest.TestCase):
    """
    Test cases for the RegisterLogic class.

    This class tests the registration functionality provided by the RegisterLogic class, ensuring both successful registration with unique credentials and handling of failed registration attempts due to existing usernames.
    """
    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_register_successful(self, mock_session):
        """
        Tests successful user registration with unique credentials.

        This test ensures that the register method returns a valid user object when provided with unique username, password, and email, indicating a successful registration.
        """
        # Setup mock session for successful registration scenario
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None

        result = RegisterLogic.register('new_user', 'new_password', 'email@example.com')
        self.assertIsNotNone(result)

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_register_failed_user_exists(self, mock_session):
        """
        Tests failed user registration when a user with the provided username already exists.

        This test ensures that the register method returns None when attempting to register with a username that already exists in the database, indicating a failed registration attempt.
        """
        # Setup mock session for user already exists scenario
        existing_user_mock = MagicMock()
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = existing_user_mock

        result = RegisterLogic.register('existing_user', 'password123', 'email@example.com')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
