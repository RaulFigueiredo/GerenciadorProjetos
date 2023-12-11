"""Module: JSON Loader

This module provides a 'Load' class for loading data from JSON files and populating the application.

Classes:
    Load: Contains methods to read and process data from JSON files.

Functions:
    - No module-level functions documented -

Raises:
    InvalidFileFormat: Raised for invalid content in JSON files.
    InvalidFileEstucture: Raised for invalid file structure.
    FileNotFoundError: Raised when the selected file is not found.
    ItemNameAlreadyExists: Raised if a project name already exists in the user's projects.
    ItemNameBlank: Raised if a project or task name is blank.

Example Usage:
    # Example usage of json_reader method
    user = User('username')
    Load.json_reader('/path/to/file.json', user)
"""
import json
import os
from typing import List
from datetime import datetime
from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.items.item_factory import ItemFactory
# pylint: disable=redefined-builtin
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError

class Load:
    """ Contains methods to read and process data from JSON files.
    """
    @staticmethod
    def date_converter(date_str: str) -> datetime.date:
        """ Converts a date string to a datetime object.

        Tries multiple date formats.

        Args:
            date_str (str): Date string.

        Returns:
            datetime.date: Datetime object representing the date string, or None if conversion fails
        """
        if not date_str:
            return None

        for fmt in ['%d/%m/%Y', '%Y-%m-%d']:  # Adicione mais formatos aqui se necessário
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Date string does not match any expected format: {date_str}")


    @staticmethod
    def json_reader(usr: IUser,file_path: str) -> None:
        """
        Reads a JSON file and loads the data into the application.

        :param usr: IUser object representing the current usr.
        :param file_path: Path to the JSON file.
        :raises FileNotFoundError, InvalidFileFormat, InvalidFileStructure,
        ItemNameBlank, ItemNameAlreadyExists
        """

        Load.check_file_existence(file_path)
        Load.check_formart(file_path)

        with open(file_path, 'r', encoding="utf8") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError as exc:
                raise InvalidFileFormat("Invalid content in JSON file.") from exc

        Load.check_file_structure(data)
        Load.check_project_name_blank(data)
        Load.check_task_name_blank(data)
        Load.check_duplicate_project_name(usr, data)



        for each_project in data:
            project_end_date = Load.date_converter(each_project['end_date'])
            projet = ItemFactory.create_item(item_type='project',
                                            user=usr,
                                            name=each_project['project'],
                                            end_date=project_end_date,
                                            description=each_project['description'])

            for each_task in each_project['tasks']:
                task_end_date = Load.date_converter(each_task['end_date'])
                notification_date = Load.date_converter(each_task['notification_date'])
                task = ItemFactory.create_item(item_type='task',
                                            project=projet,
                                            name=each_task['task'],
                                            priority=each_task['priority'],
                                            end_date=task_end_date,
                                            notification_date=notification_date,
                                            description=each_task['description'])

                for each_subtask in each_task['subtasks']:
                    print(task)
                    # pylint: disable=unused-variable
                    subtask = ItemFactory.create_item(item_type = 'subtask',
                                           task = task,
                                           name = each_subtask['subtask'])

    @staticmethod
    def check_formart(file_path: str) -> None:
        """ Checks if the file has a valid format.
        """
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() != '.json':
            raise InvalidFileFormat("The provided file is not a JSON file.")

    @staticmethod
    def check_file_existence(file_path: str) -> None:
        """ Checks if the file exists.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("A file must be selected.")

    @staticmethod
    def check_file_structure(data: List) -> None:
        """ Checks if the file structure is valid.
        """
        if not isinstance(data, list):
            raise InvalidFileEstucture("Invalid file structure")

        for project in data:
            if not all(key in project for key in ['project', 'end_date', 'description', 'tasks']):
                raise InvalidFileEstucture("Invalid project format.")

            if not isinstance(project['tasks'], list):
                raise InvalidFileEstucture("tasks must be a list.")

            for task in project['tasks']:
                if not all(key in task for key in ['task', 'priority', 'end_date',\
                             'notification_date', 'description', 'subtasks']):
                    raise InvalidFileEstucture("Invalid task format.")

                if not isinstance(task['subtasks'], list):
                    raise InvalidFileEstucture("subtasks must be a list.")


    @staticmethod
    def check_duplicate_project_name(usr: User, data: List) -> None:
        """ Checks if the name of some project to import already exists in the user's projects.
        """
        for each_project in data:
            if each_project['project'] in [project.name for project in usr.projects]:
                error_str = f"You already have a project named: {each_project['project']}."
                error_str += "\nPlease change the project name and try again."
                raise ItemNameAlreadyExists(error_str)

    @staticmethod
    def check_project_name_blank(data: List) -> None:
        """ Checks if the name of some project to import is blank.
        """
        for each_project in data:
            if each_project['project'] == '':
                error_str = "The name of some project to import is blank."
                raise ItemNameBlank(error_str)

    @staticmethod
    def check_task_name_blank(data: List) -> None:
        """ Checks if the name of some task to import is blank.
        """
        for each_project in data:
            for each_task in each_project['tasks']:
                if each_task['task'] == '':
                    error_str = "The name of some task to import is blank."
                    raise ItemNameBlank(error_str)
