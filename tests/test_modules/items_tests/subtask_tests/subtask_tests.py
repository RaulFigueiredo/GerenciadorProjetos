import unittest
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty
from sqlalchemy.orm import sessionmaker
from src.logic.orms.orm import UserORM,SubtaskORM, Base, ProjectORM, TaskORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

class TestSubtask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = TestSubtask.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        db_test_project = ProjectORM(name='Test Project', id_user=db_test_user.id_user, status=False, creation_date=date(2021, 1, 1))
        cls.session.add(db_test_project)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
        cls.test_project = Project(name=db_test_project.name, user=cls.test_user, id_project=db_test_project.id_project,status=db_test_project.status, creation_date=db_test_project.creation_date, session = cls.session)
    
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = TestSubtask.SessionLocal()
        self.create_test_items()

    def create_test_items(self):
        db_test_task = TaskORM(name='Test Task', id_project=self.test_project.id_project, status=False, creation_date=date(2021, 1, 1)) 
        self.session.add(db_test_task)
        self.session.commit()

        db_test_subtask = SubtaskORM(name='Test Subtask', id_task=db_test_task.id_task, status=False)
        self.session.add(db_test_subtask)
        self.session.commit()

        self.test_task = Task(name=db_test_task.name, project=self.test_project, id_task=db_test_task.id_task, status=db_test_task.status, creation_date=db_test_task.creation_date, session = self.session)
        self.test_subtask = Subtask(name=db_test_subtask.name, task=self.test_task, id_subtask=db_test_subtask.id_subtask, status=db_test_subtask.status, session = self.session)

    def tearDown(self):
        self.session.close()

    def test_initialization(self):
        subtask = Subtask(task=self.test_task, name="Test Subtask")

        self.assertEqual(subtask._task, self.test_task)
        self.assertEqual(subtask._name, "Test Subtask")
        self.assertFalse(subtask._status)
        self.assertIsNone(subtask._conclusion_date)
        self.assertIsInstance(subtask._mementos, list)

    def test_save_to_db(self):
        new_subtask = Subtask(task=self.test_task, name="New Subtask", session=self.session)

        with self.session as session:
            saved_subtask = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == new_subtask._id_subtask).first()
            self.assertIsNotNone(saved_subtask)
            self.assertEqual(saved_subtask.name, "New Subtask")
            self.assertEqual(saved_subtask.id_task, self.test_task.id_task)

    def test_delete(self):
        new_subtask = Subtask(task=self.test_task, name="Delete Test Subtask")
        new_subtask.save_to_db()

        new_subtask.delete()

        with self.session as session:
            deleted_subtask = session.query(SubtaskORM).filter(SubtaskORM.name == "Delete Test Subtask").first()
            self.assertIsNone(deleted_subtask)

    def test_update(self):
        new_subtask = Subtask(task=self.test_task, name="Update Test Subtask",session=self.session)
        new_subtask.save_to_db()

        new_name = "Updated Subtask"
        new_subtask.update(name=new_name)

        self.assertEqual(new_subtask._name, new_name)

        with self.session as session:
            updated_subtask = session.query(SubtaskORM).filter(SubtaskORM.id_subtask == new_subtask._id_subtask).first()
            self.assertIsNotNone(updated_subtask)
            self.assertEqual(updated_subtask.name, new_name)

    def test_conclusion_unconclusion(self):
        self.assertFalse(self.test_subtask._status)
        self.assertIsNone(self.test_subtask._conclusion_date)

        self.test_subtask.conclusion()
        self.assertTrue(self.test_subtask._status)
        self.assertEqual(self.test_subtask._conclusion_date, date.today())

        self.test_subtask.unconclusion()
        self.assertFalse(self.test_subtask._status)
        self.assertIsNone(self.test_subtask._conclusion_date)
            
    def test_save_restore_memento(self):
        self.test_subtask.save_to_memento()
        self.assertEqual(len(self.test_subtask._mementos), 1)

        self.test_subtask.update(name="Modified Subtask")
        self.assertEqual(len(self.test_subtask._mementos), 2)

        self.test_subtask.restore_from_memento()
        self.assertEqual(self.test_subtask._name, "Test Subtask")
        self.assertEqual(len(self.test_subtask._mementos), 1)

    def test_unique_name_constraint_on_update(self):
        another_subtask = Subtask(task=self.test_task, name="Another Subtask", session=self.session)
        another_subtask.save_to_db()

        with self.assertRaises(ItemNameAlreadyExists):
            self.test_subtask.update(name="Another Subtask")
    
    def test_name_validation_on_update(self):
        with self.assertRaises(ItemNameBlank):
            self.test_subtask.update(name="")

        with self.assertRaises(ItemNameBlank):
            self.test_subtask.update(name=None)

    def test_task_change_restriction(self):
        new_task = Task(name="New Test Task", project=self.test_project, session=self.session)

        with self.assertRaises(NonChangeableProperty):
            self.test_subtask.update(task=new_task)

    def test_initialization_with_without_session(self):
        subtask_with_session = Subtask(task=self.test_task, name="Subtask with Session", session=self.session)
        self.assertIsNotNone(subtask_with_session.SessionLocal)

        subtask_without_session = Subtask(task=self.test_task, name="Subtask without Session")
        self.assertIsNotNone(subtask_without_session.SessionLocal)


if __name__ == "__main__":
    unittest.main()