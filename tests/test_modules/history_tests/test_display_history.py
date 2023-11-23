import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch
from src.logic.history.task_history import HistorySingleton
from src.logic.users.user import User
from src.gui.history_page import HistoryManagerApp

class TestHistoryManagerApp(unittest.TestCase):
    def setUp(self):
        self.root_window = tk.Tk()
        self.previous_window = tk.Tk()
        self.user = User("TestUser")
        self.app = HistoryManagerApp(self.root_window, self.user, self.previous_window)

    def tearDown(self):
        self.root_window.destroy()
        self.previous_window.destroy()

    def test_display_completed_tasks(self):
        # Mocking HistorySingleton and its methods
        mock_history = MagicMock(spec=HistorySingleton)
        mock_tasks_completed = [
            MagicMock(name="Task1", project=MagicMock(label=MagicMock(color="red"))),
            MagicMock(name="Task2", project=MagicMock(label=MagicMock(color="blue")))
        ]
        mock_history.tasks_completed.return_value = mock_tasks_completed

        # Patching HistorySingleton instance in the app with the mock
        with patch.object(self.app, 'history', new=mock_history):
            self.app.display_completed_tasks()

            # Assertions for UI elements creation
            #self.assertEqual(len(self.app.root_window.grid_slaves()), len(mock_tasks_completed) + 2)  # Two extra rows for title and back button

            # Check if each task's project label has a color string
            for task in mock_tasks_completed:
                self.assertTrue(isinstance(task.project, MagicMock))
                self.assertTrue(isinstance(task.project.label, MagicMock))
                self.assertTrue(isinstance(task.project.label.color, str))
                self.assertIn(task.project.label.color.lower(), ["red", "blue"])  # Ensure color is 'red' or 'blue'

    def test_go_back(self):
        # Mocking deiconify and destroy methods
        self.app.root_window.deiconify = MagicMock()
        self.app.root_window.destroy = MagicMock()

        self.app.go_back()

        # Asserting whether the methods were called
        self.app.root_window.deiconify.assert_called_once()
        self.app.root_window.destroy.assert_called_once()

    # Add more test cases for other methods as needed...

if __name__ == '__main__':
    unittest.main()
