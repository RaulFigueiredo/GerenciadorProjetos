import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src.gui.project.project_page import ProjectPage

class TestProjectPage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.home = Mock()
        self.manager = Mock()
        self.project = Mock()
        self.project.name = "Test Project"
        self.project.tasks = [Mock(), Mock()]
        self.project.tasks[0].name = "Task 1"
        self.project.tasks[0].status = False
        self.project.tasks[1].name = "Task 2"
        self.project.tasks[1].status = True
        self.project.label = "Test Label"
        self.project.creation_date = "2023-01-01"
        self.project.end_date = "2023-12-31"
        self.project.status = None
        self.project.conclusion_date = None
        self.project.description = "Test Description"

        self.page = ProjectPage(self.master, self.home, self.manager, self.project)

    def test_init(self):
        self.assertIsNotNone(self.page)

    def test_info_box(self):
        name_label = [widget for widget in self.page.children.values() if isinstance(widget, tk.Label) and widget['text'] == self.project.name][0]
        self.assertEqual(name_label['text'], self.project.name)



    def test_description_box(self):
        description_text = [widget for widget in self.page.children.values() if isinstance(widget, tk.Text)][0]
        self.assertEqual(description_text.get("1.0", "end-1c"), self.project.description)


    def test_task_box(self):
        self.assertEqual(self.page.tasks_listbox.size(), len(self.project.tasks))
        self.assertEqual(self.page.tasks_listbox.get(0), self.project.tasks[0].name)



    def test_on_double_click(self):
        with patch('tkinter.Listbox.curselection', return_value=[0]):
            self.page.on_double_click(None)

            self.home.task_manager.open_page.assert_called_with(self.project.tasks[0], parent=self.project)


    def tearDown(self):
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()