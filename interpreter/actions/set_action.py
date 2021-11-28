import actions.action as action
import actions.math_actions as math_action
import globals
from globals import logger
import functions
from custom_exceptions import VariableNumberException, VariableIsKeywordException, VariableDoesNotExistException, IncorrectSyntaxException, ActionException
class SetAction(action.Action):
    """
    Set variable
    """
    name = "set"
    def __init__(self, var_name, value):        
        self.var_name = var_name
        self.value = value

    def action(self, variables):
        logger.debug('Set: {} to {}'.format(self.var_name, self.value))
        val_to_set = self.value.action(variables) if isinstance(self.value, math_action.MathAction) else self.value
        variables.add(self.var_name, val_to_set)
        return self.value

    @classmethod 
    def parse_from_line(self, items):
        var_name = items[1]
        value = items[3]
        # if len(items) <= 4:
        #     raise
        if items[0] != 'set':
            raise IncorrectSyntaxException(self.name)      
        if items[2] != 'to':                
            raise IncorrectSyntaxException(self.name)      
        if var_name.isdigit(): 
            raise VariableNumberException(var_name)
        if not functions.check_keywords(var_name):
            raise VariableIsKeywordException(var_name)
        
        if value in globals.MATH_OPS:
            next_action = functions.parse_line(items[3:])
            if not isinstance(next_action, math_action.MathAction):
                raise ActionException(self.name)
            return SetAction(var_name, next_action)
        try:
            value = float(value)    
        except:
            raise VariableDoesNotExistException(value)
        
        return SetAction(var_name, value)

    def __str__(self):
        return f'{self.__class__} var_name:{self.var_name} value:{self.value}'
