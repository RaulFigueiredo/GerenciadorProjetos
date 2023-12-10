import unittest
from unittest.mock import Mock
from datetime import date
from src import Project, ItemDontHaveThisAttribute, NonChangeableProperty
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty
from src.logic.orms.orm import UserORM, Base, ProjectORM, TaskORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class TestProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = TestProject.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
    
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = TestProject.SessionLocal()
        self.create_test_items()

    def create_test_items(self):
        db_test_project = ProjectORM(name='Test Project', id_user=self.test_user.id_user, status=False, creation_date=date.today())
        self.session.add(db_test_project)
        self.session.commit()
        self.test_project = Project(name=db_test_project.name, user=self.test_user, id_project=db_test_project.id_project,status=db_test_project.status, creation_date=db_test_project.creation_date, session = self.session)
    
        db_test_task = TaskORM(name='Test Task', id_project=self.test_project.id_project, status=False, creation_date=date.today()) 
        self.session.add(db_test_task)
        self.session.commit()

        self.test_task = Task(name=db_test_task.name, project=self.test_project, id_task=db_test_task.id_task, status=db_test_task.status, creation_date=db_test_task.creation_date, session = self.session)

    def tearDown(self):
        self.session.close()

    def test_init(self):
        self.assertEqual(self.test_project.name, "Test Project")
        self.assertIsNone(self.test_project.label, None)
        self.assertIsNone(self.test_project.end_date)
        self.assertEqual(self.test_project.creation_date, date.today())
        self.assertIsNone(self.test_project.conclusion_date)
        self.assertFalse(self.test_project.status)
        self.assertIsNone(self.test_project.description)

    def test_delete_with_tasks(self):
        self.test_project.delete()
        deleted_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        deleted_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        self.assertIsNone(deleted_project)
        self.assertIsNone(deleted_task)


    def test_delete_without_tasks(self):
        self.test_project.delete()
        deleted_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertIsNone(deleted_project)

    def test_update_successful(self):
        self.test_project.update(name='Updated Project Name', description='Updated Description')
        updated_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertEqual(updated_project.name, 'Updated Project Name')
        self.assertEqual(updated_project.description, 'Updated Description')
        

    def test_update_all_attributes(self):
        new_end_date = date(2023, 12, 14)
        new_conclusion_date = date(2023, 12, 15)
        self.test_project.update(name='Another Project Name', description='Another Description', end_date=new_end_date, status=True, conclusion_date=new_conclusion_date)
        updated_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertEqual(updated_project.name, 'Another Project Name')
        self.assertEqual(updated_project.description, 'Another Description')
        self.assertEqual(updated_project.end_date, new_end_date)
        self.assertTrue(updated_project.status)
        self.assertEqual(updated_project.conclusion_date, new_conclusion_date)


    def test_add_task(self):
        task = Task(name="Test Task", project=self.test_project, session=self.session)
        self.assertIn(self.test_task, self.test_project._tasks)
        added_task = self.session.query(TaskORM).filter(TaskORM.id_task == task.id_task).first()
        self.assertIsNotNone(added_task)


    def test_remove_task(self):
        self.test_project.remove_task(self.test_task)
        self.assertNotIn(self.test_task, self.test_project._tasks)

    def test_update_all_attributes(self):
        new_end_date = date(2023, 12, 14)
        new_conclusion_date = date(2023, 12, 15)
        self.test_project.update(name='Updated Project', description='New Description', end_date=new_end_date, status=True, conclusion_date=new_conclusion_date)

        updated_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertEqual(updated_project.name, 'Updated Project')
        self.assertEqual(updated_project.description, 'New Description')
        self.assertEqual(updated_project.end_date, new_end_date)
        self.assertEqual(updated_project.conclusion_date, new_conclusion_date)
        self.assertTrue(updated_project.status)

    def test_update_non_changeable(self):
        with self.assertRaises(NonChangeableProperty):
            self.test_project.update(user=Mock())

        with self.assertRaises(NonChangeableProperty):
            self.test_project.update(creation_date=date(2022, 1, 1))

    def test_update_invalid_attributes(self):
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.test_project.update(name='novo nome', invalid_attribute='Invalid')

    def test_save_to_db(self):
        new_project = Project(user=self.test_user, name='New Project', session=self.session)
        new_project.save_to_db()

        saved_project = self.session.query(ProjectORM).filter(ProjectORM.name == 'New Project').first()
        self.assertIsNotNone(saved_project)
        self.assertEqual(saved_project.name, 'New Project')
        self.assertEqual(saved_project.id_user, self.test_user.id_user)


    def test_conclusion(self):
        self.test_project.conclusion()
        concluded_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertTrue(concluded_project.status)
        self.assertEqual(concluded_project.conclusion_date, date.today())

    def test_unconclusion(self):
        self.test_project.conclusion()
        self.test_project.unconclusion()
        unconcluded_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertFalse(unconcluded_project.status)
        self.assertIsNone(unconcluded_project.conclusion_date)

    def test_save_to_memento_and_restore(self):
        original_name = self.test_project.name
        original_description = self.test_project.description
        self.test_project.save_to_memento()
        self.test_project.update(name='Temporary Name', description='Temporary Description')
        self.test_project.restore_from_memento()
        restored_project = self.session.query(ProjectORM).filter(ProjectORM.id_project == self.test_project.id_project).first()
        self.assertEqual(restored_project.name, original_name)
        self.assertEqual(restored_project.description, original_description)


if __name__ == "__main__":
    unittest.main()