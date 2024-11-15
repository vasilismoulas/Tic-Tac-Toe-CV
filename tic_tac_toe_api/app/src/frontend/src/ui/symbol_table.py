from abc import ABC, abstractmethod
from element.Element import Tsymbol
from typing import Iterator



class ISymbol_Table(ABC):
    """
    Interface that is a blueprint for Symbol Table Singleton class
    """
    @property
    @abstractmethod
    def hash_map(self, value: tuple[str, Tsymbol]) -> None:
       pass


class SingletonMeta(type, ISymbol_Table):
    """
    Metaclass for Singleton class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs) #it invokes "__init__" function/constructor bydefault
            cls._instances[cls] = instance
        return cls._instances[cls]


class Symbol_Table(metaclass=SingletonMeta):
    """
    Symbol Table is a Singleton class that contains all the symbols(Tsymbol class) of Tic-Tac-Toe game
    """

    def __init__(self) -> None:
        self.__hash_map = {}  
    
    @classmethod
    def _get_instance(cls):
        """
        Internal method to get or create the singleton instance.
        """
        if cls not in SingletonMeta._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__()
        return SingletonMeta._instances[cls]
    
    @property
    def hash_map(self, value: tuple[str, Tsymbol]) -> None:
        if((type(value[0])==str) and (type(value[1])==Tsymbol)):
            raise ValueError()
        self.__hash_map = value

    def __iter__(self) -> Iterator:
        return iter(self.__hash_map)

    def __str__(self) -> str:
        return self.__hash_map.__str__()


