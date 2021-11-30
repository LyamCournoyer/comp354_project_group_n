import actions.action as action
import actions.math_actions as math_action
import actions.set_action as set_action
import actions.for_action as for_action
from globals import logger
import globals
import functions
from custom_exceptions import IncorrectSyntaxException, ActionException, IfConditionException


class IfAction(action.Action):
    name = "if"  
    def __init__(self, condition_name, var1, var2, next_action):        
        self.condition_name = condition_name
        self.var1 = var1
        self.var2 = var2
        self.next_action = next_action 
    
    def action(self, variables):
        var1_val = functions.get_var(self.var1, variables)
        var2_val = functions.get_var(self.var2, variables)
        if self.condition_name == 'less' and var1_val < var2_val:
            return self.next_action.action(variables)
        elif self.condition_name == 'greater' and var1_val > var2_val:
            return self.next_action.action(variables)
        else:
            raise IfConditionException()

    @classmethod 
    def parse_from_line(self, items):        
        #if x is less than y action
        if len(items) <= 6:
            raise IncorrectSyntaxException(self.name)
        this_action = items[0]
        var1 = items[1]
        first_link_word = items[2]
        condition_name = items[3]
        second_link_word = items [4]
        var2 = items [5]
        next_action_items = items[6:]

        if this_action != 'if':
            raise IncorrectSyntaxException(self.name)
        if first_link_word != 'is':
            raise IncorrectSyntaxException(self.name)
        if second_link_word != 'then':
            raise IncorrectSyntaxException(self.name)
        if condition_name not in globals.IF_CONDITIONS:
            raise IfConditionException()
        next_action = functions.parse_line(next_action_items)        
        if   ( isinstance(next_action, math_action.MathAction)
                or isinstance(next_action, set_action.SetAction)
                or isinstance(next_action, for_action.ForAction)):
            return IfAction(condition_name, var1, var2, next_action)
        else:
            raise ActionException(self.name)
    
    def __str__(self):
        return f'{self.__class__} condition:{self.condition_name} var1:{self.var1} var2:{self.var2} next_action:{self.next_action}'