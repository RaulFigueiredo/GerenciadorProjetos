import unittest
from unittest.mock import patch, MagicMock
from src.logic.authentication.authentication import RegisterLogic

class TestRegisterLogic(unittest.TestCase):

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_register_successful(self, mock_session):
        # Setup mock session for successful registration scenario
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None

        result = RegisterLogic.register('new_user', 'new_password', 'email@example.com')
        self.assertIsNotNone(result)

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_register_failed_user_exists(self, mock_session):
        # Setup mock session for user already exists scenario
        existing_user_mock = MagicMock()
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = existing_user_mock

        result = RegisterLogic.register('existing_user', 'password123', 'email@example.com')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
