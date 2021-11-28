import actions.action as action
from globals import logger
import globals
import functions
from custom_exceptions import IncorrectSyntaxException, DivideByZeroException
class MathAction(action.Action):
    name = "math operation"
    def __init__(self, var1, var2, do_print=True):
        self.var1 = var1
        self.var2 = var2
        self.do_print = True
    
    @classmethod 
    # Determines & calls type of Math operation 
    def parse_from_line(self, items):
        math_action = items[0]
        var1 = items[1]
        link_word = items[2]
        var2 = items[3]
        if len(items) != 4:
            raise IncorrectSyntaxException(self.name)
        if math_action == 'add':
            if link_word != 'to':
                raise IncorrectSyntaxException(self.name + " add")
            return AddAction(var1, var2)
        elif math_action == 'subtract':
            if link_word != 'from':
                raise IncorrectSyntaxException(self.name + " subtract")
            return SubAction(var1, var2)
        elif math_action == 'multiply':
            if link_word != 'by':
                raise IncorrectSyntaxException(self.name + " multiply")
            return MultAction(var1, var2)
        elif math_action == 'divide':
            if link_word != 'by':
                raise IncorrectSyntaxException(self.name + " divide")
            return DivAction(var1, var2)
        elif math_action == 'modulo':
            if link_word != 'by':
                raise IncorrectSyntaxException(self.name + " modulo")
            return ModAction(var1, var2)
        else:
            raise IncorrectSyntaxException(self.name)
    
    def get_var(self, var, variables): 
        """
        Determine if the passed value is a literal or a variable.
        """    
        return functions.get_var(var, variables)

    def set_var(self, var, variables):
        """
        Determine if the passed value is a literal or a variable.
        """    
        return functions.set_var(var, variables)

    def action(self, variables):
        pass

    def __str__(self):
        return f'{self.__class__} var1:{self.var1} var2:{self.var2}'

class AddAction(MathAction):
    """
    Add two number together
    """
    def action(self, variables):        
        logger.debug('Add: {} to {}'.format(self.var1, self.var2 ))
        var1_val = self.get_var(self.var1, variables)
        var2_val = self.get_var(self.var2, variables)
        res = var1_val + var2_val
        if self.do_print:
            logger.info(res)
        return res
    
class SubAction(MathAction):
    """
    Subtract two numbers
    """
    def action(self, variables):
        logger.debug('Subtract: {} from {}'.format(self.var1, self.var2 ))
        var1_val = self.get_var(self.var1, variables)
        var2_val = self.get_var(self.var2, variables)
        res = var2_val - var1_val
        if self.do_print:
            logger.info(res)
        return res

class MultAction(MathAction):
    """
    Multiply two numbers
    """
    def action(self, variables):
        logger.debug('Multiply: {} by {}'.format(self.var1, self.var2 ))
        var1_val = self.get_var(self.var1, variables)
        var2_val = self.get_var(self.var2, variables)
        res = var1_val * var2_val
        if self.do_print:
            logger.info(res)
        return res

class DivAction(MathAction):
    """
    Divide two numbers
    """
    def action(self, variables):
        logger.debug('Divide: {} by {}'.format(self.var1, self.var2 ))
        var1_val = self.get_var(self.var1, variables)
        var2_val = self.get_var(self.var2, variables)
        if var2_val == 0:
            raise DivideByZeroException("divide")
        res = var1_val/var2_val
        if self.do_print:
            logger.info(res)
        return res

class ModAction(MathAction):
    """
    Modulo two numbers
    """
    def action(self, variables):
        logger.debug('Modulo: {} by {}'.format(self.var1, self.var2 ))
        var1_val = self.get_var(self.var1, variables)
        var2_val = self.get_var(self.var2, variables)
        if var2_val == 0:
            raise DivideByZeroException("modulo")
        res = var1_val%var2_val
        if self.do_print:
            logger.info(res)
        return res