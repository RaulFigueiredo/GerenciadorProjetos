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
                    if project.creation_date is not None]
        return [project for project in projects
                if project.creation_date >= lower_limit
                and project.creation_date <= upper_limit]

    def filter_projects_by_end_date(self, lower_limit, upper_limit):
        projects = [project for project in self.user.projects
                    if project.end_date is not None]
        return [project for project in projects
                if project.end_date >= lower_limit
                and project.end_date <= upper_limit]

    def filter_projects_by_conclusion_date(self, lower_limit, upper_limit):
        projects = [project for project in self.user.projects
                    if project.conclusion_date is not None]
        return [project for project in projects
                if project.conclusion_date >= lower_limit
                and project.conclusion_date <= upper_limit]

    def filter_projects_by_status(self, status):
        return [project for project in self.user.projects
                if project.status == status]

    def filter_label_by_name(self, name):
        for label in self.user.labels:
            if label.name == name:
                return label
        return None
