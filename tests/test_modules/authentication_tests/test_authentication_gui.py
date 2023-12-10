"""
This module contains unit tests for the Authentication class in a tkinter-based GUI application. It uses the unittest framework and patches external dependencies to test the functionality of user login and registration processes.

Classes:
- TestAuthentication: Contains test cases for the Authentication class.

Test cases in this module focus on verifying the success and failure scenarios of user authentication (login and registration). They use mocking to simulate interactions with the backend logic and ensure the GUI behaves as expected under different circumstances.

Methods:
- setUp: Prepares the test environment before each test.
- tearDown: Cleans up after each test.
- test_login_user_success: Tests successful user login.
- test_login_user_fail: Tests unsuccessful user login.
- test_register_user_success: Tests successful user registration.
- test_register_user_fail: Tests unsuccessful user registration.
"""

import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from src.gui.authentication import Authentication

class TestAuthentication(unittest.TestCase):
    """
    Test cases for the Authentication class.

    This class contains methods to test both login and registration functionalities in the authentication module. It sets up a tkinter root and mock user object for each test.
    """

    def setUp(self):
        """
        Prepares the test environment before each test.

        Initializes the tkinter root and creates a mock user object. It also instantiates the Authentication class for testing.
        """
        self.root = Tk()
        # Create a mock user object
        self.mock_user = MagicMock()
        self.mock_user.projects = []
        self.auth = Authentication(self.root)

    def tearDown(self):
        """
        Cleans up the test environment after each test.

        Destroys the tkinter root to ensure a clean state for the next test.
        """
        self.root.destroy()

    @patch('src.logic.authentication.authentication.LoginLogic.login')
    def test_login_user_success(self, mock_login):
        """
        Tests successful user login.

        Mocks the backend login logic to simulate a successful login and verifies that the user is correctly set in the Authentication class.
        """
        # Set the mock to return the mock user object on successful login
        mock_login.return_value = self.mock_user

        result = self.auth.login_user("test_user", "test_password")
        self.assertTrue(result)
        self.assertIsNotNone(self.auth.user)

    @patch('src.logic.authentication.authentication.LoginLogic.login')
    def test_login_user_fail(self, mock_login):
        """
        Tests unsuccessful user login.

        Mocks the backend login logic to simulate a failed login and verifies that the user is not set and the correct error message is displayed.
        """
        # Set the mock to return False on failed login
        mock_login.return_value = False

        result = self.auth.login_user("test_user", "wrong_password")
        self.assertFalse(result)
        self.assertIsNone(self.auth.user)
        # Verify that the status label is updated correctly
        self.assertEqual(self.auth.login_frame.status_label.cget("text"), "Login failed")

    @patch('src.logic.authentication.authentication.RegisterLogic.register')
    def test_register_user_success(self, mock_register):
        """
        Tests successful user registration.

        Mocks the backend registration logic to simulate a successful registration and verifies that the user is correctly set in the Authentication class.
        """
        # Set the mock to return the mock user object on successful registration
        mock_register.return_value = self.mock_user

        result = self.auth.register_user("new_user", "new_password", "email@example.com")
        self.assertTrue(result)
        self.assertIsNotNone(self.auth.user)

    @patch('src.logic.authentication.authentication.RegisterLogic.register')
    def test_register_user_fail(self, mock_register):
        """
        Tests unsuccessful user registration.

        Mocks the backend registration logic to simulate a failed registration and verifies that the user is not set and the correct error message is displayed.
        """

        # Set the mock to return False on failed registration
        mock_register.return_value = False

        result = self.auth.register_user("existing_user", "password", "email@example.com")
        self.assertFalse(result)
        self.assertIsNone(self.auth.user)
        # Verify that the status label is updated correctly
        self.assertEqual(self.auth.register_frame.status_label.cget("text"), "Registration failed")

if __name__ == '__main__':
    unittest.main()
