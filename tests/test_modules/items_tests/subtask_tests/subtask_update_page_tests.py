import unittest
from unittest.mock import Mock
import tkinter as tk
from src.gui.subtask.subtask_updata_page import SubtaskUpdatePage
from src.gui.forms_base import EntryField

class TestSubtaskUpdatePage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.manager = Mock()
        self.mediator = Mock()
        self.subtask = Mock()
        self.subtask.name = "Test Subtask"
        self.update_page = SubtaskUpdatePage(self.master, self.manager, self.mediator, self.subtask)

    def test_init(self):
        self.assertIsNotNone(self.update_page)

    def test_create_widgets(self):
        self.assertIsNotNone(self.update_page.name_field)
        self.assertIsInstance(self.update_page.name_field, EntryField)
        self.assertEqual(self.update_page.name_field.get_value(), self.subtask.name)

    def test_prepare_data(self):

        test_name = "Updated Subtask"
        self.update_page.name_field.set_value(test_name)

        expected_data = {
            "name": test_name,
        }

        self.assertEqual(self.update_page.prepare_data(), expected_data)

    def tearDown(self):
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()
