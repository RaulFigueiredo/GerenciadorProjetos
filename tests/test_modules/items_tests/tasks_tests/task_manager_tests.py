import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src.gui.task.task_manager import TaskDisplayManager

class TestTaskDisplayManager(unittest.TestCase):
    def setUp(self):
        self.home = Mock()
        self.home.project_manager = Mock()
        self.manager = TaskDisplayManager(self.home)

    def test_open_page(self):
        item = Mock()
        item.subtasks = []  # Configura 'subtasks' para ser iterável
        parent = Mock()

        with patch.object(tk, 'Toplevel') as mock_top:
            mock_top.return_value.title.return_value = "Detalhes da Tarefa"
            self.manager.open_page(item, parent)
            mock_top.assert_called_once_with(self.home)
            self.assertEqual(self.manager.top_window.title(), "Detalhes da Tarefa")


    def test_refresh_parent_page(self):
        self.manager.parent = Mock()  # Define o atributo 'parent' para o teste
        self.manager.refresh_parent_page()
        self.home.project_manager.top_window.destroy.assert_called_once()
        self.home.project_manager.open_page.assert_called_once_with(self.manager.parent)
        self.home.project_manager.refresh_parent_page.assert_called_once()

    def tearDown(self):
        if self.manager.top_window and self.manager.top_window.winfo_exists():
            self.manager.top_window.destroy()

if __name__ == '__main__':
    unittest.main()
