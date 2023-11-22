from typing import Any
from src.logic.items.item_interface import IItem
from src.logic.items.project import Project
from src.logic.items.subtask import Subtask
from src.logic.items.task import Task
from src.logic.execeptions.exceptions_items import ItemNameBlank,\
                                                    ItemNameAlreadyExists, \
                                                    UnknownItem


class ItemFactory:
    @staticmethod
    def create_item(item_type: str, **kwargs: Any) -> IItem:
        name = kwargs.get('name')
        if name is None or name == '':
            raise ItemNameBlank("Argumento 'nome' é obrigatório e não pode \
                                ser nulo ou vazio para um Item")
        
        if item_type == 'project':
            user = kwargs.get('user')
            if name in [project.name for project in user.projects]:
                raise ItemNameAlreadyExists("Já existe um projeto com esse nome")
            return Project(**kwargs)
        
        elif item_type == 'task':
            project = kwargs.get('project')
            if name in [task.name for task in project.tasks]:
                raise ItemNameAlreadyExists("Já existe uma tarefa com esse nome \
                                            nesse projeto")
            return Task(**kwargs)
        
        elif item_type == 'subtask':
            task = kwargs.get('task')
            if name in [subtask.name for subtask in task.subtasks]:
                raise ItemNameAlreadyExists("Já existe uma subtarefa com esse \
                                            nome nessa tarefa")
            return Subtask(**kwargs)
    
        else:
            raise UnknownItem("Tipo de item desconhecido")