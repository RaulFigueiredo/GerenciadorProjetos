import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src.gui.subtask.subtask_page import SubtaskPage
from src.gui.subtask.subtask_updata_page import SubtaskUpdatePage
from src.gui.subtask.subtask_create_page import SubtaskCreatePage
from src.gui.mediator import FormMediator
from src.gui.subtask.subtask_manager import SubtaskDisplayManager

class TestSubtaskDisplayManager(unittest.TestCase):
    def setUp(self):
        self.home = Mock()
        self.manager = SubtaskDisplayManager(self.home)

    def test_open_page(self):
        item = Mock()
        parent = Mock()

        with unittest.mock.patch('tkinter.Toplevel') as mock_top:
            mock_top.return_value.title.return_value = "Detalhes da Subtarefa"
            self.manager.open_page(item, parent)
            self.assertEqual(mock_top.return_value.title(), "Detalhes da Subtarefa")

    def test_open_update_page(self):
        item = Mock()

        with unittest.mock.patch('tkinter.Toplevel') as mock_top:
            mock_top.return_value.title.return_value = "Editar Tarefa"
            self.manager.open_update_page(item)
            self.assertEqual(mock_top.return_value.title(), "Editar Tarefa")

    def test_open_create_page(self):
        parent = Mock()

        with unittest.mock.patch('tkinter.Toplevel') as mock_top:
            mock_top.return_value.title.return_value = "Criar Nova Tarefa"
            self.manager.open_create_page(parent)
            self.assertEqual(mock_top.return_value.title(), "Criar Nova Tarefa")

    def tearDown(self):
        if self.manager.top_window and self.manager.top_window.winfo_exists():
            self.manager.top_window.destroy()

if __name__ == '__main__':
    unittest.main()