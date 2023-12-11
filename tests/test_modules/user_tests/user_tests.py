import unittest
from unittest.mock import Mock
from datetime import date
from src import Subtask,User,Project,Task,Subtask, Label
from src.logic.orms.orm import UserORM, Base, ProjectORM, TaskORM,SubtaskORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class UserTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = UserTask.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
    
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = UserTask.SessionLocal()

    def tearDown(self):
        self.session.close()

    def test_initialization(self):
        self.assertEqual(self.test_user.name, "Test User")
        self.assertEqual(self.test_user.labels, [])
        self.assertEqual(self.test_user.projects, [])

    def test_add_label(self):
        label = Label(user = self.test_user, name = "Test Label", color="azul",session=self.session)
        self.assertEqual(self.test_user.labels, [label])
        self.test_user.remove_label(label)

    def test_add_two_labels(self):
        mock_label1 = Label(user = self.test_user, name = "Test Label 1", color="azul",session=self.session)
        mock_label2 = Label(user = self.test_user, name = "Test Label 2", color="azul",session=self.session)
        self.assertEqual(self.test_user.labels, [mock_label2, mock_label1])
        self.test_user.remove_label(mock_label1)
        self.test_user.remove_label(mock_label2)

    def test_remove_label(self):
        mock_label = Label(user = self.test_user, name = "Test Label", color="azul",session=self.session)
        self.test_user.remove_label(mock_label)
        self.assertEqual(self.test_user.labels, [])

    def test_remove_two_labels(self):
        mock_label1 = Label(user = self.test_user, name = "Test Label 1", color="azul",session=self.session)
        mock_label2 = Label(user = self.test_user, name = "Test Label 2", color="azul",session=self.session)
        self.test_user.remove_label(mock_label1)
        self.test_user.remove_label(mock_label2)
        self.assertEqual(self.test_user.labels, [])

    def test_add_project(self):
        project = Project(user = self.test_user, name = "Test project",session=self.session)
        self.assertEqual(self.test_user.projects, [project])
        self.test_user.remove_project(project)

    def test_add_two_projects(self):
        mock_project1 = Project(user = self.test_user, name = "Test project 1", session=self.session)
        mock_project2 = Project(user = self.test_user, name = "Test project 2", session=self.session)
        self.assertEqual(self.test_user.projects, [mock_project2, mock_project1])
        self.test_user.remove_project(mock_project1)
        self.test_user.remove_project(mock_project2)


    def test_remove_project(self):
        mock_project = Project(user = self.test_user, name = "Test project", session=self.session)
        self.test_user.remove_project(mock_project)
        self.assertEqual(self.test_user.projects, [])

    def test_remove_two_projects(self):
        mock_project1 = Project(user = self.test_user, name = "Test project 1", session=self.session)
        mock_project2 = Project(user = self.test_user, name = "Test project 2", session=self.session)
        self.assertEqual(self.test_user.projects, [mock_project2, mock_project1])
        self.test_user.remove_project(mock_project1)
        self.test_user.remove_project(mock_project2)

    def test_singleton_instance(self):
        User._instance = None
        user1 = User(name = "Primeiro Usuário", id_user=2, session=self.session)
        user2 = User(name = "Segundo Usuário", id_user=3, session=self.session)

        self.assertIs(user1, user2)
        self.assertEqual(user1.name, user2.name)


if __name__ == '__main__':
    unittest.main()