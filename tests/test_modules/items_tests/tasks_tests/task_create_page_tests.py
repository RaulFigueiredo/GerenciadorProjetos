import unittest
from unittest.mock import Mock
import tkinter as tk
from src.gui.task.task_create_page import TaskCreatePage
import datetime

class TestTaskCreatePage(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.mediator = Mock()
        self.parent = Mock()
        self.create_page = TaskCreatePage(self.master, self.mediator, self.parent)

    def test_init(self):
        self.assertIsNotNone(self.create_page)

    def test_create_widgets(self):
        self.assertIsNotNone(self.create_page.name_field)
        self.assertIsNotNone(self.create_page.priority_combobox)
        self.assertIsNotNone(self.create_page.end_date_field)
        self.assertIsNotNone(self.create_page.notification_date_field)
        self.assertIsNotNone(self.create_page.description_text)

    def test_prepare_data(self):
        test_name = "Task Name"
        test_priority = "Alta"
        test_end_date = datetime.datetime.strptime("31/12/2023", "%d/%m/%Y").date()
        test_notification_date = datetime.datetime.strptime("01/12/2023", "%d/%m/%Y").date()
        test_description = "Task Description"

        self.create_page.name_field.set_value(test_name)
        self.create_page.priority_combobox.set_value(test_priority)
        self.create_page.end_date_field.set_value(test_end_date)
        self.create_page.notification_date_field.set_value(test_notification_date)
        self.create_page.description_text.set_value(test_description)

        expected_data = {
            "item_type": "task",
            "project": self.parent,
            "name": test_name,
            "priority": test_priority,
            "end_date": test_end_date,
            "notification_date": test_notification_date,
            "description": test_description
        }

        self.assertEqual(self.create_page.prepare_data(), expected_data)

    def tearDown(self):
        self.master.destroy()

if __name__ == '__main__':
    unittest.main()
