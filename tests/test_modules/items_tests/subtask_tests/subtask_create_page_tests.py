import unittest
from unittest.mock import Mock
import tkinter as tk
from src.gui.forms_base import EntryField
from src.gui.base_CRUD.base_create_page import BaseCreatePage
from src.gui.subtask.subtask_create_page import SubtaskCreatePage

class TestSubtaskCreatePage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.mediator = Mock()
        self.parent = Mock()
        self.subtask_page = SubtaskCreatePage(self.master, self.mediator, self.parent)

    def test_init(self):
        self.assertIsNotNone(self.subtask_page)

    def test_create_widgets(self):
        self.assertIsNotNone(self.subtask_page.name_field)
        self.assertIsInstance(self.subtask_page.name_field, EntryField)

    def test_prepare_data(self):
        test_name = "Test Subtask"
        self.subtask_page.name_field.set_value(test_name)

        expected_data = {
            "item_type": "subtask",
            "task": self.parent,
            "name": test_name
        }

        self.assertEqual(self.subtask_page.prepare_data(), expected_data)

    def tearDown(self):
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()
