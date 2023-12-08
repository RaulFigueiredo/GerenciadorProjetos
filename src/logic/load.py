import json
from src.logic.users.user_interface import IUser
from src.logic.users.user import User
from src.logic.items.item_factory import ItemFactory

class Load:
    @staticmethod
    def json_reader(file_path: str, user: IUser) -> None:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        for each_project in data:
            projet = ItemFactory.create_item(item_type = 'project',
                                              user = user,
                                              name = each_project['project'],
                                              end_date = each_project['end_date'],
                                              description = each_project['description'])
            
            for each_task in each_project['tasks']:
                task = ItemFactory.create_item( item_type = 'task', 
                                                project = projet,
                                                name = each_task['task'],
                                                priority = each_task['priority'],
                                                end_date = each_task['end_date'],
                                                notification_date = each_task['notification_date'],
                                                description = each_task['description'])
                
                for each_subtask in each_task['subtasks']:
                    print(task)
                    subtask = ItemFactory.create_item(item_type = 'subtask',
                                           task = task,
                                           name = each_subtask['subtask'])
                                           

                

if __name__ == '__main__':
    user = User('ronaldo')
    Load.json_reader('/home/raul/Documents/EngSoft/GerenciadorProjetos/src/logic/teste_export', user)
    print('+'*30)
    print(user.projects)
    print('+'*30)
    print(user.projects[0].tasks)
    print('+'*30)

            