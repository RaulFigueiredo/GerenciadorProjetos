import datetime
import pandas as pd
from src.logic.filter.filter import Filter


class DashboardData:
    def __init__(self, user):
        self.user = user
        self.projects = user.projects
        self.filter = Filter(user)
    
    def update_data(self, project_name='Todos'):
        if project_name == 'Todos':
            self.projects = self.user.projects
        else:
            self.projects = [self.filter.filter_project_by_name(project_name)]

    def get_number_of_tasks(self):
        tasks = []
        for project in self.projects:
            tasks += project.tasks
        return len(tasks)

    def get_number_of_done_tasks(self):
        return len(self.filter.filter_tasks_by_status(self.projects, True))
    
    def get_number_of_on_time_tasks(self):
        today = datetime.datetime.today().date()
        on_time = self.filter.filter_tasks_by_end_date(self.projects, upper_limit=today)
        return len([task for task in on_time if not task.status])

    def get_number_of_for_today_tasks(self):
        today = datetime.datetime.today().date()
        end_today_tasks = self.filter.filter_tasks_by_end_date(self.projects, today, today)
        return len([task for task in end_today_tasks if not task.status])

    def get_number_of_late_tasks(self):
        yesterday = (datetime.datetime.today() - pd.DateOffset(days=1)).date()
        late_tasks = self.filter.filter_tasks_by_end_date(self.projects, upper_limit=yesterday)
        return len([task for task in late_tasks if not task.status])

    '''
    - step 1
    def get_timespan_of_tasks(self):
        tasks = [task for task in self.projects
                 if task.creation_date is not None
                 and task.end_date is not None]
    - step 2
    def get_timespan_of_tasks(self):
        tasks = [task for task in self.projects
                 if task.creation_date is not None
                 and task.end_date is not None]
        days_diffs = list(map(lambda x: x.end_date - x.creation_date, tasks))
    - step 3
    def get_timespan_of_tasks(self):
        tasks = [task for task in self.projects
                 if task.creation_date is not None
                 and task.end_date is not None]
        days_diffs = list(map(lambda x: x.end_date - x.creation_date, tasks))
        data = {'até 1': 0, '1 a 2': 0, '2 a 3': 0, '3+': 0}
        for days_diff in days_diffs:
            if days_diff <= 7:
                pass
            elif days_diff <= 14:
                pass
            elif days_diff <= 21:
                pass
            else:
                pass
    - step 4
    def get_timespan_of_tasks(self):
        tasks = [task for task in self.projects
                 if task.creation_date is not None
                 and task.end_date is not None]
        days_diffs = list(map(lambda x: x.end_date - x.creation_date, tasks))
        data = {'até 1': 0, '1 a 2': 0, '2 a 3': 0, '3+': 0}
        for days_diff in days_diffs:
            if days_diff <= 7:
                data['até 1'] += 1
            elif days_diff <= 14:
                data['1 a 2'] += 1
            elif days_diff <= 21:
                data['2 a 3'] += 1
            else:
                data['3+'] += 1
        return data
    '''
    def get_timespan_of_tasks(self):
        tasks = [task for task in self.projects
                 if task.creation_date is not None
                 and task.end_date is not None]
        days_diffs = list(map(lambda x: (x.end_date - x.creation_date).days, tasks))
        data = {'até 1': 0, '1 a 2': 0, '2 a 3': 0, '3+': 0}
        for days_diff in days_diffs:
            if days_diff <= 7:
                data['até 1'] += 1
            elif days_diff <= 14:
                data['1 a 2'] += 1
            elif days_diff <= 21:
                data['2 a 3'] += 1
            else:
                data['3+'] += 1
        return data
    
    def get_next_deadlines(self):
        today = datetime.datetime.today().date()
        tasks = self.filter.filter_tasks_by_end_date(self.projects, today)
        days_diffs = list(map(lambda x: (x.end_date - today).days, tasks))
        data = {'até 1': 0, '1 a 2': 0, '2 a 3': 0, '3+': 0}
        for days_diff in days_diffs:
            if days_diff <= 7:
                data['até 1'] += 1
            elif days_diff <= 14:
                data['1 a 2'] += 1
            elif days_diff <= 21:
                data['2 a 3'] += 1
            else:
                data['3+'] += 1
        return data
    
    def get_created_tasks(self):
        today = datetime.datetime.today().date()
        one_month_ago = (datetime.datetime.today() - pd.DateOffset(days=30)).date()
        day = one_month_ago
        data = {}
        while day <= today:
            data[day.strftime('%d-%m-%Y')] = 0
            day = (day + pd.DateOffset(days=1)).date()
        created_tasks = self.filter.filter_tasks_by_creation_date(self.projects, one_month_ago)
        dates = [task.creation_date.strftime('%d-%m-%Y') for task in created_tasks]
        total = 0
        for date in data.keys():
            total += dates.count(date)
            data[date] = total 
        return data
    
    def get_finished_by_weekday(self):
        finished_tasks = self.filter.filter_tasks_by_status(self.projects, True)
        week_days = list(map(lambda x: x.conclusion_date.weekday(), finished_tasks))
        data = {'seg': 0, 'ter': 0, 'qua': 0, 'qui': 0, 'sex': 0, 'sab': 0, 'dom': 0}
        for day in week_days:
            if day == 0:
                data['seg'] += 1
            elif day == 1:
                data['ter'] += 1
            elif day == 2:
                data['qua'] += 1
            elif day == 3:
                data['qui'] += 1
            elif day == 4:
                data['sex'] += 1
            elif day == 5:
                data['sab'] += 1
            elif day == 6:
                data['dom'] += 1
        return data
