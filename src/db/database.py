"""
Module Name: Database Module

Description:
This module contains a class, `Database`, used to create and manage a
database connection. It provides methods for executing raw SQL queries
and committing sessions.

Classes:
- Database: Manages the database connection and provides methods for
SQL query execution and session commits.

Dependencies:
- os: Operating system interfaces.
- sqlalchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- sqlalchemy.orm: Provides the ORM functionality.
- dotenv: Loads environment variables from a .env file.

Environment Variables:
- DB_HOST: Hostname of the database server.
- DB_USER: Username for the database connection.
- DB_PASS: Password for the database connection.
- DB_NAME: Name of the database.

Attributes:
- _instance: Private class attribute to manage the singleton instance of the Database class.

Methods:
- __new__(): Creates a new instance of the Database class with a singleton pattern.
- get_session(): Retrieves a session from the session factory.
- execute_raw_sql(): Executes raw SQL queries and returns results.
- commit(): Commits the current session to the database.
"""


import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

class Database:
    """ This class will be used to create the database connection.
    """
    _instance = None

    def __new__(cls) -> object:
        """ Creates a new instance of the Database class.

        Returns:
            object: The instance of the Database class.
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)

            # Read environment variables
            db_host = os.getenv('DB_HOST')
            db_user = os.getenv('DB_USER')
            db_pass = os.getenv('DB_PASS')
            db_name = os.getenv('DB_NAME')

            # Create the database connection string
            connection_string = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:3306/{db_name}'

            # Store the engine as an attribute of the instance
            cls._instance.engine = create_engine(connection_string)

            # Create and store the session factory
            cls._instance.session_factory = sessionmaker(bind=cls._instance.engine)
        return cls._instance

    @classmethod
    def get_session(cls: object) -> object:
        """ Get a session from the session factory.

        Args:
            cls (object): Cls object

        Returns:
            object: _description_
        """
        return cls._instance.session_factory()

    def execute_raw_sql(self, sql: object, params:str=None, is_select:bool=True) -> list:
        """ Executes a raw SQL query.

        Args:
            sql (object): SQL query.
            params (str, optional): Parameters. Defaults to None.
            is_select (bool, optional): Is selected. Defaults to True.

        Returns:
            list:
        """
        with self.get_session() as session:
            result = session.execute(text(sql), params)
            if is_select:
                return result.fetchall()
            else:
                session.commit()
                return result.rowcount

    def commit(self) -> None:
        """ Commit the current session
        """
        with self.get_session() as session:
            session.commit()
