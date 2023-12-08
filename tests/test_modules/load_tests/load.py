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

class TestLoad(unittest.TestCase):

    def setUp(self):
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
        # Testar o método check_format com um formato de arquivo válido
        Load.check_formart(self.valid_file_path)

    def test_check_format_with_invalid_format(self):
        # Testar o método check_format com um formato de arquivo inválido
        with self.assertRaises(InvalidFileFormat):
            Load.check_formart(self.invalid_file_path)

    def test_check_file_existence_with_existing_file(self):
        # Testar o método check_file_existence com um arquivo existente
        with patch('os.path.exists', return_value=True):
            Load.check_file_existence(self.valid_file_path)

    def test_check_file_existence_with_nonexistent_file(self):
        # Testar o método check_file_existence com um arquivo inexistente
        with patch('os.path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                Load.check_file_existence(self.nonexistent_file_path)

    def test_check_file_structure_with_valid_data(self):
        # Testar o método check_file_structure com dados válidos
        Load.check_file_structure(self.valid_data)

    def test_check_file_structure_with_invalid_data(self):
        # Testar o método check_file_structure com dados inválidos
        with self.assertRaises(InvalidFileEstucture):
            Load.check_file_structure(self.invalid_data_structure)

    def test_check_duplicate_project_name_with_no_duplicates(self):
        # Testar o método check_duplicate_project_name sem duplicatas
        # preciso fazer por user ser um singleton
        self.user.remove_project(self.user.projects[0])

        new_project = Project(self.user, 'Projeto 3', '2023-01-01', 'Descrição do Projeto 2')
        self.assertIn(new_project, self.user.projects)
        try:
            Load.check_duplicate_project_name(self.user, self.valid_data)
        except ItemNameAlreadyExists:
            self.fail("check_duplicate_project_name levantou ItemNameAlreadyExists inesperadamente!")

    def test_check_duplicate_project_name_with_duplicates(self):
        # Testar o método check_duplicate_project_name com duplicatas
        project = Project(self.user, name='Projeto 1', end_date='2023-01-01', description='Descrição do Projeto 1')
        self.assertIn(project, self.user.projects)

        with self.assertRaises(ItemNameAlreadyExists):
            Load.check_duplicate_project_name(self.user, self.valid_data)

    def test_check_project_name_blank_with_no_blank_names(self):
        # Testar o método check_project_name_blank sem nomes em branco
        Load.check_project_name_blank(self.valid_data)

    def test_check_project_name_blank_with_blank_names(self):
        # Testar o método check_project_name_blank com nomes em branco
        data_with_blank_name = [{"project": "", "end_date": "2023-01-01", "description": "Descrição", "tasks": []}]
        with self.assertRaises(ItemNameBlank):
            Load.check_project_name_blank(data_with_blank_name)

    def test_json_reader_with_valid_data(self):
        # Testar o método json_reader com dados válidos
        for project in self.user.projects:
            self.user.remove_project(project)
        
        Load.json_reader(self.user, self.valid_file_path)
        self.assertEqual(len(self.user.projects), 3)
        self.assertEqual(len(self.user.projects[0].tasks), 1)
        self.assertEqual(len(self.user.projects[0].tasks[0].subtasks), 0)

