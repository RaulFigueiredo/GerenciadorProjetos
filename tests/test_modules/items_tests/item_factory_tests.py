import unittest
from unittest.mock import Mock
from datetime import date
from src import Project, ItemDontHaveThisAttribute, NonChangeableProperty
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty
from src.logic.orms.orm import UserORM, Base, ProjectORM, TaskORM,SubtaskORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src import ItemFactory, ItemNameBlank, ItemNameAlreadyExists, UnknownItem

class TestItemFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = TestItemFactory.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
    
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = TestItemFactory.SessionLocal()
        self.create_test_items()

    def create_test_items(self):
        db_test_project = ProjectORM(name='Test Project', id_user=self.test_user.id_user, status=False, creation_date=date.today())
        self.session.add(db_test_project)
        self.session.commit()
        self.test_project = Project(name=db_test_project.name, user=self.test_user, id_project=db_test_project.id_project,status=db_test_project.status, creation_date=db_test_project.creation_date, session = self.session)
    
        db_test_task = TaskORM(name='Test Task', id_project=self.test_project.id_project, status=False, creation_date=date.today()) 
        self.session.add(db_test_task)
        self.session.commit()

        db_test_subtask = SubtaskORM(name='Test Subtask', id_task=db_test_task.id_task, status=False)
        self.session.add(db_test_subtask)
        self.session.commit()

        self.test_task = Task(name=db_test_task.name, project=self.test_project, id_task=db_test_task.id_task, status=db_test_task.status, creation_date=db_test_task.creation_date, session = self.session)
        self.test_subtask = Subtask(name=db_test_subtask.name, task=self.test_task, id_subtask=db_test_subtask.id_subtask, status=db_test_subtask.status, session = self.session)

    def tearDown(self):
        self.session.close()

    def test_create_item_with_blank_name(self):
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('project', name='')
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('subtask', name='')
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('task', name='')
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('label', name='')

    def test_create_item_with_name_none(self):
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('project', name=None)
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('subtask', name=None)
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('task', name=None)
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('label', name='')

    def test_create_project_with_duplicate_name(self):
        project = ItemFactory.create_item('project', name='Existing Project', user=self.test_user, session=self.session)
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('project', name='Existing Project', user=self.test_user, session=self.session)

    def test_create_task_with_duplicate_name(self):
        task = ItemFactory.create_item('task', name='Existing Task', project=self.test_project, session=self.session)
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('task', name='Existing Task', project=self.test_project, session=self.session)

    def test_create_subtask_with_duplicate_name(self):
        subtask = ItemFactory.create_item('subtask', name='Existing Subtask', task=self.test_task, session=self.session)
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('subtask', name='Existing Subtask', task=self.test_task, session=self.session)

    def test_create_label_with_duplicate_name(self):
        label = ItemFactory.create_item('label', name='Existing Label', color='Azul', user=self.test_user, session=self.session)
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('label', name='Existing Label', user=self.test_user, session=self.session)

    def test_create_item_with_unknown_type(self):
        with self.assertRaises(UnknownItem):
            ItemFactory.create_item('unknown', name='Some Name')

    def test_create_project(self):
        project = ItemFactory.create_item('project', name='New Project', user=self.test_user, session=self.session)
        self.assertEqual(project.name, 'New Project')
        self.assertEqual(project._user, self.test_user)

    def test_create_task(self):
        task = ItemFactory.create_item('task', name='New Task', project=self.test_project, session=self.session)
        self.assertEqual(task.name, 'New Task')
        self.assertEqual(task.project, self.test_project)

    def test_create_subtask(self):
        subtask = ItemFactory.create_item('subtask', name='New Subtask', task=self.test_task, session=self.session)
        self.assertEqual(subtask.name, 'New Subtask')

    def test_create_subtask(self):
        label = ItemFactory.create_item('label', name='New label', color = 'Azul', user=self.test_user, session=self.session)
        self.assertEqual(label.name, 'New label')
        self.assertEqual(label.color, 'Azul')


if __name__ == "__main__":
    unittest.main()