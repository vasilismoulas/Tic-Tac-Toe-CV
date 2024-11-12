from abc import ABC, abstractmethod
from element.Element import Tsymbol


class ISymbol_Table(ABC):
    """
    Interface that is a blueprint for Symbol Table Singleton class
    """
    @property
    @abstractmethod
    def hash_map(self, value: tuple[str, Tsymbol]) -> None:
       pass


class SingletonMeta(type):
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
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Symbol_Table(ISymbol_Table, metaclass=SingletonMeta):
    """
    Symbol Table is a Singleton class that contains all the symbols(Tsymbol class) of Tic-Tac-Toe game
    """

    def __init__(self) -> None:
      self.__hash_map = {}  

    @property
    def hash_map(self, value: tuple[str, Tsymbol]) -> None:
        if((type(value[0])==str) and (type(value[1])==Tsymbol)):
            raise ValueError()
        self.__hash_map = value

    def __iter__(self):
        pass

    def __str__(self) -> str:
        return f" {0} "
    
    