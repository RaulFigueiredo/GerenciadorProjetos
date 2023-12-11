"""
Module Name: File Adapter

Description:
This module provides functionality to read and process data from various file formats
into the application. It contains methods for reading JSON, TXT, and CSV files.

- Imports necessary libraries: 'json', 'tempfile', 'csv', 'os'.
- Imports specific classes and exceptions: 'User', 'Load', 'InvalidFileFormat',
  'InvalidFileEstucture'.
- Defines the 'FileAdapter' class with methods for reading different file formats.

- Raises 'InvalidFileFormat' if the file format is unsupported.
- Raises 'InvalidFileEstucture' if the file structure is invalid.

Methods:
    - read_file(user, file_path): Reads a file and loads data into the application
based on the file format.
    - convert_txt_to_json(file_path): Converts TXT file data to JSON format.
    - convert_csv_to_json(file_path): Converts CSV file data to JSON format.
    - save_to_temp_file(json_data): Saves JSON data to a temporary file and returns the file path.
"""

import json
import tempfile
import csv
import os
#from typing import List
#from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.load import Load
#from src.logic.items.item_factory import ItemFactory
# pylint: disable=redefined-builtin
from src.logic.execeptions.exceptions_items import InvalidFileFormat,\
                                                    InvalidFileEstucture

class FileAdapter:
    """ Contains methods to read and process data from JSON files.

    Raises:
        InvalidFileFormat: If the file has an invalid format.
        InvalidFileEstucture: If the file has an invalid structure.

    Returns:
        _type_: The return value. Use ``None`` for nothing.
    """
    @staticmethod
    def read_file(user: User, file_path: str) -> None:
        """ Reads a file and loads the data into the application.

        Args:
            user (callable): The current user.
            file_path (str): The path to the file.

        Raises:
            InvalidFileFormat: If the file has an invalid format.

        Returns:
            _type_: The return value. Use ``None`` for nothing.
        """
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.json':
            return Load.json_reader(user, file_path)
        elif file_extension.lower() == '.txt':
            data = FileAdapter.convert_txt_to_json(file_path)
            temp_file_path = FileAdapter.save_to_temp_file(data)
            return Load.json_reader(user, temp_file_path)
        elif file_extension.lower() == '.csv':
            data = FileAdapter.convert_csv_to_json(file_path)
            temp_file_path = FileAdapter.save_to_temp_file(data)
            return Load.json_reader(user, temp_file_path)
        else:
            raise InvalidFileFormat("Unsupported file format.")

    @staticmethod
    def convert_txt_to_json(file_path: str) -> str:
        """ Converts a TXT file to a JSON file.

        Args:
            file_path (str): The path to the TXT file.

        Raises:
            InvalidFileEstucture: If the TXT file has an invalid structure.

        Returns:
            str: The JSON data.
        """
        combined_data = []
        with open(file_path, 'r', encoding="utf8") as txt_file:
            for line in txt_file:
                try:
                    json_object = json.loads(line.strip())

                    combined_data.append(json_object)
                except json.decoder.JSONDecodeError as exc:
                    raise InvalidFileEstucture("Invalid content in TXT file.") from exc

        return json.dumps(combined_data)

    @staticmethod
    def convert_csv_to_json(file_path: str) -> str:
        """ Converts a CSV file to a JSON file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            str: The JSON data.
        """
        projects = {}
        tasks = {}

        with open(file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                item_type = row['type'].strip()
                parent = row['parent'].strip()
                name = row['name'].strip()

                end_date = Load.date_converter(row['end_date'].strip())
                end_date_str = end_date.isoformat() if end_date else None

                notification_date = Load.date_converter(row['notification_date'].strip())
                notification_date_str = notification_date.isoformat() if notification_date else None

                if item_type == 'project':
                    projects[name] = {
                        'project': name,
                        'description': row['description'].strip(),
                        'end_date': end_date_str,
                        'tasks': []
                    }

                elif item_type == 'task':
                    task_info = {
                        'task': name,
                        'description': row['description'].strip(),
                        'end_date': end_date_str,
                        'notification_date': notification_date_str,
                        'priority': row['priority'].strip() if row['priority'].strip() else None,
                        'subtasks': []
                    }
                    tasks[name] = task_info
                    if parent in projects:
                        projects[parent]['tasks'].append(task_info)

                elif item_type == 'subtask':
                    subtask_info = {'subtask': name}
                    if parent in tasks:
                        tasks[parent]['subtasks'].append(subtask_info)

        return json.dumps(list(projects.values()), indent=4)

    @staticmethod
    def save_to_temp_file(json_data: str) -> str:
        """ Saves the given JSON data to a temporary file and returns the path to the file.

        Args:
            json_data (str): The JSON data to be saved.

        Returns:
            str: The path to the temporary file.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_file.write(json_data.encode('utf-8'))
            return temp_file.name
