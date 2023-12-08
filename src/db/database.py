from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

class Database:
    _instance = None

    def __new__(cls):
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
    def get_session(cls):
        return cls._instance.session_factory()

    def execute_raw_sql(self, sql, params=None, is_select=True):
        with self.get_session() as session:
            result = session.execute(text(sql), params)
            if is_select:
                return result.fetchall()
            else:
                session.commit()
                return result.rowcount

    def commit(self):
        with self.get_session() as session:
            session.commit()
