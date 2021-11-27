#####
# Variable exceptions
#####

class VariableException(Exception):
    """Base class for Variable exeption"""

class VariableDoesNotExistException(VariableException):
    """ Exception raised when trying to get a variable that does not exist"""
    def __init__(self, var_name):
        self.var_name = var_name
        super().__init__(f'Cannot use variable "{self.var_name}" because it was not set first.')

class VariableIsKeywordtException(VariableException):
    """ Exception raised when trying to set a variable that is a keyword"""
    def __init__(self, var_name):
        self.var_name = var_name        
        super().__init__(f'Cannot set variable "{self.var_name}" because it is a keyword. Please use a different name.')