"""
Module Name: ORM Models

Description:
This module contains SQLAlchemy ORM models representing various entities in
the application's database schema. It includes classes that map to tables in
the database and their relationships.

Classes:
- UserORM: Represents the 'User' table in the database, including relationships
with labels and projects.
- LabelORM: Represents the 'Label' table in the database, associated with users.
- ProjectORM: Represents the 'Project' table in the database, associated with
users and labels.
- TaskORM: Represents the 'Task' table in the database, associated with projects
and having relationships with subtasks.
- SubtaskORM: Represents the 'Subtask' table in the database, associated with tasks.

Dependencies:
- sqlalchemy: SQL toolkit and Object-Relational Mapping (ORM) library.

Attributes:
- Base: SQLAlchemy declarative base used for ORM class inheritance.

Methods (Sample from UserORM):
- get_user_by_id(): Retrieves a user by their ID from the 'User' table.
- get_projects_by_user_id(): Retrieves all projects associated with a user by their
ID from the 'Project' table.
- get_tasks_by_project_id(): Retrieves all tasks associated with a project by its ID
from the 'Task' table.

Note:
- These classes define the database schema and relationships using SQLAlchemy ORM,
reflecting the structure of the underlying database tables and their connections.
"""


from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.db.database import Database

Base = declarative_base()

class UserORM(Base):
    """ UserORM class.

    Args:
        Base (Base): Base class for the ORM

    Returns:
        _type_: UserORM class
    """
    __tablename__ = 'User'

    id_user = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(25), nullable=False)

    labels = relationship("LabelORM", backref="user")
    projects = relationship("ProjectORM", backref="user")

    @classmethod
    def get_user_by_id(cls, user_id: object) -> object:
        """ Get user by id.

        Args:
            user_id (object): User id

        Returns:
            object: User
        """
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_user == user_id).first()


class LabelORM(Base):
    """ LabelORM class.
    """
    __tablename__ = 'Label'

    id_label = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id_user'), nullable=False)
    name = Column(String(50), nullable=False)
    color = Column(String(25), nullable=False)

class ProjectORM(Base):
    """ ProjectORM class.

    Args:
        Base (_type_): Base class for the ORM

    Returns:
        _type_: ProjectORM class
    """
    __tablename__ = 'Project'

    id_project = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id_user'), nullable=False)
    id_label = Column(Integer, ForeignKey('Label.id_label'))
    name = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False)
    creation_date = Column(Date, nullable=False)
    end_date = Column(Date)
    conclusion_date = Column(Date)
    description = Column(String(300))

    tasks = relationship("TaskORM", backref="project")

    @classmethod
    def get_projects_by_user_id(cls, user_id: object) -> object:
        """ Get all projects from a user.

        Args:
            user_id (object): User id

        Returns:
            object: List of projects
        """
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_user == user_id).all()

class TaskORM(Base):
    """ TaskORM class.
    """
    __tablename__ = 'Task'

    id_task = Column(Integer, primary_key=True)
    id_project = Column(Integer, ForeignKey('Project.id_project'), nullable=False)
    name = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False)
    creation_date = Column(Date, nullable=False)
    end_date = Column(Date)
    conclusion_date = Column(Date)
    notification_date = Column(Date)
    priority = Column(String(25))
    description = Column(String(300))

    subtasks = relationship("SubtaskORM", backref="task")

    @classmethod
    def get_tasks_by_project_id(cls, project_id: object) -> object:
        """ Get all tasks from a project.

        Args:
            project_id (object): Project id

        Returns:
            object: List of tasks
        """
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_project == project_id).all()
class SubtaskORM(Base):
    """ SubtaskORM class.

    Args:
        Base (Base): Base class for the ORM
    """
    __tablename__ = 'Subtask'

    id_subtask = Column(Integer, primary_key=True)
    id_task = Column(Integer, ForeignKey('Task.id_task'), nullable=False)
    name = Column(String(150), nullable=False)
    status = Column(Boolean, nullable=False)
    conclusion_date = Column(Date)
