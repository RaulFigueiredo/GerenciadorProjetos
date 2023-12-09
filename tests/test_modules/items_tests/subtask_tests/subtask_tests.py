import unittest
from src import Subtask, ItemDontHaveThisAttribute, NonChangeableProperty
from unittest.mock import Mock

class TestSubtask(unittest.TestCase):

    def setUp(self):
        self.mock_task = Mock()
        self.subtask = Subtask(self.mock_task, "Test Subtask")

    def test_initialization(self):
        self.assertEqual(self.subtask.name, "Test Subtask")
        self.assertFalse(self.subtask.status)

    def test_delete(self):
        self.subtask.delete()
        self.mock_task.remove_subtask.assert_called_once_with(self.subtask)

    def test_update_successful(self):
        self.subtask.update(name="Updated Subtask", status=True)
        self.assertEqual(self.subtask.name, "Updated Subtask")
        self.assertTrue(self.subtask.status)

    def test_update_unsuccessful(self):
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.subtask.update(invalid_attribute="Unknown Attribute")
    
    def test_update_non_changeable(self):
        with self.assertRaises(NonChangeableProperty):
            self.subtask.update(task=Mock())




if __name__ == "__main__":
    unittest.main()