import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src.gui.project.project_manager import ProjectDisplayManager  
import datetime

class TestProjectDisplayManager(unittest.TestCase):
    def setUp(self):
        self.home = tk.Tk()
        self.user = Mock()  
        self.home.update_main_page = Mock()
        self.user.labels = [Mock(name='Label 1'), Mock(name='Label 2')]
        self.manager = ProjectDisplayManager(self.home, self.user)

    @patch('tkinter.messagebox')
    def test_open_page(self, mock_messagebox):
        mock_messagebox.askyesno.return_value = True
        mock_project = Mock()
        mock_project.tasks = []  
        self.manager.open_page(mock_project)

    def test_open_create_page(self):
        self.manager.open_create_page() 

    def test_open_update_page(self):
        mock_project = Mock()
        mock_project.end_date = datetime.date(2023, 1, 1)  
        self.manager.open_update_page(mock_project)

    def test_refresh_parent_page(self):
        self.manager.refresh_parent_page()
        self.home.update_main_page.assert_called_once()

    def tearDown(self):
        self.home.destroy()

if __name__ == '__main__':
    unittest.main()
