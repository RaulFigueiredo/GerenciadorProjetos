from sqlalchemy import create_engine
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
            connection_string = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}'

            engine = create_engine(connection_string)
            cls._instance.session_factory = sessionmaker(bind=engine)
        return cls._instance

    def get_session(self):
        return self._instance.session_factory()

    def load_data(self, model, filter_by=None):
        pass

    def update_data(self, model, filter_by, update_values):
        pass

    def delete_data(self, model, filter_by):
        pass
