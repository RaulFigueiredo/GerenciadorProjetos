import unittest
from src.logic import Task, ItemDontHaveThisAttribute, NonChangeableProperty
from unittest.mock import Mock
from datetime import date

class TestTask(unittest.TestCase):

    def setUp(self):
        self.name = "Task Name"
        self.project = Mock()
        self.priority = "High"
        self.end_date = date(2023, 12, 31)
        self.notification_date = date(2023, 11, 30)
        self.description = "Task Description"

        self.task = Task(project = self.project,
                         name = self.name,
                         priority = self.priority,
                         end_date = self.end_date, 
                         notification_date = self.notification_date,
                         description = self.description)


    def test_initialization_values(self):
        self.assertEqual(self.task.name, self.name)
        self.assertEqual(self.task.project, self.project)
        self.assertEqual(self.task.priority, self.priority)
        self.assertEqual(self.task.end_date, self.end_date)
        self.assertEqual(self.task.notification_date, self.notification_date)
        self.assertEqual(self.task.description, self.description)


    def test_default_values(self):
        self.assertEqual(self.task.creation_date, date.today())
        self.assertIsNone(self.task.conclusion_date)
        self.assertFalse(self.task.status)

    def test_delete_task_without_subtasks(self):
        self.task.delete()

        self.assertEqual(len(self.task.subtasks), 0)
        self.project.remove_task.assert_called_once_with(self.task)


    def test_delete_task_with_subtasks(self):
        subtask1 = Mock()
        subtask2 = Mock()  
        
        self.task.add_subtask(subtask1)
        self.task.add_subtask(subtask2)

        self.task.delete()

        subtask1.delete.assert_called_once()
        subtask2.delete.assert_called_once()
        self.project.remove_task.assert_called_once_with(self.task)


    def test_add_one_subtask(self):
        subtask = Mock()  

        self.task.add_subtask(subtask)
        self.assertIn(subtask, self.task.subtasks)


    def test_add_two_subtask(self):
        subtask1 = Mock()  
        subtask2 = Mock()  

        self.task.add_subtask(subtask1)
        self.task.add_subtask(subtask2)
        self.assertIn(subtask1, self.task.subtasks)
        self.assertIn(subtask2, self.task.subtasks)


    def test_remove_one_subtask(self):
        subtask = Mock()  

        self.task.add_subtask(subtask)

        self.task.remove_subtask(subtask)
        self.assertNotIn(subtask, self.task.subtasks)
    
    def test_remove_two_subtask(self):
        subtask1 = Mock()  
        subtask2 = Mock()  

        self.task.add_subtask(subtask1)
        self.task.add_subtask(subtask2)

        self.task.remove_subtask(subtask1)
        self.task.remove_subtask(subtask2)
        self.assertNotIn(subtask1, self.task.subtasks)
        self.assertNotIn(subtask2, self.task.subtasks)

    def test_update_valid_attributes(self):
        task = Task(project = self.project, name="Task Name", priority="High")
        task.update(name="Updated Name", priority="Low", end_date = date(2023, 12, 13))

        self.assertEqual(task.name, "Updated Name")
        self.assertEqual(task.priority, "Low")
        self.assertEqual(task.end_date, date(2023, 12, 13))

    def test_update_all_attributes(self):
        task = Task(project = self.project, name="Task Name", priority="High")
        task.update(name="Updated Name", priority="Low", end_date = date(2023, 12, 13),
                    notification_date = date(2023, 12, 12), description = "Updated Description",
                    status = True)

        self.assertEqual(task.name, "Updated Name")
        self.assertEqual(task.priority, "Low")
        self.assertEqual(task.end_date, date(2023, 12, 13))
        self.assertEqual(task.notification_date, date(2023, 12, 12))
        self.assertEqual(task.description, "Updated Description")
        self.assertTrue(task.status)

    def test_update_invalid_attributes(self):
        task = Task(project = self.project, name="Task Name", priority="High")
        with self.assertRaises(ItemDontHaveThisAttribute):
            task.update(invalid_attribute="Invalid Attribute")
    
    def test_update_non_changeable_attributes(self):
        task = Task(project = self.project, name="Task Name", priority="High")
        with self.assertRaises(NonChangeableProperty):
            task.update(creation_date = date(2023, 11, 13))
        with self.assertRaises(NonChangeableProperty):
            task.update(project = Mock())
        with self.assertRaises(NonChangeableProperty):
            task.update(subtasks = [Mock()])
        with self.assertRaises(NonChangeableProperty):
            task.update(project = Mock(), subtasks = [], name = "Updated Name")


if __name__ == "__main__":
    unittest.main()