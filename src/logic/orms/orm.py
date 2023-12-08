from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.db.database import Database

Base = declarative_base()

class UserORM(Base):
    __tablename__ = 'User'

    id_user = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(25), nullable=False)

    labels = relationship("LabelORM", backref="user")
    projects = relationship("ProjectORM", backref="user")

    @classmethod
    def get_user_by_id(cls, user_id):
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_user == user_id).first()


class LabelORM(Base):
    __tablename__ = 'Label'

    id_label = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('User.id_user'), nullable=False)
    name = Column(String(50), nullable=False)
    color = Column(String(25), nullable=False)

class ProjectORM(Base):
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
    def get_projects_by_user_id(cls, user_id):
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_user == user_id).all()

class TaskORM(Base):
    __tablename__ = 'Task'

    id_task = Column(Integer, primary_key=True)
    id_project = Column(Integer, ForeignKey('Project.id_project'), nullable=False)
    name = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False)
    creation_date = Column(Date, nullable=False)
    end_date = Column(Date)
    conclusion_date = Column(Date)
    priority = Column(String(25))
    descriptions = Column(String(300))

    subtasks = relationship("SubtaskORM", backref="task")

    @classmethod
    def get_tasks_by_project_id(cls, project_id):
        with Database.get_session() as session:
            return session.query(cls).filter(cls.id_project == project_id).all()
class SubtaskORM(Base):
    __tablename__ = 'Subtask'

    id_subtask = Column(Integer, primary_key=True)
    id_task = Column(Integer, ForeignKey('Task.id_task'), nullable=False)
    name = Column(String(150), nullable=False)
    color = Column(String(25), nullable=False)
