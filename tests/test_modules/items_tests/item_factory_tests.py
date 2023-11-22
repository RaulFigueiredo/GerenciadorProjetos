import unittest
from unittest.mock import Mock
from src import ItemFactory, ItemNameBlank, ItemNameAlreadyExists, UnknownItem

class TestItemFactory(unittest.TestCase):

    def setUp(self):
        self.project_mock = Mock()
        self.task_mock = Mock()
        self.subtask_mock = Mock()

    def test_create_item_with_blank_name(self):
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('project', name='')
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('subtask', name='')
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('task', name='')
    
    def test_create_item_with_name_none(self):
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('project', name=None)
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('subtask', name=None)
        with self.assertRaises(ItemNameBlank):
            ItemFactory.create_item('task', name=None)

    def test_create_project_with_duplicate_name(self):
        user = Mock()
        user.projects = [self.project_mock]
        self.project_mock.name = 'Existing Project'
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('project', name='Existing Project', user=user)

    def test_create_task_with_duplicate_name(self):
        project = Mock()
        project.tasks = [self.task_mock]
        self.task_mock.name = 'Existing Task'
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('task', name='Existing Task', project=project)

    def test_create_subtask_with_duplicate_name(self):
        task = Mock()
        task.subtasks = [self.subtask_mock]
        self.subtask_mock.name = 'Existing Subtask'
        with self.assertRaises(ItemNameAlreadyExists):
            ItemFactory.create_item('subtask', name='Existing Subtask', task=task)

    def test_create_item_with_unknown_type(self):
        with self.assertRaises(UnknownItem):
            ItemFactory.create_item('unknown', name='Some Name')

    def test_create_project(self):
        user = Mock()
        user.projects = []
        project = ItemFactory.create_item('project', name='New Project', user=user)
        self.assertEqual(project.name, 'New Project')
        self.assertEqual(project._user, user)
        user.add_project.assert_called_once_with(project)

    def test_create_task(self):
        project = Mock()
        project.tasks = []
        task = ItemFactory.create_item('task', name='New Task', project=project)
        self.assertEqual(task.name, 'New Task')
        self.assertEqual(task.project, project)
        project.add_task.assert_called_once_with(task)

    def test_create_subtask(self):
        task = Mock()
        task.subtasks = []
        subtask = ItemFactory.create_item('subtask', name='New Subtask',color = "Blue" ,task=task)
        self.assertEqual(subtask.name, 'New Subtask')
        self.assertEqual(subtask.color, "Blue")
        task.add_subtask.assert_called_once_with(subtask)


if __name__ == "__main__":
    unittest.main()