from src.logic.items.item_interface import IItem
from typing import List
from datetime import date

        
class Task(IItem):
    def __init__(self,  project: IItem, name: str, priority: str = None, end_date: date = None, 
                 notification_date: date = None, description: str = None) -> None:
        self._project = project
        self._name = name
        self._priority = priority
        self._description = description
        self._end_date = end_date
        self._notification_date = notification_date
        self._creation_date = date.today()
        self._conclusion_date = None
        self._status = False
        self._subtasks: List[IItem] = []

        self._project.add_task(self)

    """ 
    - step 1 
    def delete(self):
        pass
        
    - step 2
    def delete(self):
        self._project.remove_task(self)
    
    - step 3
    def delete(self):
        self._subtasks.remove_subtask(subtask)
        self._project.remove_task(self)

    - step 4
    def delete(self):
        self._subtasks = []
        self._project.remove_task(self)

    - step 5
    def delete(self):
        self._subtasks[0].delete()
        self._subtasks[1].delete()
        self._project.remove_task(self)

    - step 6
    def delete(self):
        for subtask in self._subtasks[:]:
            subtask.delete()
        self._project.remove_task(self)
    """ 
    # step 6
    def delete(self) -> None:
        for subtask in self._subtasks[:]:
            subtask.delete()
        self._project.remove_task(self)
        # remover do banco de dados

    """
    - step 1
    def update(self) -> None:
        pass
        
    - step 2
    def update(self, name, priority)-> None:
        self._name = name
        self._priority = priority

    - step 3
    def update(self, name, priority, end_date, notification_date, description,
            status) -> None:
        self._name = name
        self._priority = priority
        self._end_date = end_date
        self._notification_date = notification_date
        self._description = description
        self._status = status

    - step 4
    def update(self, name = None, priority = None, end_date = None,
            notification_date = None, description = None, status= None) -> None:
        if name:
            self._name = name
        if priority:
            self._priority = priority
        if end_date:
            self._end_date = end_date
        if notification_date:
            self._notification_date = notification_date
        if description:
            self._description = description
        if status:
            self._status = status
    """
    
    # step 4
    def update(self, name = None, priority = None, end_date = None,
            notification_date = None, description = None, status= None) -> None:
        if name:
            self._name = name
        if priority:
            self._priority = priority
        if end_date:
            self._end_date = end_date
        if notification_date:
            self._notification_date = notification_date
        if description:
            self._description = description
        if status:
            self._status = status
        # atualizar no banco de dados        

    def add_subtask(self, subtask: IItem) -> None:
        self._subtasks.append(subtask)
        # adicionar no banco de dados 

    def remove_subtask(self, subtask: IItem) -> None:
        self._subtasks.remove(subtask)
        # remover do banco de dados

    @property
    def subtasks(self) -> List[IItem]:
        return self._subtasks

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def priority(self) -> str:
        return self._priority
    
    @property
    def end_date(self) -> date:
        return self._end_date
    
    @property
    def creation_date(self) -> date:
        return self._creation_date
    
    @property
    def conclusion_date(self) -> date:
        return self._conclusion_date
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def status(self) -> bool:
        return self._status

    @property
    def project(self) -> IItem:
        return self._project
    
    @property
    def notification_date(self) -> date:
        return self._notification_date