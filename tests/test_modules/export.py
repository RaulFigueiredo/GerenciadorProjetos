import unittest
from unittest.mock import patch, MagicMock
from unittest.mock import patch, mock_open  # Importação correta aqui
from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import EmptyListProjects,\
                                                   FileNameBlank,\
                                                   DirectoryBlank
from src.logic.export import Export
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
import os



class TestExport(unittest.TestCase):

    def setUp(self):
        user = User(name="Usuário Exemplo")
        pj_1 = Project(name="Projeto Exemplo 1", user=user, description='Esse é um projeto de exemplo (1)')
        pj_2 = Project(name="Projeto Exemplo 2", user=user, description='Esse é um projeto de exemplo (2)')
        pj_3 = Project(name="Projeto Exemplo 3", user=user, description='Esse é um projeto de exemplo (3)')

        t1 = Task(name="Tarefa Exemplo 1", project=pj_1, description='Essa é uma tarefa de exemplo (1)')
        t2 = Task(name="Tarefa Exemplo 2", project=pj_1, description='Essa é uma tarefa de exemplo (2)')

        self.projects_list = [pj_1, pj_2, pj_3]

    def test_json_generator_valid_input(self):
        with patch('builtins.open', new_callable=mock_open()), patch('os.makedirs'), patch('os.path.exists', return_value=True):
            Export.json_generator(self.projects_list, 'test_file', 'test_directory')

    def test_json_generator_empty_list(self):
        with self.assertRaises(EmptyListProjects):
            Export.json_generator([], 'test_file', 'test_directory')

    def test_json_generator_blank_filename(self):
        with self.assertRaises(FileNameBlank):
            Export.json_generator(self.projects_list, '', 'test_directory')

    def test_json_generator_blank_directory(self):
        with self.assertRaises(DirectoryBlank):
            Export.json_generator(self.projects_list, 'test_file', '')

    def test_check_data_non_empty(self):
        try:
            Export.check_data(self.projects_list)
        except Exception as e:
            self.fail(f"check_data raised an unexpected exception: {e}")

    def test_check_data_empty(self):
        with self.assertRaises(EmptyListProjects):
            Export.check_data([])

    def test_check_filename_non_empty(self):
        try:
            Export.check_filename('test_file')
        except Exception as e:
            self.fail(f"check_filename raised an unexpected exception: {e}")

    def test_check_filename_empty(self):
        with self.assertRaises(FileNameBlank):
            Export.check_filename('')

    def test_check_directory_non_empty(self):
        try:
            Export.check_directory('test_directory')
        except Exception as e:
            self.fail(f"check_directory raised an unexpected exception: {e}")

    def test_check_directory_empty(self):
        with self.assertRaises(DirectoryBlank):
            Export.check_directory('')

if __name__ == '__main__':
    unittest.main()