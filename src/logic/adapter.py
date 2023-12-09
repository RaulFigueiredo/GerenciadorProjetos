import json
import os
from typing import List
from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.load import Load
from src.logic.items.item_factory import ItemFactory
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    InvalidFileFormat,\
                                                    InvalidFileEstucture,\
                                                    FileNotFoundError
import ast

class FileAdapter:
    @staticmethod
    def read_file(user, file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.json':
            return Load.json_reader(user, file_path)
        elif file_extension.lower() == '.txt':
            return Load.txt_reader(user, file_path)
        else:
            raise InvalidFileFormat("Unsupported file format.")