import unittest
from unittest.mock import patch, MagicMock
from src.logic.authentication.authentication import LoginLogic

class TestLoginLogic(unittest.TestCase):

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_login_successful(self, mock_session):
        # Setup mock session and query
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(name='test_user', password='password123')

        result = LoginLogic.login('test_user', 'password123')
        self.assertIsNotNone(result)

    @patch('src.logic.authentication.authentication.SessionLocal')
    def test_login_failed(self, mock_session):
        # Setup mock session and query
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = None

        result = LoginLogic.login('wrong_user', 'wrong_password')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
