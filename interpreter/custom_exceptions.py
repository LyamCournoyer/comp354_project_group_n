class InterpreterException(Exception):
     """Base class for Custom exeption"""
#####
# Variable exceptions
#####
class VariableException(InterpreterException):
    """Base class for Variable exeption"""

class VariableDoesNotExistException(VariableException):
    """ Exception raised when trying to get a variable that does not exist"""
    def __init__(self, var_name):
        self.var_name = var_name
        super().__init__(f'Cannot use variable "{self.var_name}" because it was not set first.')

class VariableIsKeywordException(VariableException):
    """ Exception raised when trying to set a variable that is a keyword"""
    def __init__(self, var_name):
        self.var_name = var_name        
        super().__init__(f'Cannot set variable "{self.var_name}" because it is a keyword. Please use a different name.')

class VariableNumberException(VariableException):
    """ Exception raised when trying to set a variable that is a number"""
    def __init__(self, var_name):
        self.var_name = var_name        
        super().__init__(f'Cannot set variable "{self.var_name}" because it is a number. Please use a different name.')

#####
# Syntax Exceptions
#####

class SyntaxException(InterpreterException):
    """Base class for Syntax exception"""

class IncorrectSyntaxException(SyntaxException):
    """ Exception raised when incorrect command is entered """
    def __init__(self, command_name):
        self.command_name = command_name
        super().__init__(f'Cannot execute command "{self.command_name}" as the syntax is incorrect')

class ActionException(SyntaxException):
    def __init__(self, command_name):
        self.command_name = command_name
        super().__init__(f'Action in "{self.command_name}" command is invalid') 

class IfConditionException(SyntaxException):
    def __init__(self):
        super().__init__(f'Condition in "if" command is invalid') 

#####
# Math Exceptions
#####

class MathException(InterpreterException):
     """ Exception raised when invalid mathematical operations executed """

class DivideByZeroException(MathException):
    def __init__(self, operation_name):
        self.operation_name = operation_name
        super().__init__(f'Cannot {self.operation_name} by zero') 
