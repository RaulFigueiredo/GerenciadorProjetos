import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch, Mock
from src.logic.history.task_history import HistorySingleton
from src.logic.users.user import User
from src.gui.history_page import HistoryManagerApp
import unittest
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty
from sqlalchemy.orm import sessionmaker
from src.logic.orms.orm import UserORM,SubtaskORM, Base, ProjectORM, TaskORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

class TestHistoryManagerApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = cls.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

    def setUp(self):
        self.root = tk.Tk()
        with patch.object(User, 'seve_to_db') as mock_save:
            self.user = User("username", self.SessionLocal())

        self.controller_mock = Mock()
        self.on_close_mock = Mock()
        self.app = HistoryManagerApp(self.root, self.controller_mock, self.on_close_mock, self.user)

    def test_initialization(self):
        """ Tests whether the HistoryManagerApp class is initialized correctly """
        self.assertIsInstance(self.app, HistoryManagerApp)
        self.assertEqual(self.app.user, self.user)
        self.assertIsInstance(self.app.history, HistorySingleton)

    def test_get_task_info(self):
        """ Tests whether the get_task_info method returns the correct information """
        fake_task = Mock()
        fake_task.project.name = "Projeto Exemplo"
        fake_task.name = "Tarefa Exemplo"
        fake_task.conclusion_date = date(2021, 3, 3)

        result = self.app.get_task_info(fake_task)
        expected_result = {
            "key": "Projeto Exemplo",
            "value": "Tarefa Exemplo",
            "date": "03/03/2021"
        }
        self.assertEqual(result, expected_result)


    def test_go_back(self):
        """ Testa se o método go_back chama controller.deiconify """
        self.app.controller.deiconify = Mock()
        self.app.go_back()
        self.app.controller.deiconify.assert_called_once()


    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()