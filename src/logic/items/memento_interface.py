"""
Module Name: Memento Interface

Description:
This module contains the IMemento abstract base class, serving as an interface blueprint 
for memento classes.

- IMemento inherits from the ABC (Abstract Base Class).
- It declares an abstract method, 'get_state()', that mandates implementation by 
  inheriting classes.

Methods:
- get_state(): An abstract method that specifies the structure for retrieving the 
  state of the memento, returning a tuple.

The IMemento class acts as a template defining the method required for accessing 
the internal state of memento objects in various implementing classes.
"""

from abc import ABC, abstractmethod

class IMemento(ABC):
    """ This class represents the interface for a memento.

    Args:
        ABC (ABC): The abstract base class for the memento.
    """
    @abstractmethod
    def get_state(self) -> tuple:
        """ Returns the state of the memento.

        Returns:
            tuple: The state of the memento.
        """
