import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from src.gui.authentication import Authentication

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        # Create a mock user object
        self.mock_user = MagicMock()
        self.mock_user.projects = []
        self.auth = Authentication(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('src.logic.authentication.authentication.LoginLogic.login')
    def test_login_user_success(self, mock_login):
        # Set the mock to return the mock user object on successful login
        mock_login.return_value = self.mock_user

        result = self.auth.login_user("test_user", "test_password")
        self.assertTrue(result)
        self.assertIsNotNone(self.auth.user)

    @patch('src.logic.authentication.authentication.LoginLogic.login')
    def test_login_user_fail(self, mock_login):
        # Set the mock to return False on failed login
        mock_login.return_value = False

        result = self.auth.login_user("test_user", "wrong_password")
        self.assertFalse(result)
        self.assertIsNone(self.auth.user)
        # Verify that the status label is updated correctly
        self.assertEqual(self.auth.login_frame.status_label.cget("text"), "Login failed")

    @patch('src.logic.authentication.authentication.RegisterLogic.register')
    def test_register_user_success(self, mock_register):
        # Set the mock to return the mock user object on successful registration
        mock_register.return_value = self.mock_user

        result = self.auth.register_user("new_user", "new_password", "email@example.com")
        self.assertTrue(result)
        self.assertIsNotNone(self.auth.user)

    @patch('src.logic.authentication.authentication.RegisterLogic.register')
    def test_register_user_fail(self, mock_register):
        # Set the mock to return False on failed registration
        mock_register.return_value = False

        result = self.auth.register_user("existing_user", "password", "email@example.com")
        self.assertFalse(result)
        self.assertIsNone(self.auth.user)
        # Verify that the status label is updated correctly
        self.assertEqual(self.auth.register_frame.status_label.cget("text"), "Registration failed")

if __name__ == '__main__':
    unittest.main()
