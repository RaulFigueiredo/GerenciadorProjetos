"""
This module contains unit tests for the Label class, verifying creation, update, and deletion of labels,
along with interactions with a mocked user object to simulate system operations.
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

class TestLabel(unittest.TestCase):
    """
    The TestLabel class contains unit tests for the Label class.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment before each test method is called.
        Initializes a mocked user and a Label object for testing purposes.
        """
        self.mock_user: Mock = Mock()
        self.mock_user.add_label = Mock()
        self.mock_user.remove_label = Mock()
        self.mock_user.update_label = Mock()
        self.label: Label = Label(self.mock_user, "Test Label", "blue")

    def test_init(self) -> None:
        """
        Tests the proper initialization of the Label object, verifying that the name and color attributes are correct.
        """
        self.assertEqual(self.label.name, "Test Label")
        self.assertEqual(self.label.color, "blue")
        self.mock_user.add_label.assert_called_with(self.label)

    def test_delete(self) -> None:
        """
        Tests the deletion method of the Label object, verifying that the mock user's remove_label method is called.
        """
        self.label.delete()
        self.mock_user.remove_label.assert_called_with(self.label)

    def test_update_valid(self) -> None:
        """
        Tests valid update of the Label object by changing its name and color, and verifies that the new values are correct.
        """
        self.label.update(name="New Label", color="red")
        self.assertEqual(self.label.name, "New Label")
        self.assertEqual(self.label.color, "red")
        self.mock_user.update_label.assert_called_with(self.label)

    def test_update_invalid(self) -> None:
        """
        Tests invalid update of the Label object by attempting to update a non-existent attribute and verifies that the correct exception is raised.
        """
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.label.update(task="New Task")

    def test_update_non_changeable_property(self) -> None:
        """
        Tests that updating a non-changeable property (user) raises the appropriate exception.
        """
        with self.assertRaises(NonChangeableProperty):
            self.label.update(user=self.mock_user)

    def test_getters(self) -> None:
        """
        Tests the getters for name and color properties.
        """
        self.assertEqual(self.label.name, "Test Label")
        self.assertEqual(self.label.color, "blue")

    def test_setters(self) -> None:
        """
        Tests the setters for name and color properties.
        """
        self.label.name = "Updated Label"
        self.label.color = "green"
        self.assertEqual(self.label.name, "Updated Label")
        self.assertEqual(self.label.color, "green")

    def test_update_with_invalid_data_type(self) -> None:
        """
        Tests updating the label with invalid data types for name and color properties.
        """
        with self.assertRaises(TypeError):
            self.label.update(name=123)  # Assuming name should be a string

        with self.assertRaises(TypeError):
            self.label.update(color=456)  # Assuming color should be a string
            
if __name__ == "__main__":
    unittest.main()