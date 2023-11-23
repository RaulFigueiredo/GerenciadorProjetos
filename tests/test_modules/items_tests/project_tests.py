import unittest
from unittest.mock import Mock
from datetime import date
from src import Project, ItemDontHaveThisAttribute, NonChangeableProperty

class TestProject(unittest.TestCase):

    def setUp(self):
        self.user = Mock()
        self.label = Mock()
        self.project = Project(user=self.user, name="Project Name", label=self.label,
                               end_date=date(2023, 12, 13))

    def test_init(self):
        self.assertEqual(self.project.name, "Project Name")
        self.assertEqual(self.project.label, self.label)
        self.assertEqual(self.project.end_date, date(2023, 12, 13))
        self.assertEqual(self.project.creation_date, date.today())
        self.assertIsNone(self.project.conclusion_date)
        self.assertFalse(self.project.status)
        self.assertEqual(self.project.tasks, [])
        self.assertIsNone(self.project.description)

    def test_delete_with_tasks(self):
        
        mock_task1 = Mock()
        mock_task2 = Mock()
        self.project.add_task(mock_task1)
        self.project.add_task(mock_task2)

        self.project.delete()

        mock_task1.delete.assert_called_once()
        mock_task2.delete.assert_called_once()

        self.user.remove_project.assert_called_once_with(self.project)

    def test_delete_without_tasks(self):
        self.project.delete()

        self.user.remove_project.assert_called_once_with(self.project)

    def test_update_successful(self):
        self.project.update(name='New Project Name', description='New Description')

        self.assertEqual(self.project.name, 'New Project Name')
        self.assertEqual(self.project.description, 'New Description')
        

    def test_update_all_attributes(self):
        new_label_mock = Mock()
        self.project.update(name='New Project Name', description='New Description',
                            end_date=date(2023, 12, 14), label=new_label_mock, status=True,
                            conclusion_date=date(2023, 12, 15))

        self.assertEqual(self.project.name, 'New Project Name')
        self.assertEqual(self.project.description, 'New Description')
        self.assertEqual(self.project.end_date, date(2023, 12, 14))
        self.assertEqual(self.project.label, new_label_mock)
        self.assertTrue(self.project.status)
        self.assertEqual(self.project.conclusion_date, date(2023, 12, 15))


    def test_add_task(self):
        mock_task = Mock()
        self.project.add_task(mock_task)
        self.assertIn(mock_task, self.project._tasks)


    def test_add_two_tasks(self):
        mock_task1 = Mock()
        mock_task2 = Mock()
        self.project.add_task(mock_task1)
        self.project.add_task(mock_task2)
        self.assertIn(mock_task1, self.project._tasks)
        self.assertIn(mock_task2, self.project._tasks)


    def test_remove_task(self):
        mock_task = Mock()
        self.project.add_task(mock_task)
        
        self.project.remove_task(mock_task)
        
        self.assertNotIn(mock_task, self.project._tasks)

    def test_remove_two_tasks(self):
        mock_task1 = Mock()
        mock_task2 = Mock()
        self.project.add_task(mock_task1)
        self.project.add_task(mock_task2)
        
        self.project.remove_task(mock_task1)
        self.project.remove_task(mock_task2)
        
        self.assertNotIn(mock_task1, self.project._tasks)
        self.assertNotIn(mock_task2, self.project._tasks)

    def test_update_valid_attributes(self):
        project = Project(user = self.user, name="Project Name", label="High")
        project.update(name="Updated Name", label="Low", end_date = date(2023, 12, 13))

        self.assertEqual(project.name, "Updated Name")
        self.assertEqual(project.label, "Low")
        self.assertEqual(project.end_date, date(2023, 12, 13))

    def test_update_all_attributes(self):
        project = Project(user = self.user, name="Project Name", label="High")
        project.update(name="Updated Name", label="Low", end_date = date(2023, 12, 13),
                    description = "Updated Description", status = True)

        self.assertEqual(project.name, "Updated Name")
        self.assertEqual(project.label, "Low")
        self.assertEqual(project.end_date, date(2023, 12, 13))
        self.assertEqual(project.description, "Updated Description")
        self.assertTrue(project.status)

    def test_update_non_changeable(self):
        with self.assertRaises(NonChangeableProperty):
            self.project.update(user=Mock())
        with self.assertRaises(NonChangeableProperty):
            self.project.update(creation_date=date(2021, 1, 1))
        with self.assertRaises(NonChangeableProperty):
            self.project.update(name="Updated Name", label="Low", end_date = date(2023, 12, 13),
                                creation_date=date(2021, 1, 1))
        with self.assertRaises(NonChangeableProperty):
            self.project.update(user=Mock(), name="Updated Name", label="Low", end_date = date(2023, 12, 13))
    
    def test_update_invalid_attributes(self):
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.project.update(invalid_attribute="Invalid Attribute")

if __name__ == "__main__":
    unittest.main()