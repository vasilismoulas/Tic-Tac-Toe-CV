from abc import ABC, abstractmethod
from pygame.rect import Rect
from pygame.surface import Surface
from enum import Enum


class symbolType(Enum):
    
    ST_CROSS_SYMBOL = 1
    ST_CIRCLE_SYMBOL = 2


class ITsymbol(ABC):
    """Interface that is a blueprint for Tic-Tac-Toe's interactive symbols
        (e.g.: cross and circle)
    """

    @property
    @abstractmethod
    def surface(self) -> Surface:
        pass

    @surface.setter
    @abstractmethod
    def surface(self, value: Surface) -> None:
       pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None:
       pass

    @property
    @abstractmethod
    def x(self) -> int:
       pass

    @x.setter
    @abstractmethod
    def name(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def y(self) -> int:
        pass

    @y.setter
    @abstractmethod
    def name(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def rect(self) -> Rect:
        return self.__rect

    @rect.setter
    @abstractmethod
    def rect(self, value: Rect) -> None:
        pass

    @property
    @abstractmethod
    def img_path(self) -> str:
        pass

    @img_path.setter
    @abstractmethod
    def img_path(self, value: str) -> None:
        pass 
    
    @property
    @abstractmethod
    def serial(self) -> int:
        pass
    
    @property
    @abstractmethod
    def symbol_name(self) -> str:
       pass
    
    @property
    @abstractmethod
    def symbol_type(self) -> str:
      pass
   
    @abstractmethod
    def generate_nodename(self) -> str:
        pass
 
    @classmethod
    def __subclasshook__(cls, C):
         if cls is ITsymbol:
             if any("__iter__" in B.__dict__ for B in C.__mro__):
                 return True
         return NotImplemented


class Tsymbol(ITsymbol):
     """Class/Data Structure that represents Tic-Tac-Toe's interactive symbols
        (e.g.: cross and circle)
     """
     __serial: int = 1
     
     def __init__(self, surface: Surface, symbol_name: str) -> None:
        self.__surface = surface
        self.__rect = surface.get_rect()
        self.__x = None
        self.__y = None
        self.__symbol_name = symbol_name
        self.__symbol_type = self.generate_nodename()
        Tsymbol.__serial += 1
 
     @property
     def surface(self) -> Surface:
        return self.__surface

     @surface.setter
     def surface(self, value: Surface) -> None:
        if not isinstance(value, Surface):
            raise ValueError()
        self.__surface = value

     @property
     def name(self) -> str:
        return self.__name

     @name.setter
     def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError()
        self.__name = value

     @property
     def x(self) -> int:
        return self.__x

     @x.setter
     def name(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError()
        self.__x = value

     @property
     def y(self) -> int:
        return self.__y

     @y.setter
     def name(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError()
        self.__y = value 

     @property
     def rect(self) -> Rect:
        return self.__rect

     @rect.setter
     def rect(self, value: Rect) -> None:
        if not isinstance(value, Rect):
            raise ValueError()
        self.__rect = value

     @property
     def img_path(self) -> str:
        return self.__img_path

     @img_path.setter
     def img_path(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError()
        self.__img_path = value
        
     @property
     def symbol_name(self) -> str:
        return self.__symbol_name
        
     @property
     def symbol_type(self) -> str:
        return self.__symbol_type
        
     @property
     def serial(self) -> int:
        return Tsymbol.__serial
    
     def generate_nodename(self) -> str:
        return f"{self.__symbol_name}_{Tsymbol.__serial}"

     def __str__(self):
        return f"Symbol's name {self.__name}"

