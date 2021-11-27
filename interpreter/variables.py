from custom_exceptions import VariableDoesNotExistException
from globals import logger


class Variables:
    def __init__(self):
        self.__items = {}
    
    def add(self, name, val):       
        self.__items[name] = val
    
    def get(self, name):        
        logger.debug('Getting variable: {}'.format(name)) 
        if name in self.__items:
            return self.__items[name]
        else:
            raise VariableDoesNotExistException(name)

    def __str__(self):
        return f'{self.__class__} variables: {self.__items}'




        