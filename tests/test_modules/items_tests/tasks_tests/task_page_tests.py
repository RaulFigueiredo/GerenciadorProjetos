import unittest
from unittest.mock import Mock
from src.gui.task.task_page import TaskPage
from tkinter import Tk
from unittest.mock import MagicMock, patch
from src.gui.base_CRUD.base_page import BasePage

class TestTaskPage(unittest.TestCase):

    def setUp(self):
        self.master = Tk()
        self.home = MagicMock()
        self.manager = MagicMock()
        self.task = MagicMock()
        self.task_page = TaskPage(self.master, self.home, self.manager, self.task)

    def tearDown(self):
        self.master.destroy()

    def test_create_widgets(self):
        with patch.object(self.task_page, 'info_box') as mock_info_box, \
             patch.object(self.task_page, 'description_box') as mock_description_box, \
             patch.object(self.task_page, 'subtask_box') as mock_subtask_box, \
             patch.object(self.task_page, 'get_buttons') as mock_get_buttons:

            self.task_page.create_widgets()

            mock_info_box.assert_called_once()
            mock_description_box.assert_called_once()
            mock_subtask_box.assert_called_once()
            mock_get_buttons.assert_called_once()

    def test_on_double_click_with_selection(self):
        self.task_page.subtasks_listbox.insert('end', 'subtask1')
        self.task_page.subtasks_listbox.selection_set(0)
        self.task_page.on_double_click(None)
        # Verifique se a ação esperada ocorre quando um item é selecionado

    def test_on_double_click_without_selection(self):
        self.task_page.on_double_click(None)
        # Verifique se nada acontece quando não há seleção

    def test_info_box(self):
        with patch('tkinter.Label') as mock_label:
            self.task_page.info_box()
            mock_label.assert_called()  # Verifique 