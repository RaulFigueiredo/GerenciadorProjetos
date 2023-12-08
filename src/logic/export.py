from src.logic.items.item_interface import IItem
import json
import os
from typing import List

class Export:
    @staticmethod
    def json_generator(list_projects: List[IItem], name_file: str, directory: str) -> None:
        projects_data = []

        for project in list_projects:
            project_info = {
                "project": project.name,
                "label": project.label,
                "end_date": project.end_date,
                "creation_date": project.description,
                "tasks": []
            }

            for task in project.tasks:
                task_info = {
                    "task": task.name,
                    "priority": task.priority,
                    "end_date": task.end_date,
                    "notification_date": task.notification_date
                }
                project_info["tasks"].append(task_info)

            projects_data.append(project_info)

        # Cria o diretório se não existir
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Caminho completo para o arquivo
        file_path = os.path.join(directory, name_file)

        # Escreve o JSON no arquivo
        with open(file_path, 'w') as json_file:
            json.dump(projects_data, json_file, indent=4)
