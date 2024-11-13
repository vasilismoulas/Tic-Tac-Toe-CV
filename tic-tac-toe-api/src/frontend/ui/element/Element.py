from abc import ABC, abstractmethod
from pygame.rect import Rect
from pygame.surface import Surface
from enum import Enum


class symbolType(Enum):
    
    ST_CROSS_SYMBOL = 1
    ST_CIRCLE_SYMBOL = 2


class IElement(ABC):
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
 
    @classmethod
    def __subclasshook__(cls, C):
         if cls is IElement:
             if any("__iter__" in B.__dict__ for B in C.__mro__):
                 return True
         return NotImplemented


class Tsymbol(IElement):
     """Class/Data Structure that represents Tic-Tac-Toe's interactive symbols
        (e.g.: cross and circle)
     """
     __serial: int = 0
     
     def __init__(self, surface : Surface, name : str, x : int , y : int, rect : Rect, img_path : str ) -> None:
        self.__surface = surface
        self.__name = name
        self.__x = x
        self.__y = y
        self.__rect = rect
        self.__img_path = img_path
        Tsymbol.__symbol_count += 1
 
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
     def serial(self) -> int:
        return Tsymbol.__serial

     def __str__(self):
        return f"Symbol's name {self.__name}"

