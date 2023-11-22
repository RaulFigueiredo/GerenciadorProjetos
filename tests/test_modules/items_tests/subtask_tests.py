import unittest
from src import Subtask
from unittest.mock import Mock

class TestSubtask(unittest.TestCase):

    def setUp(self):
        self.mock_task = Mock()
        self.subtask = Subtask(self.mock_task, "Test Subtask", "Red")

    def test_initialization(self):
        self.assertEqual(self.subtask.name, "Test Subtask")
        self.assertEqual(self.subtask.color, "Red")

    def test_delete(self):
        self.subtask.delete()
        self.mock_task.remove_subtask.assert_called_once_with(self.subtask)

    def test_update_successful(self):
        self.subtask.update(name="Updated Subtask", color="Blue")
        self.assertEqual(self.subtask.name, "Updated Subtask")
        self.assertEqual(self.subtask.color, "Blue")




if __name__ == "__main__":
    unittest.main()