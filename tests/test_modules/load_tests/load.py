import unittest
import json
from unittest.mock import patch, Mock, mock_open
from src.logic.load import Load
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError

"""
This module contains unit tests for the Load class in the src.logic.load module. It includes tests for various
scenarios such as valid and invalid file formats, file existence, file structure, and duplicate project names to
ensure robustness and reliability of the Load functionality.
"""

class TestLoad(unittest.TestCase):
    """
    Test suite for the Load class.

    Methods:
        setUp: Sets up test data for the test methods.
        test_check_format_with_valid_format: Tests the check_format method with a valid file format.
        test_check_format_with_invalid_format: Tests the check_format method with an invalid file format.
        test_check_file_existence_with_existing_file: Tests the check_file_existence method with an existing file.
        test_check_file_existence_with_nonexistent_file: Tests the check_file_existence method with a nonexistent file.
        test_check_file_structure_with_valid_data: Tests the check_file_structure method with valid data.
        test_check_file_structure_with_invalid_data: Tests the check_file_structure method with invalid data structure.
        test_check_duplicate_project_name_with_no_duplicates: Tests check_duplicate_project_name with no duplicate project names.
        test_check_duplicate_project_name_with_duplicates: Tests check_duplicate_project_name with duplicate project names.
        test_check_project_name_blank_with_no_blank_names: Tests check_project_name_blank with no blank project names.
        test_check_project_name_blank_with_blank_names: Tests check_project_name_blank with blank project names.
        test_json_reader_with_valid_data: Tests json_reader method with valid data.
    """

    def setUp(self):
        """
        Set up function to initialize common test data.
        Creates example user, valid and invalid data, and file paths for testing.
        """
        self.valid_file_path = 'tests/test_modules/load_tests/valid.json'
        self.invalid_file_path = 'tests/test_modules/load_tests/invalid.txt'
        self.nonexistent_file_path = 'nonexistent.json'
        self.user = User('Usuário Exemplo') 
        self.valid_data = [
            {
                "project": "Projeto 1",
                "end_date": "2023-01-01",
                "description": "Descrição do Projeto 1",
                "tasks": [
                    {
                        "task": "Tarefa 1",
                        "priority": 'Urgente',
                        "end_date": "2023-01-10",
                        "notification_date": "2023-01-05",
                        "description": "Descrição da Tarefa 1",
                        "subtasks": [
                            {"subtask": "Subtarefa 1"}
                        ]
                    }
                ]
            }
        ]
        self.invalid_data_structure = {"invalid": "data"}

    def test_check_format_with_valid_format(self):
        """
        Test the check_format method with a file having a valid format.
        Ensures that no exception is raised for a valid file format.
        """
        Load.check_formart(self.valid_file_path)

    def test_check_format_with_invalid_format(self):
        """
        Test the check_format method with a file having an invalid format.
        Verifies that an InvalidFileFormat exception is raised.
        """
        with self.assertRaises(InvalidFileFormat):
            Load.check_formart(self.invalid_file_path)

    def test_check_file_existence_with_existing_file(self):
        """
        Test the check_file_existence method with an existing file.
        Ensures that no exception is raised for an existing file.
        """
        with patch('os.path.exists', return_value=True):
            Load.check_file_existence(self.valid_file_path)

    def test_check_file_existence_with_nonexistent_file(self):
        """
        Test the check_file_existence method with a nonexistent file.
        Verifies that a FileNotFoundError exception is raised.
        """
        with patch('os.path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                Load.check_file_existence(self.nonexistent_file_path)

    def test_check_file_structure_with_valid_data(self):
        """
        Test the check_file_structure method with valid data.
        Ensures that no exception is raised for a valid data structure.
        """
        Load.check_file_structure(self.valid_data)

    def test_check_file_structure_with_invalid_data(self):
        """
        Test the check_file_structure method with invalid data structure.
        Verifies that an InvalidFileStructure exception is raised.
        """
        with self.assertRaises(InvalidFileEstucture):
            Load.check_file_structure(self.invalid_data_structure)

    def test_check_duplicate_project_name_with_no_duplicates(self):
        """
        Test the check_duplicate_project_name method with no duplicate project names.
        Ensures that no exception is raised when there are no duplicates.
        """
        self.user.remove_project(self.user.projects[0])

        new_project = Project(self.user, 'Projeto 3', '2023-01-01', 'Descrição do Projeto 2')
        self.assertIn(new_project, self.user.projects)
        try:
            Load.check_duplicate_project_name(self.user, self.valid_data)
        except ItemNameAlreadyExists:
            self.fail("check_duplicate_project_name levantou ItemNameAlreadyExists inesperadamente!")

    def test_check_duplicate_project_name_with_duplicates(self):
        """
        Test the check_duplicate_project_name method with duplicate project names.
        Verifies that an ItemNameAlreadyExists exception is raised with duplicate names.
        """
        project = Project(self.user, name='Projeto 1', end_date='2023-01-01', description='Descrição do Projeto 1')
        self.assertIn(project, self.user.projects)

        with self.assertRaises(ItemNameAlreadyExists):
            Load.check_duplicate_project_name(self.user, self.valid_data)

    def test_check_project_name_blank_with_no_blank_names(self):
        """
        Test the check_project_name_blank method with no blank project names.
        Ensures that no exception is raised when project names are not blank.
        """
        Load.check_project_name_blank(self.valid_data)

    def test_check_project_name_blank_with_blank_names(self):
        """
        Test the check_project_name_blank method with blank project names.
        Verifies that an ItemNameBlank exception is raised when project names are blank.
        """
        data_with_blank_name = [{"project": "", "end_date": "2023-01-01", "description": "Descrição", "tasks": []}]
        with self.assertRaises(ItemNameBlank):
            Load.check_project_name_blank(data_with_blank_name)

    def test_json_reader_with_valid_data(self):
        """
        Test the json_reader method with valid data.
        Ensures that the user's projects are correctly loaded from the file.
        """
        for project in self.user.projects:
            self.user.remove_project(project)
        
        Load.json_reader(self.user, self.valid_file_path)
        self.assertEqual(len(self.user.projects), 3)
        self.assertEqual(len(self.user.projects[0].tasks), 1)
        self.assertEqual(len(self.user.projects[0].tasks[0].subtasks), 0)

