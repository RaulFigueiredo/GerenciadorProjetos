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
from datetime import datetime 

"""
This module contains the Load class, which is responsible for reading JSON files and reconstructing project,
task, and subtask objects from the file content. It includes various checks to ensure the integrity and
correct format of the data.
"""

class Load:
    """ Class responsible for loading project data from a JSON file. """
    

    @staticmethod
    def txt_reader(user: IUser, file_path: str) -> None:
        """
        Reads a TXT file where each line is a JSON object, converts its content to JSON format, 
        and loads the data into the application.

        :param user: IUser object representing the current user.
        :param file_path: Path to the TXT file.
        :raises FileNotFoundError, InvalidFileFormat, InvalidFileStructure, ItemNameBlank, ItemNameAlreadyExists
        """

        Load.check_file_existence(file_path)

        with open(file_path, 'r') as txt_file:
            for line in txt_file:
                try:
                    each_project = json.loads(line.strip())
                    Load.check_file_structure([each_project])
                    Load.check_project_name_blank([each_project])
                    Load.check_task_name_blank([each_project])
                    Load.check_duplicate_project_name(user, [each_project])
                    end_date = Load.date_converter(each_project['end_date'])
                    project = ItemFactory.create_item(item_type='project',
                                                      user=user,
                                                      name=each_project['project'],
                                                      end_date=end_date,
                                                      description=each_project['description'])

                    for each_task in each_project['tasks']:
                        end_date = Load.date_converter(each_task['end_date'])
                        notification_date = Load.date_converter(each_task['notification_date'])
                        task = ItemFactory.create_item(item_type='task',
                                                       project=project,
                                                       name=each_task['task'],
                                                       priority=each_task['priority'],
                                                       end_date=end_date,
                                                       notification_date=notification_date,
                                                       description=each_task['description'])

                        for each_subtask in each_task['subtasks']:
                            print(task)
                            subtask = ItemFactory.create_item(item_type='subtask',
                                                              task=task,
                                                              name=each_subtask['subtask'])

                except json.JSONDecodeError:
                    raise InvalidFileFormat("Invalid content in TXT file. Unable to convert to JSON.")
    @staticmethod
    def date_converter(date: str) -> datetime:
        if date is not None:
            new_date = datetime.strptime(date, '%d/%m/%Y').date()
            new_date = new_date.strftime('%d/%m/%Y')
        else:
            new_date = None
        return new_date

    @staticmethod
    def json_reader(user: IUser,file_path: str) -> None:
        """
        Reads a JSON file and loads the data into the application.

        :param user: IUser object representing the current user.
        :param file_path: Path to the JSON file.
        :raises FileNotFoundError, InvalidFileFormat, InvalidFileStructure, ItemNameBlank, ItemNameAlreadyExists
        """

        Load.check_file_existence(file_path)
        Load.check_formart(file_path)

        with open(file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                raise InvalidFileFormat("Invalid content in JSON file.")

        Load.check_file_structure(data)
        Load.check_project_name_blank(data)
        Load.check_task_name_blank(data)
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
        """ Checks if the file has a valid format."""
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() != '.json':
            raise InvalidFileFormat("The provided file is not a JSON file.")

    @staticmethod
    def check_file_existence(file_path: str):
        """ Checks if the file exists."""
        if not os.path.exists(file_path):
            raise FileNotFoundError("A file must be selected.")

    @staticmethod
    def check_file_structure(data: List):
        """ Checks if the file structure is valid."""
        if not isinstance(data, list):
            raise InvalidFileEstucture("Invalid file structure")

        for project in data:
            if not all(key in project for key in ['project', 'end_date', 'description', 'tasks']):
                raise InvalidFileEstucture("Invalid project format.")

            if not isinstance(project['tasks'], list):
                raise InvalidFileEstucture("tasks must be a list.")

            for task in project['tasks']:
                if not all(key in task for key in ['task', 'priority', 'end_date', 'notification_date', 'description', 'subtasks']):
                    raise InvalidFileEstucture("Invalid task format.")
                
                if not isinstance(task['subtasks'], list):
                    raise InvalidFileEstucture("subtasks must be a list.")

    
    @staticmethod
    def check_duplicate_project_name(user, data):
        """ Checks if the name of some project to import already exists in the user's projects."""
        for each_project in data:
            if each_project['project'] in [project.name for project in user.projects]:
                error_str = f"You already have a project named: {each_project['project']}."
                error_str += "\nPlease change the project name and try again."
                raise ItemNameAlreadyExists(error_str)
            
    @staticmethod
    def check_project_name_blank(data):
        """ Checks if the name of some project to import is blank."""
        for each_project in data:
            if each_project['project'] == '':
                error_str = "The name of some project to import is blank."
                raise ItemNameBlank(error_str)

    @staticmethod
    def check_task_name_blank(data):
        """ Checks if the name of some task to import is blank."""
        for each_project in data:
            for each_task in each_project['tasks']:
                if each_task['task'] == '':
                    error_str = "The name of some task to import is blank."
                    raise ItemNameBlank(error_str)



                

if __name__ == '__main__':
    user = User('ronaldo')
    Load.json_reader('/home/raul/Documents/EngSoft/GerenciadorProjetos/src/logic/teste_export.json', user)
    print('+'*30)
    print(user.projects)
    print('+'*30)
    print(user.projects[0].tasks)
    print('+'*30)
