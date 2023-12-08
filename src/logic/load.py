import json
import os
from typing import List
from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError

class Load:
    @staticmethod
    def json_reader(user: IUser,file_path: str) -> None:

        Load.check_file_existence(file_path)
        Load.check_formart(file_path)

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        Load.check_file_structure(data)
        Load.check_project_name_blank(data)
        Load.check_task_name_black(data)
        Load.check_duplicate_project_name(user, data)

        for each_project in data:
            projet = ItemFactory.create_item(item_type = 'project',
                                              user = user,
                                              name = each_project['project'],
                                              end_date = each_project['end_date'],
                                              description = each_project['description'])
            
            for each_task in each_project['tasks']:
                task = ItemFactory.create_item( item_type = 'task', 
                                                project = projet,
                                                name = each_task['task'],
                                                priority = each_task['priority'],
                                                end_date = each_task['end_date'],
                                                notification_date = each_task['notification_date'],
                                                description = each_task['description'])
                
                for each_subtask in each_task['subtasks']:
                    print(task)
                    subtask = ItemFactory.create_item(item_type = 'subtask',
                                           task = task,
                                           name = each_subtask['subtask'])
                                           
    @staticmethod
    def check_formart(file_path: str):
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() != '.json':
            raise InvalidFileFormat("O arquivo fornecido não é um arquivo JSON.")

    def check_file_existence(file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError("É necessário selecionar um arquivo.")

    @staticmethod
    def check_file_structure(data: List):
        if not isinstance(data, list):
            raise InvalidFileEstucture("Estrutura de arquivo inválida")

        for project in data:
            if not all(key in project for key in ['project', 'end_date', 'description', 'tasks']):
                raise InvalidFileEstucture("Formato de projeto inválido.")

            if not isinstance(project['tasks'], list):
                raise InvalidFileEstucture("Formato inválido: 'tasks' deve ser uma lista.")

            for task in project['tasks']:
                if not all(key in task for key in ['task', 'priority', 'end_date', 'notification_date', 'description', 'subtasks']):
                    raise InvalidFileEstucture("Formato de tarefa inválido.")
                
                if not isinstance(task['subtasks'], list):
                    raise InvalidFileEstucture("Formato inválido: 'subtasks' deve ser uma lista.")

    
    @staticmethod
    def check_duplicate_project_name(user, data):
        for each_project in data:
            if each_project['project'] in [project.name for project in user.projects]:
                erro_str = "Você ja possui um projeto com o nome: "+each_project['project']+""
                erro_str += "\nPor favor, altere o nome do projeto e tente novamente."
                raise ItemNameAlreadyExists(erro_str)
            
    @staticmethod
    def check_project_name_blank(data):
        for each_project in data:
            if each_project['project'] == '':
                erro_str = "O nome de algum projeto para importar está em branco."
                raise ItemNameBlank(erro_str)
            
    @staticmethod
    def check_task_name_black(data):
        for each_project in data:
            for each_task in each_project['tasks']:
                if each_task['task'] == '':
                    erro_str = "O nome de alguma tarefa para importar está em branco."
                    raise ItemNameBlank(erro_str)



                

if __name__ == '__main__':
    user = User('ronaldo')
    Load.json_reader('/home/raul/Documents/EngSoft/GerenciadorProjetos/src/logic/teste_export.json', user)
    print('+'*30)
    print(user.projects)
    print('+'*30)
    print(user.projects[0].tasks)
    print('+'*30)

            