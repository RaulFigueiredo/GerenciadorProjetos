from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import EmptyListProjects,\
                                                   FileNameBlank,\
                                                   DirectoryBlank
import json
import os
from typing import List

class Export:
    @staticmethod
    def json_generator( list_projects: List[IItem], name_file: str, directory: str) -> None:
        projects_data = []

        Export.check_filename(name_file)

        Export.check_directory(directory)

        Export.check_data(list_projects)

        for project in list_projects:
            project_info = {
                "project": project.name,
                "end_date": project.end_date,
                "description": project.description,
                "tasks": []
            }

            for task in project.tasks:
                task_info = {
                    "task": task.name,
                    "priority": task.priority,
                    "end_date": task.end_date,
                    "notification_date": task.notification_date,
                    "description": task.description,
                    "subtasks": []
                }
                
                for subtask in task.subtasks:
                    subtask_info = {
                        "subtask": subtask.name,
                    }
                    task_info["subtasks"].append(subtask_info)

                project_info["tasks"].append(task_info)

            projects_data.append(project_info)

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, name_file+'.json')

        with open(file_path, 'w') as json_file:
            json.dump(projects_data, json_file, indent=4)

    @staticmethod
    def check_data(list_projects: List[IItem]) -> None:
        if list_projects == []:
            raise EmptyListProjects("Lista de projetos para exportar está vazia.")

    @staticmethod
    def check_filename(name_file: str) -> None:
        if name_file == '':
            raise FileNameBlank("Nome do arquivo não pode ser vazio.")
        
    @staticmethod
    def check_directory(directory: str) -> None:
        if directory == '':
            raise DirectoryBlank("Diretório precisa ser selecionado.")