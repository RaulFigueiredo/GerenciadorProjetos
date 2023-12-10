"""
This module contains unit tests for the AddLabelDialog and EditLabelDialog classes from the src.gui module.
It includes tests for initial states, user interactions, validation of inputs, and the overall functionality
of the dialog windows in a Tkinter application. These tests ensure that the dialog components behave as expected,
properly handle user input, and provide feedback or results based on user actions.
"""

import unittest
from unittest.mock import Mock
from src.logic.items.label import Label
from src.gui.labels.label_create import AddLabelDialog
from src.gui.labels.label_edit import EditLabelDialog
from unittest.mock import patch
import tkinter as tk

from src.logic.execeptions.exceptions_items import  ItemDontHaveThisAttribute,\
                                                    NonChangeableProperty


class TestAddLabelDialog(unittest.TestCase):
    """
    Unit tests for the AddLabelDialog class, verifying the dialog's initial state,
    the response to user interactions, and the functionality of its show method.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment before each test method is executed.
        Initializes the Tkinter root and the AddLabelDialog instance.
        """
        self.root = tk.Tk()
        self.add_label_dialog = AddLabelDialog(self.root)
        self.add_label_dialog.top.withdraw()

    def tearDown(self) -> None:
        """
        Cleans up the test environment after each test method is executed.
        Destroys the Tkinter root window.
        """
        self.root.destroy()

    def test_initial_state(self) -> None:
        """
        Tests the initial state of the AddLabelDialog, verifying that the result is None
        and both name entry and color combobox are empty.
        """
        self.assertIsNone(self.add_label_dialog.result)
        self.assertEqual(self.add_label_dialog.name_entry.get(), "")
        self.assertEqual(self.add_label_dialog.color_combobox.get(), "")

    @patch('tkinter.Toplevel.destroy')
    def test_on_confirm(self, mock_destroy) -> None:
        """
        Tests the on_confirm method by simulating user input and confirming the dialog.
        Verifies that the dialog captures the input correctly and calls the destroy method.
        """
        self.add_label_dialog.name_entry.insert(0, "Test Label")
        self.add_label_dialog.color_combobox.set("blue")
        self.add_label_dialog.on_confirm()

        self.assertEqual(self.add_label_dialog.result, ("Test Label", "blue"))
        mock_destroy.assert_called_once()

    def test_show(self) -> None:
        """
        Tests the show method, verifying that it correctly handles the dialog display
        and returns the appropriate result.
        """
        with patch.object(self.add_label_dialog.top, 'wait_window', return_value=None):
            result = self.add_label_dialog.show()
        self.assertIsNone(result)


class TestEditLabelDialog(unittest.TestCase):
    """
    Unit tests for the EditLabelDialog class, focusing on verifying the dialog's initial state,
    the response to user input, validation of input fields, and the functionality of its show method.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment before each test method is executed.
        Initializes the Tkinter root and the EditLabelDialog instance with predefined values.
        """
        self.root = tk.Tk()
        self.edit_label_dialog = EditLabelDialog(self.root, "Previous Name", "blue")
        self.edit_label_dialog.top.withdraw()

    def tearDown(self) -> None:
        """
        Cleans up the test environment after each test method is executed.
        Destroys the Tkinter root window.
        """
        self.root.destroy()

    def test_initial_state(self) -> None:
        """
        Tests the initial state of the EditLabelDialog, verifying that the name entry and color combobox
        are set to the expected initial values.
        """
        self.assertEqual(self.edit_label_dialog.name_entry.get(), "Previous Name")
        self.assertEqual(self.edit_label_dialog.color_combobox.get(), "blue")

    @patch('tkinter.messagebox.showwarning')
    @patch('tkinter.Toplevel.destroy')
    def test_on_confirm_valid(self, mock_destroy, mock_showwarning) -> None:
        """
        Tests the on_confirm method with valid input, verifying that the dialog captures the updated input correctly,
        does not show a warning, and calls the destroy method.
        """
        self.edit_label_dialog.name_entry.delete(0, tk.END)
        self.edit_label_dialog.name_entry.insert(0, "New Name")
        self.edit_label_dialog.color_combobox.set("green")
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_not_called()
        self.assertEqual(self.edit_label_dialog.result, ("New Name", "green"))
        mock_destroy.assert_called_once()

    @patch('tkinter.messagebox.showwarning')
    def test_on_confirm_empty_name(self, mock_showwarning) -> None:
        """
        Tests the on_confirm method with an empty name, verifying that the dialog shows a warning
        and does not update the result.
        """
        self.edit_label_dialog.name_entry.delete(0, tk.END)
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_called_once()
        self.assertIsNone(self.edit_label_dialog.result)

    @patch('tkinter.messagebox.showwarning')
    def test_on_confirm_empty_color(self, mock_showwarning) -> None:
        """
        Tests the on_confirm method with no color selected, verifying that the dialog shows a warning
        and does not update the result.
        """
        self.edit_label_dialog.color_combobox.set('')
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_called_once()
        self.assertIsNone(self.edit_label_dialog.result)

    def test_show(self) -> None:
        """
        Tests the show method, verifying that it correctly handles the dialog display
        and returns the appropriate result based on user interaction.
        """
        with patch.object(self.edit_label_dialog.top, 'wait_window', return_value=None):
            result = self.edit_label_dialog.show()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()