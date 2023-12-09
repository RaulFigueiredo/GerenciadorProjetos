import json
import tempfile
import csv
import os
from typing import List
from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.load import Load
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError
import ast

class FileAdapter:
    @staticmethod
    def read_file(user, file_path):
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
        """
        Converts a TXT file where each line is a JSON object into a format that can be read by json_reader.

        :param file_path: Path to the TXT file.
        :return: String representation of the JSON list.
        """
        combined_data = []
        with open(file_path, 'r') as txt_file:
            for line in txt_file:
                try:
                    json_object = json.loads(line.strip())
                    combined_data.append(json_object)
                except json.JSONDecodeError:
                    raise InvalidFileFormat("Invalid content in TXT file. Unable to convert to JSON.")

        return json.dumps(combined_data)
    
    @staticmethod
    def convert_csv_to_json(file_path: str) -> str:
        projects = {}
        tasks = {}

        with open(file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                item_type = row['type'].strip()
                parent = row['parent'].strip()
                name = row['name'].strip()

                if item_type == 'project':
                    projects[name] = {
                        'project': name,
                        'description': row['description'].strip(),
                        'end_date': row['end_date'].strip() if row['end_date'].strip() else None,
                        'tasks': []
                    }

                elif item_type == 'task':
                    task_info = {
                        'task': name,
                        'description': row['description'].strip(),
                        'end_date': row['end_date'].strip() if row['end_date'].strip() else None,
                        'notification_date': row['notification_date'].strip() if row['notification_date'].strip() else None,
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
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_file.write(json_data.encode('utf-8'))
            return temp_file.name
