import unittest
from unittest.mock import Mock
import tkinter as tk
from src.gui.subtask.subtask_page import SubtaskPage

class TestSubtaskPage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.home = Mock()
        self.manager = Mock()
        self.subtask = Mock()
        self.subtask.name = "Test Subtask"
        self.subtask.status = True
        self.subtask.conclusion_date = "2023-12-10"
        self.subtask_page = SubtaskPage(self.master, self.home, self.manager, self.subtask)

    def test_init(self):
        self.assertIsNotNone(self.subtask_page)

    def test_create_widgets(self):
        self.assertEqual(self.subtask_page.item, self.subtask)
        self.assertIsNotNone(self.subtask_page.grid_slaves(row=0, column=0))
        self.assertIsNotNone(self.subtask_page.grid_slaves(row=2, column=0))  

        if self.subtask.status:
            self.assertIsNotNone(self.subtask_page.grid_slaves(row=1, column=0))  

    def tearDown(self):
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()