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
        """
        Converts a CSV file into a format that can be read by json_reader.

        :param file_path: Path to the CSV file.
        :return: String representation of the JSON list.
        """
        data = []
        with open(file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if 'tasks' in row and row['tasks']:
                    tasks_json = row['tasks'].replace("'", '"').replace("None", "null")
                    try:
                        tasks = json.loads(tasks_json)
                        for task in tasks:
                            if 'subtasks' in task:
                                if isinstance(task['subtasks'], str):
                                    subtasks_str = task['subtasks'].replace("'", '"').replace("None", "null")
                                    try:
                                        task['subtasks'] = json.loads(subtasks_str)
                                    except json.JSONDecodeError:
                                        task['subtasks'] = []
                                elif task['subtasks'] is None:
                                    task['subtasks'] = []
                                # Garanta que todas as subtasks sejam listas de dicionários
                                if not all(isinstance(subtask, dict) for subtask in task['subtasks']):
                                    task['subtasks'] = [{'subtask': subtask} if isinstance(subtask, str) else subtask for subtask in task['subtasks']]
                            else:
                                task['subtasks'] = []
                        row['tasks'] = tasks
                    except json.JSONDecodeError:
                        raise InvalidFileFormat(f"Invalid JSON format in tasks: {tasks_json}")
                else:
                    row['tasks'] = []

                data.append(row)

        return json.dumps(data)

    
    @staticmethod
    def save_to_temp_file(json_data: str) -> str:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_file.write(json_data.encode('utf-8'))
            return temp_file.name
