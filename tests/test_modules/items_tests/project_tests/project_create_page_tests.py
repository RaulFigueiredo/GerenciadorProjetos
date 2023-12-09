import unittest
from unittest.mock import Mock
from src.logic.items.label import Label
from src.gui.project.project_create_page import ProjectCreatePage
from unittest.mock import patch
import tkinter as tk

class TestProjectCreatePage(unittest.TestCase):

    def setUp(self):
        self.master = tk.Tk() 
        self.mediator = Mock()  
        self.parent = Mock()  
        self.labels = ["Label 1", "Label 2"] 

        self.page = ProjectCreatePage(self.master, self.mediator, self.parent, self.labels)

    def test_init(self):
        self.assertIsNotNone(self.page)
        self.assertEqual(self.page.labels, self.labels)

    def test_prepare_data(self):
        self.page.name_field.get_value = Mock(return_value="Test Project")
        self.page.label_combobox.get_value = Mock(return_value="Test Label")
        self.page.date_field.get_value = Mock(return_value="2023-12-08")
        self.page.description_text.get_value = Mock(return_value="Test Description")

        data = self.page.prepare_data()

        self.assertEqual(data["item_type"], "project")
        self.assertEqual(data["user"], self.parent)
        self.assertEqual(data["name"], "Test Project")
        self.assertEqual(data["label"], "Test Label")
        self.assertEqual(data["end_date"], "2023-12-08")
        self.assertEqual(data["description"], "Test Description")

    def tearDown(self):
        self.master.destroy()  

if __name__ == '__main__':
    unittest.main()