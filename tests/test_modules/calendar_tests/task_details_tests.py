""" 
- TestTaskDetails: Focuses on testing the functionality related to displaying, updating, and 
  managing task details in the user interface. This includes tests for showing task details, 
  clearing them, and handling their visibility, ensuring a user-friendly task management 
  experience.
"""
import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src import TaskDetails

class TestTaskDetails(unittest.TestCase):
    """
    Test suite for the TaskDetails class.

    This suite includes tests for showing task details, clearing the details text, and closing
    the details frame, ensuring proper functionality and user interface interactions.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment by initializing the TaskDetails instance with mock objects.
        """
        self.mock_details_frame = Mock()
        self.mock_details_text = Mock()
        self.mock_details_scroll = Mock()
        self.mock_close_button = Mock()

        self.task_details = TaskDetails(self.mock_details_frame,
                                        self.mock_details_text,
                                        self.mock_details_scroll,
                                        self.mock_close_button)

    def test_show_task_details(self) -> None:
        """
        Test the functionality of showing task details.

        This test verifies if the task details are displayed correctly within the user interface
        when provided with task information, and checks if the widgets are positioned correctly.
        """
        with patch('tkinter.Button'):
            task_info = [("Tarefa1", "Desc1", "red", "Detalhes1", "Proj1")]
            self.task_details.show_task_details(task_info)

            self.mock_details_frame.grid.assert_called_with(row=0, column=1,
                                                           sticky='nsew', padx=10, pady=10)
            self.mock_details_text.grid.assert_called_with(row=0, column=0, sticky='nsew')
            self.mock_details_scroll.grid.assert_called_with(row=0, column=1, sticky='ns')

    def test_clear_details(self) -> None:
        """
        Test the functionality of clearing the task details.

        This test checks if the task details text is correctly cleared and if the text widget is
        reset to the appropriate state after clearing.
        """
        self.task_details.clear_details()

        self.mock_details_text.config.assert_any_call(state='normal')
        self.mock_details_text.delete.assert_called_with('1.0', tk.END)
        self.mock_details_text.config.assert_any_call(state='disabled')

    def test_close_details(self) -> None:
        """
        Test the functionality of closing the task details frame.

        This test verifies if the task details frame is properly hidden or removed from the user
        interface when the close action is triggered.
        """
        self.task_details.close_details()

        self.mock_details_frame.grid_remove.assert_called_once()
