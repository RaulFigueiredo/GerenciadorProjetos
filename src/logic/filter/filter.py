from datetime import date

class Filter:
    def __init__(self, user):
        self.user = user

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

    def filter_project_by_name(self, name):
        for project in self.user.projects:
            if project.name == name:
                return project
        return None

    def filter_projects_by_creation_date(self, lower_limit, upper_limit):
        projects = [project for project in self.user.projects
                    if isinstance(project.creation_date, date)]
        return [project for project in projects
                if project.creation_date >= lower_limit
                and project.creation_date <= upper_limit]

    def filter_projects_by_end_date(self, lower_limit, upper_limit):
        projects = [project for project in self.user.projects
                    if isinstance(project.end_date, date)]
        return [project for project in projects
                if project.end_date >= lower_limit
                and project.end_date <= upper_limit]

    def filter_projects_by_conclusion_date(self, lower_limit, upper_limit):
        projects = [project for project in self.user.projects
                    if isinstance(project.conclusion_date, date)]
        return [project for project in projects
                if project.conclusion_date >= lower_limit
                and project.conclusion_date <= upper_limit]

    def filter_projects_by_status(self, status):
        return [project for project in self.user.projects
                if project.status == status]

    def filter_tasks_by_creation_date(self, projects, lower_limit, upper_limit):
        valid_tasks = []
        for project in projects:
            valid_tasks += [task for task in project.tasks if isinstance(task.creation_date, date)] 
        tasks = []
        for task in valid_tasks:
            if task.creation_date >= lower_limit and task.creation_date <= upper_limit:
                tasks.append(task)
        return tasks
    
    def filter_tasks_by_end_date(self, projects, lower_limit, upper_limit):
        valid_tasks = []
        for project in projects:
            valid_tasks += [task for task in project.tasks if isinstance(task.end_date, date)] 
        tasks = []
        for task in valid_tasks:
            if task.end_date >= lower_limit and task.end_date <= upper_limit:
                tasks.append(task)
        return tasks


    def filter_tasks_by_conclusion_date(self, projects, lower_limit, upper_limit):
        valid_tasks = []
        for project in projects:
            valid_tasks += [task for task in project.tasks if isinstance(task.conclusion_date, date)] 
        tasks = []
        for task in valid_tasks:
            if task.conclusion_date >= lower_limit and task.conclusion_date <= upper_limit:
                tasks.append(task)
        return tasks
