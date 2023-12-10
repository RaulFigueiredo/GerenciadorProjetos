"""
    This module contains the Notification class responsible for managing and notifying
users about various task-related events.

- The Notification class is initialized with a User object to handle notifications
for the associated user.

- Three sets - 'urgent_tasks', 'notification_date_tasks', and 'due_date_tasks'
(manage tasks categorized by urgency, notification dates, and due dates, respectively).

Methods:
    - check_notification_date(): Checks for tasks with notification dates set for the current
day and adds them to notification_date_tasks.
    - check_due_date(): Manages the process of checking tasks due today, tomorrow, or overdue
and categorizes them accordingly.
    - check_tomorrows_due_date(today): Handles tasks due the next day and performs specific actions,
such as checking priority.
    - check_todays_due_date(today): Identifies tasks due today and adds them to due_date_tasks.
    - check_passed_due_date(today): Identifies tasks overdue before the current day and adds
them to due_date_tasks.
    - check_priority(task): Checks if a task has high priority and adds it to the urgent_tasks set.
    - add_notification_date_task(task): Adds tasks with notification dates to
notification_date_tasks based on exclusion criteria.
    - add_due_date_task(task): Adds tasks with due dates to due_date_tasks based on exclusion
criteria.
    - add_urgent_task(task): Adds urgent tasks to urgent_tasks based on exclusion criteria.

    The methods handle various task-related conditions, manage task categorization, and ensure
tasks are added to the respective sets based on specific criteria.
"""
import datetime
from src.logic.users.user import User
from src.logic.items.item_interface import IItem

class Notification:
    """ a
    """
    def __init__(self, usr: User) -> None:
        self.usr = usr
        self.notification_date_tasks = set()
        self.due_date_tasks = set()
        self.urgent_tasks = set()

    #pylint: disable=pointless-string-statement
    """
    # step 1:
    def check_notification_date(self) -> None:
        pass

    # step 2:
    def check_notification_date(self) -> None:
        self.notification_date_tasks.add(self.usr.projects[0].tasks[0])

    # step 3:
    def check_notification_date(self) -> None:
        if self.usr.projects[0].tasks[0].notification_date == datetime.date.today():
            self.notification_date_tasks.add(self.usr.projects[0].tasks[0])

    # step 4:
    def check_notification_date(self) -> None:
        today = datetime.date.today()
        for each_project in self.usr.projects:
            if each_project.tasks[0].notification_date == today:
                self.notification_date_tasks.add(each_project.tasks[0])

    # step 5:
    def check_notification_date(self) -> None:
        today = datetime.date.today()
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                if each_task.notification_date == today:
                    self.notification_date_tasks.add(each_project.tasks[0])
    """

    def check_notification_date(self) -> None:
        """ This method will be used to check the notification date of the tasks
        """
        today = datetime.date.today()
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                if each_task.notification_date == today:
                    self.add_notification_date_task(each_task)

    #pylint: disable=pointless-string-statement
    """
    # step 1:
    def check_due_date(self) -> None:
        pass

    # step 2:
    def check_due_date(self) -> None:
        self.due_date_tasks.add(self.usr.projects[0].tasks[0])
    
    # step 3:
    def check_due_date(self) -> None:
        if self.usr.projects[0].tasks[0].end_date == datetime.date.today():
            self.due_date_tasks.add(self.usr.projects[0].tasks[0])

    # step 4:
    def check_due_date(self) -> None:
        today = datetime.date.today()
        for each_project in self.usr.projects:
            if each_project.tasks[0].end_date == today:
                self.due_date_tasks.add(each_project.tasks[0])

    # step 5:
    def check_due_date(self) -> None:
        today = datetime.date.today()
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                if each_task.end_date == today:
                    self.add_due_date_task(each_task)
    """

    def check_due_date(self) -> None:
        """ This method will be used to check the due date of the tasks
        """
        today = datetime.date.today()

        self.check_tomorrows_due_date(today)
        self.check_todays_due_date(today)
        self.check_passed_due_date(today)

    def check_tomorrows_due_date(self, today: datetime.date) -> None:
        """ Check for tasks due tomorrow and handle accordingly
        """
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                if each_task.end_date == today + datetime.timedelta(days=1):
                    self.check_priority(each_task)

    def check_todays_due_date(self, today: datetime.date) -> None:
        """ Check for tasks due today and handle accordingly
        """
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                if each_task.end_date == today:
                    self.add_due_date_task(each_task)

    def check_passed_due_date(self, today: datetime.date) -> None:
        """ Check for tasks due before today and handle accordingly
        """
        for each_project in self.usr.projects:
            for each_task in each_project.tasks:
                task_due_date = each_task.end_date.date() if \
                      isinstance(each_task.end_date, datetime.datetime) else each_task.end_date
                if task_due_date is not None and task_due_date < today:
                    self.add_due_date_task(each_task)

    def check_priority(self, task: IItem) -> None:
        """ This method will be used to check the priority of the tasks

        Args:
            task (IItem): Task
        """
        if task.priority == "Alta":
            self.add_urgent_task(task)

    def add_notification_date_task(self, task: IItem) -> None:
        """ This method will be used to add a notification date task

        Args:
            task (IItem): Task
        """
        if task not in self.urgent_tasks and task not in self.due_date_tasks:
            self.notification_date_tasks.add(task)

    def add_due_date_task(self, task: IItem) -> None:
        """ This method will be used to add a due date task

        Args:
            task (IItem): Task
        """
        if task not in self.urgent_tasks and task not in self.notification_date_tasks:
            self.due_date_tasks.add(task)

    def add_urgent_task(self, task: IItem) -> None:
        """ This method will be used to add a urgent task

        Args:
            task (IItem): Task
        """
        if task not in self.due_date_tasks and task not in self.notification_date_tasks:
            self.urgent_tasks.add(task)
