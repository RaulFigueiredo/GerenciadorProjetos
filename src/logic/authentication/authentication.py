# import database
from src.db.database import Database
from sqlalchemy.exc import SQLAlchemyError
from src.logic.orms.orm import UserORM
from src.logic.users.user import User
from src.logic.items.project import Project
from src.logic.items.task import Task
from src.logic.items.subtask import Subtask
from src.logic.items.label import Label

from sqlalchemy.orm import sessionmaker

db = Database()

SessionLocal = sessionmaker(bind=db.engine)

def instance_user(db_user):
    """
    Converts a UserORM instance into a User instance, along with associated projects, tasks, subtasks, and labels.

    Parameters:
        db_user (UserORM): An instance of UserORM representing a user in the database.

    Returns:
        User: An instance of the User class, populated with data from the UserORM instance, including associated projects, tasks, subtasks, and labels.
    """
    print(f'Creating user instance from {db_user.name}')
    user = User(db_user.name)
    db_projects = db_user.projects
    db_labes = db_user.labels
    for db_project in db_projects:
        project = Project(user, db_project.name, description=db_project.description)
        db_tasks = db_project.tasks
        for db_task in db_tasks:
            task = Task(project, db_task.name, description=db_task.descriptions, end_date=db_task.end_date, priority=db_task.priority)
            db_subtasks = db_task.subtasks
            for db_subtask in db_subtasks:
                subtask = Subtask(task, db_subtask.name)
                task.add_subtask(subtask)
    for db_label in db_labes:
        label = Label(user, db_label.name, db_label.color)
        user.add_label(label)
    return user

class LoginLogic:
    """
    Class to handle the login logic.
    """

    @staticmethod
    def login(username, password):
        """
        Authenticates a user by their username and password, using SQLAlchemy ORM for database interaction.

        Parameters:
            username (str): The username of the user attempting to log in.
            password (str): The password of the user attempting to log in.

        Returns:
            User or None: Returns a User instance if authentication is successful; None otherwise.
        """
        try:
            # Create a new session
            with SessionLocal() as session:
                # Query the UserORM table
                user = session.query(UserORM).filter(UserORM.name == username, UserORM.password == password).first()

                # Check if user exists with the given username and password
                if user is not None:
                    user_instance = instance_user(user)
                    return user_instance
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

class RegisterLogic:
    """
    Class to handle the registration logic.
    """

    @staticmethod
    def register(username, password, email):
        """
        Registers a new user with the provided username, password, and email.

        Parameters:
            username (str): The username for the new user.
            password (str): The password for the new user.
            email (str): The email address for the new user.

        Returns:
            User or None: Returns a User instance if registration is successful; None if the username already exists or an error occurs.
        """
        print(f"Attempting to register with username: {username}, and email: {email}")

        try:
            with SessionLocal() as session:
                # Check if username already exists
                if session.query(UserORM).filter(UserORM.name == username).first():
                    return None

                # Create new user and add to session
                new_user = UserORM(name=username, password=password, email=email)
                session.add(new_user)
                session.commit()
                new_user_intance = instance_user(new_user)
                # Return the new user
                return new_user_intance
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
