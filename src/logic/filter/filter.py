"""
Module providing a Filter class for managing and filtering projects and tasks based
on various criteria.

This module includes a class, Filter, designed to handle project and task filtering based
on different parameters:
    - Filtering projects by name or similar names.
    - Filtering projects by creation date, end date, conclusion date, status, and label name.
    - Filtering tasks within projects by creation date, end date, conclusion date, and status.

Usage:
    - Initialize the Filter class by providing a user object containing project and task
information.
    - Utilize different methods to filter projects or tasks based on specific criteria by providing:
        - Criteria such as name, date ranges, status, or label name.
        - Projects or tasks to be filtered.

Example:
    # Initialize Filter with a user object
    filter = Filter(user)

    # Filter projects by name
    project = filter.filter_project_by_name('ProjectX')

    # Filter projects by similar name
    similar_projects = filter.filter_projects_by_similar_name('Project')

    # Filter projects by creation date range
    filtered_projects = filter.filter_projects_by_creation_date(projects_list, start_date, end_date)

    # Filter tasks by creation date range
    filtered_tasks = filter.filter_tasks_by_creation_date(projects_list, start_date, end_date)

Note:
    - Ensure the provided user object contains projects and tasks.
    - Methods return filtered lists of projects or tasks based on the specified criteria.
"""

from datetime import date

class Filter:
    """ Filter class
    """
    def __init__(self, user: callable) -> None:
        """ Initialize the class

        Args:
            user (callable): User
        """
        self.user = user

    # pylint: disable=pointless-string-statement
    '''
    - step 1
    def filter_project_by_name(self, name):
        pass

    - step 2
    def filter_project_by_name(self, name):
        for project in self.user.projects:
            if project.name == name:
                pass
    
    - step 3
    def filter_project_by_name(self, name):
        for project in self.user.projects:
            if project.name == name:
                return project
        return None
    '''

    def filter_project_by_name(self, name: str) -> callable:
        """ Filter project by name

        Args:
            name (str): Name of the project

        Returns:
            Project: Project
        """
        for project in self.user.projects:
            if project.name == name:
                return project
        return None

    def filter_projects_by_similar_name(self, name: str) -> list:
        """ Filter projects by similar name

        Args:
            name (str): Name of the project

        Returns:
            list: List of projects
        """
        return [project for project in self.user.projects if name in project.name]

    def filter_projects_by_creation_date(
            self,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by creation date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower Limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper Limit. Defaults to date(9999,12,31).

        Returns:
            list: List of projects
        """
        projects = [project for project in self.user.projects
                    if isinstance(project.creation_date, date)]
        return [project for project in projects
                if project.creation_date >= lower_limit
                and project.creation_date <= upper_limit]

    def filter_projects_by_end_date(
            self,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by end date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower Limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper Limit. Defaults to date(9999,12,31).

        Returns:
            list: List of projects
        """
        projects = [project for project in self.user.projects
                    if isinstance(project.end_date, date)]
        return [project for project in projects
                if project.end_date >= lower_limit
                and project.end_date <= upper_limit]

    def filter_projects_by_conclusion_date(
            self,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by conclusion date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower Limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper Limit. Defaults to date(9999,12,31).

        Returns:
            list: list of projects
        """
        projects = [project for project in self.user.projects
                    if isinstance(project.conclusion_date, date)]
        return [project for project in projects
                if project.conclusion_date >= lower_limit
                and project.conclusion_date <= upper_limit]

    def filter_projects_by_status(self, status: str) -> list:
        """ Filter projects by status

        Args:
            status (str): Status of the project

        Returns:
            list: List of projects
        """
        return [project for project in self.user.projects
                if project.status == status]

    def filter_projects_by_label_name(self, name: str) -> list:
        """ Filter projects by label name

        Args:
            name (str): Name of the label

        Returns:
            list: List of projects
        """
        valid_projects = [project for project in self.user.projects if project.label is not None]
        return [project for project in valid_projects if project.label.name == name]

    def filter_tasks_by_creation_date(
            self,
            projects: list,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by creation date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower Limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper Limit. Defaults to date(9999,12,31).

        Returns:
            list: _description_
        """
        valid_tasks = []
        for project in projects:
            valid_tasks += [task for task in project.tasks if isinstance(task.creation_date, date)]
        tasks = []
        for task in valid_tasks:
            if task.creation_date >= lower_limit and task.creation_date <= upper_limit:
                tasks.append(task)
        return tasks

    def filter_tasks_by_end_date(
            self,
            projects: list,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by end date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower Limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper Limit. Defaults to date(9999,12,31).

        Returns:
            list: _description_
        """
        valid_tasks = []
        for project in projects:
            valid_tasks += [task for task in project.tasks if isinstance(task.end_date, date)]
        tasks = []
        for task in valid_tasks:
            if task.end_date >= lower_limit and task.end_date <= upper_limit:
                tasks.append(task)
        return tasks

    def filter_tasks_by_conclusion_date(
            self,
            projects: list,
            lower_limit: date =date(1,1,1),
            upper_limit: date =date(9999,12,31)
        ) -> list:
        """ Filter tasks by conclusion date

        Args:
            projects (list): List of projects
            lower_limit (date, optional): Lower limit. Defaults to date(1,1,1).
            upper_limit (date, optional): Upper limit. Defaults to date(9999,12,31).

        Returns:
            list: _description_
        """
        valid_tasks = []
        for project in projects:
            valid_tasks +=[task for task in project.tasks if isinstance(task.conclusion_date, date)]
        tasks = []
        for task in valid_tasks:
            if task.conclusion_date >= lower_limit and task.conclusion_date <= upper_limit:
                tasks.append(task)
        return tasks

    def filter_tasks_by_status(self, projects: list, status: str) -> list:
        """ Filter tasks by status

        Args:
            projects (list): List of projects
            status (str): Status of the task

        Returns:
            list: List of tasks
        """
        tasks = []
        for project in projects:
            for task in project.tasks:
                if task.status == status:
                    tasks.append(task)
        return tasks
