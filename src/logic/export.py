from src.logic.items.item_interface import IItem
from src.logic.execeptions.exceptions_items import EmptyListProjects,\
                                                   FileNameBlank,\
                                                   DirectoryBlank
import json
import os
from typing import List
from datetime import datetime


"""
This module contains the Export class, responsible for generating JSON files from a list of projects.
Each project is converted into a dictionary containing details of the project and its associated tasks.
"""

class Export:
    """ Class responsible for exporting project data to a JSON file. """


    @staticmethod
    def json_generator( list_projects: List[IItem], name_file: str, directory: str) -> None:
        """
        Generates a JSON file from a list of projects.

        :param list_projects: List of IItem objects representing projects.
        :param file_name: Name of the JSON file to be created.
        :param directory: Directory where the JSON file will be saved.
        :raises EmptyListProjects: If the list of projects is empty.
        :raises FileNameBlank: If the file name is empty.
        :raises DirectoryBlank: If the directory is empty.
        """
        projects_data = []
        Export.check_filename(name_file)

        Export.check_directory(directory)

        Export.check_data(list_projects)

        for project in list_projects:
            end_date = Export.date_converter(project.end_date)
            project_info = {
                "project": project.name,
                "end_date": end_date,
                "description": project.description,
                "tasks": []
            }
            for task in project.tasks:
                end_date = Export.date_converter(task.end_date)
                notification_date = Export.date_converter(task.notification_date)
                task_info = {
                    "task": task.name,
                    "priority": task.priority,
                    "end_date": end_date,
                    "notification_date": notification_date,
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
        """ Checks if the list of projects is empty."""
        if list_projects == []:
            raise EmptyListProjects("The list of projects to export is empty.")

    @staticmethod
    def check_filename(name_file: str) -> None:
        """ Checks if the file name is empty."""
        if name_file == '':
            raise FileNameBlank("File name cannot be empty.")
        
    @staticmethod
    def check_directory(directory: str) -> None:
        """ Checks if the directory is empty."""
        if directory == '':
            raise DirectoryBlank("Directory must be selected.")
        
    @staticmethod
    def date_converter(date: str) -> datetime:
        if date is not None:
            new_date = datetime.strptime(date, '%d/%m/%Y').date()
            new_date = new_date.strftime('%d/%m/%Y')
        else:
            new_date = None
        return new_date