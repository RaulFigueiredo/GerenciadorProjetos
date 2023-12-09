import unittest
from unittest.mock import patch, MagicMock,mock_open
from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import EmptyListProjects,\
                                                   FileNameBlank,\
                                                   DirectoryBlank
from src.logic.export import Export
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
import os

"""
This module contains unit tests for the Export class in the src.logic.export module. It includes tests for various
scenarios such as valid input, empty lists, blank filenames, and blank directories to ensure robustness and
reliability of the Export functionality.
"""

class TestExport(unittest.TestCase):
    """
    Test suite for the Export class.

    Methods:
        setUp: Sets up test data for the test methods.
        test_json_generator_valid_input: Tests the json_generator method with valid input.
        test_json_generator_empty_list: Tests the json_generator method with an empty list.
        test_json_generator_blank_filename: Tests the json_generator method with a blank filename.
        test_json_generator_blank_directory: Tests the json_generator method with a blank directory.
        test_check_data_non_empty: Tests the check_data method with non-empty data.
        test_check_data_empty: Tests the check_data method with empty data.
        test_check_filename_non_empty: Tests the check_filename method with a non-empty filename.
        test_check_filename_empty: Tests the check_filename method with an empty filename.
        test_check_directory_non_empty: Tests the check_directory method with a non-empty directory.
        test_check_directory_empty: Tests the check_directory method with an empty directory.
    """

    def setUp(self):
        """
        Set up function to initialize common test data.
        Creates example user, projects, and tasks for testing.
        """
        user = User(name="Usuário Exemplo")
        pj_1 = Project(name="Projeto Exemplo 1", user=user, description='Esse é um projeto de exemplo (1)')
        pj_2 = Project(name="Projeto Exemplo 2", user=user, description='Esse é um projeto de exemplo (2)')
        pj_3 = Project(name="Projeto Exemplo 3", user=user, description='Esse é um projeto de exemplo (3)')

        t1 = Task(name="Tarefa Exemplo 1", project=pj_1, description='Essa é uma tarefa de exemplo (1)')
        t2 = Task(name="Tarefa Exemplo 2", project=pj_1, description='Essa é uma tarefa de exemplo (2)')

        self.projects_list = [pj_1, pj_2, pj_3]

    def test_json_generator_valid_input(self):
        """
        Test the json_generator method with valid input parameters.
        Ensures that no exceptions are raised and the function behaves as expected.
        """
        with patch('builtins.open', new_callable=mock_open()), patch('os.makedirs'), patch('os.path.exists', return_value=True):
            Export.json_generator(self.projects_list, 'test_file', 'test_directory')

    def test_json_generator_empty_list(self):
        """
        Test the json_generator method with an empty list.
        Verifies that an EmptyListProjects exception is raised.
        """
        with self.assertRaises(EmptyListProjects):
            Export.json_generator([], 'test_file', 'test_directory')

    def test_json_generator_blank_filename(self):
        """
        Test the json_generator method with a blank filename.
        Checks if the FileNameBlank exception is raised.
        """
        with self.assertRaises(FileNameBlank):
            Export.json_generator(self.projects_list, '', 'test_directory')

    def test_json_generator_blank_directory(self):
        """
        Test the json_generator method with a blank directory.
        Verifies that a DirectoryBlank exception is raised.
        """
        with self.assertRaises(DirectoryBlank):
            Export.json_generator(self.projects_list, 'test_file', '')

    def test_check_data_non_empty(self):
        """
        Test the check_data method with non-empty data.
        Ensures no exception is raised for valid data input.
        """
        try:
            Export.check_data(self.projects_list)
        except Exception as e:
            self.fail(f"check_data raised an unexpected exception: {e}")

    def test_check_data_empty(self):
        """
        Test the check_data method with empty data.
        Checks that an EmptyListProjects exception is raised.
        """
        with self.assertRaises(EmptyListProjects):
            Export.check_data([])

    def test_check_filename_non_empty(self):
        """
        Test the check_filename method with a non-empty filename.
        Ensures no exception is raised for a valid filename.
        """
        try:
            Export.check_filename('test_file')
        except Exception as e:
            self.fail(f"check_filename raised an unexpected exception: {e}")

    def test_check_filename_empty(self):
        """
        Test the check_filename method with an empty filename.
        Verifies that a FileNameBlank exception is raised.
        """
        with self.assertRaises(FileNameBlank):
            Export.check_filename('')

    def test_check_directory_non_empty(self):
        """
        Test the check_directory method with a non-empty directory.
        Ensures no exception is raised for a valid directory.
        """
        try:
            Export.check_directory('test_directory')
        except Exception as e:
            self.fail(f"check_directory raised an unexpected exception: {e}")

    def test_check_directory_empty(self):
        """
        Test the check_directory method with an empty directory.
        Verifies that a DirectoryBlank exception is raised.
        """
        with self.assertRaises(DirectoryBlank):
            Export.check_directory('')

if __name__ == '__main__':
    unittest.main()