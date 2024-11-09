from abc import ABC, abstractmethod

class IElement(ABC):
    
    @abstractmethod
    def get_rect(self):
        pass
    
    # @classmethod
    # def __subclasshook__(cls, C):
    #     if cls is IElement:
    #         if any("__iter__" in B.__dict__ for B in C.__mro__):
    #             return True
    #     return NotImplemented


class cross_symbol(IElement):
    
     def get_rect(self):
        print("method got implemented")


class circle_symbol(IElement):
    
    def get_rect(self):
        print("method got implemented")