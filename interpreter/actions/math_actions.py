import actions.action as action
from globals import logger
import globals
import functions
class MathAction(action.Action):
    def __init__(self, var1, var2, do_print=True):
        self.var1 = var1
        self.var2 = var2
        self.do_print = True
    
    @classmethod 
    # Determines & calls type of Math operation 
    def parse_from_line(self, items):
        var1 = items[1]
        var2 = items[3]
        if len(items) != 4:
            raise
        if items[0] == 'add':
            if items[2] != 'to':
                raise
            return AddAction(var1, var2)
        if items[0] == 'subtract':
            if items[2] != 'from':
                raise
            return SubAction(var1, var2)
        if items[0] == 'multiply':
            if items[2] != 'by':
                raise
            return MultAction(var1, var2)
        if items[0] == 'divide':
            if items[2] != 'by':
                raise
            return DivAction(var1, var2)
        if items[0] == 'modulo':
            if items[2] != 'by':
                raise
            return ModAction(var1, var2)
        else:
            raise
    
    def get_var(self, var, variables): 
        """
        Determine if the passed value is a literal or a variable.
        """    
        try: 
            value = float(var)
        except:
            if functions.check_keywords(var): 
                value = variables.get(var)
            else:
                raise          
            
        logger.debug('Using value {}'.format(value))
        return value

    def set_var(self, var, variables):
        """
        Determine if the passed value is a literal or a variable.
        """    
        try: 
            value = float(var)
        except:
            if functions.check_keywords(var): 
                value = variables.get(var)
            else:
                raise          
        
        logger.debug('Using value {}'.format(value))
        return value

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
        res = var1_val%var2_val
        if self.do_print:
            logger.info(res)
        return res