"""Class: FormMediator

This class serves as a mediator for forms, handling creation and update actions.

Classes:
    FormMediator: Mediator for forms.

Methods:
    - __init__: Initializes the FormMediator object.
    - create: Creates an item.
    - update: Updates an item.

Example Usage:
    # Example usage of FormMediator class
    def submit_action(item_type, data):
        # Implementation of submit_action method

    mediator = FormMediator(submit_action)
    mediator.create(data)
"""

class FormMediator:
    """ Mediator for forms.
    """
    def __init__(self, submit_action: callable):
        self.submit_action = submit_action

    def create(self, data: dict[any]) -> None:
        """ Creates an item.

        Args:
            data (dict[Any]): Data of the item.
        """
        print(data)
        item_type = data['item_type']
        del data['item_type']

        self.submit_action(item_type, data)

    def update(self, data: dict[any]) -> None:
        """ Updates an item.

        Args:
            data (dict[Any]): Data of the item.
        """
        self.submit_action(data)
