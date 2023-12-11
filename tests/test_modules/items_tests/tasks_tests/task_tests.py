import unittest
from unittest.mock import Mock
from datetime import date
from src import Project, ItemDontHaveThisAttribute, NonChangeableProperty
from src import Subtask,User,Project,Task,Subtask,ItemNameAlreadyExists, ItemNameBlank, NonChangeableProperty
from src.logic.orms.orm import UserORM, Base, ProjectORM, TaskORM,SubtaskORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class TestTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = TestTask.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)
    
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = TestTask.SessionLocal()
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

    def test_initialization_values(self):
            self.assertEqual(self.test_task.name, 'Test Task')
            self.assertEqual(self.test_task.project.id_project, self.test_project.id_project)
            self.assertEqual(self.test_task.project, self.test_project)
            self.assertFalse(self.test_task.status)

    def test_default_values(self):
        new_task = Task(name='New Task', project=self.test_project, session=self.session)
        self.assertEqual(new_task.creation_date, date.today())
        self.assertIsNone(new_task.conclusion_date)
        self.assertFalse(new_task.status)

    def test_delete_task_without_subtasks(self):
        self.test_task.delete()
        deleted_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        self.assertIsNone(deleted_task)


    def test_delete_task_with_subtasks(self):
        self.test_task.add_subtask(self.test_subtask)
        self.test_task.delete()
        deleted_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        deleted_subtask = self.session.query(SubtaskORM).filter(SubtaskORM.id_subtask == self.test_subtask.id_subtask).first()
        self.assertIsNone(deleted_task)
        self.assertIsNone(deleted_subtask)


    def test_add_subtask(self):
        new_subtask = Subtask(name='New Subtask', task=self.test_task, session=self.session)
        self.assertIn(new_subtask, self.test_task.subtasks)
        
        added_subtask = self.session.query(SubtaskORM).filter(SubtaskORM.id_subtask == new_subtask.id_subtask).first()
        self.assertIsNotNone(added_subtask)


    def test_remove_subtask(self):
        new_subtask = Subtask(name='New Subtask for delete', task=self.test_task, session=self.session)
        self.test_task.remove_subtask(new_subtask)
        self.assertNotIn(new_subtask, self.test_project._tasks)

    def test_update_valid_attributes(self):
        new_subtask = Task(project = self.test_project, name="New name",priority="alta", creation_date=date.today(),session = self.session)
        new_subtask.update(name="Updated Name", priority="Alta", end_date = date(2023, 12, 13))

        updated_task = self.session.query(TaskORM).filter(TaskORM.id_task == new_subtask.id_task).first()

        self.assertEqual(updated_task.name, "Updated Name")
        self.assertEqual(updated_task.priority, "Alta")
        self.assertEqual(updated_task.end_date, date(2023, 12, 13))

    def test_update_all_attributes(self):
        new_task = Task(project = self.test_project, name="New task name",priority="alta", creation_date=date.today(),session = self.session)
        new_task.update(name="Updated Name", priority="alta", end_date = date(2023, 12, 13),
                    notification_date = date(2023, 12, 12), description = "Updated Description",
                    status = True)

        task = self.session.query(TaskORM).filter(TaskORM.id_task == new_task.id_task).first()

        self.assertEqual(task.name, "Updated Name")
        self.assertEqual(task.priority, "alta")
        self.assertEqual(task.end_date, date(2023, 12, 13))
        self.assertEqual(task.notification_date, date(2023, 12, 12))
        self.assertEqual(task.description, "Updated Description")
        self.assertTrue(task.status)

    def test_update_invalid_attributes(self):
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.test_task.update(name = 'New Name',invalid_attribute="Invalid")
    
    def test_update_non_changeable_attributes(self):
        new_project = Project(name='New project', user=self.test_user, status=False, creation_date=date.today(), session = self.session)
        task = Task(project = self.test_project, name="New name",priority="alta", creation_date=date.today(),session = self.session)
        with self.assertRaises(NonChangeableProperty):
            task.update(creation_date = date(2023, 11, 13))
        with self.assertRaises(NonChangeableProperty):
            task.update(project = new_project)
        with self.assertRaises(NonChangeableProperty):
            task.update(subtasks = [Mock])
        with self.assertRaises(NonChangeableProperty):
            task.update(project = new_project, subtasks = [], name = "Updated Name")

    def test_save_to_db(self):
        new_task = Task(name="New Task", project=self.test_project, session=self.session)

        saved_task = self.session.query(TaskORM).filter(TaskORM.name == "New Task").first()
        self.assertIsNotNone(saved_task)
        self.assertEqual(saved_task.name, "New Task")  

    def test_conclusion(self):
        self.test_task.conclusion()

        concluded_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        self.assertTrue(concluded_task.status)
        self.assertEqual(concluded_task.conclusion_date, date.today())

    def test_unconclusion(self):
        self.test_task.conclusion()
        self.test_task.unconclusion()

        unconcluded_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        self.assertFalse(unconcluded_task.status)
        self.assertIsNone(unconcluded_task.conclusion_date)

    def test_save_to_memento(self):
        self.test_task.save_to_memento()
        self.assertTrue(self.test_task.has_memento())

    def test_restore_from_memento(self):
        original_name = self.test_task.name
        self.test_task.update(name="Updated Name")
        self.test_task.restore_from_memento()
        self.assertEqual(self.test_task.name, original_name)

        self.test_task.update(name="Updated Name")
        self.test_task.update(name="Another Name")
        self.test_task.restore_from_memento()

        restored_task = self.session.query(TaskORM).filter(TaskORM.id_task == self.test_task.id_task).first()
        self.assertEqual(restored_task.name, "Updated Name")



if __name__ == "__main__":
    unittest.main()