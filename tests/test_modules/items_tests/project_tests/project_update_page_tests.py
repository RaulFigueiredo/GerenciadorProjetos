import unittest
from unittest.mock import Mock
import tkinter as tk
from src.gui.project.project_update_page import ProjectUpdatePage
import datetime

class TestProjectUpdatePage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.manager = Mock()
        self.mediator = Mock()
        self.project = Mock()
        self.project.name = "Test Project"
        self.project.label = "Test Label"
        self.project.end_date = datetime.date(2023, 12, 9)  # Usando um objeto datetime.date
        self.project.description = "Test Description"
        self.labels = ["Label 1", "Label 2"]

        self.update_page = ProjectUpdatePage(self.master, self.manager, self.mediator, self.project, self.labels)

    def test_init(self):
        self.assertIsNotNone(self.update_page)

    def test_create_widgets(self):
        expected_date_str = self.project.end_date.strftime('%m/%d/%y').lstrip('0').replace('/0','/')
        self.assertEqual(self.update_page.date_field.get_value(), expected_date_str)

        self.assertEqual(self.update_page.name_field.get_value(), self.project.name)
        self.assertEqual(self.update_page.label_combobox.get_value(), self.project.label)
        self.assertEqual(self.update_page.description_text.get_value(), self.project.description)

    def test_prepare_data(self):
        expected_data = {
            "name": self.project.name,
            "label": self.project.label,
            "end_date": self.project.end_date.strftime('%m/%d/%y').lstrip('0').replace('/0','/'),
            "description": self.project.description
        }
        self.assertEqual(self.update_page.prepare_data(), expected_data)

    def tearDown(self):
        self.master.update_idletasks()  
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()
