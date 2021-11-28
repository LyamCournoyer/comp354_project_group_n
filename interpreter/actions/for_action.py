import actions.action as action
import actions.math_actions as math_action
import actions.set_action as set_action
from globals import logger
import functions
from custom_exceptions import IncorrectSyntaxException, ActionException

class ForAction(action.Action):
    name = "for"
    def __init__(self, num_iterations, next_action):        
        self.steps = [num_iterations, next_action]
        self.num_iterations = num_iterations
        self.next_action = next_action
    
    def action(self, variables):
        self.num_iterations = self.steps[0]        
        for i in range(0, self.num_iterations):
            self.steps[1].action(variables)

    @classmethod 
    def parse_from_line(self,items):
        #for x times do action
        num_iterations = None
        if items[0] != 'for':
            raise IncorrectSyntaxException(self.name)      
        if items[2] != 'times':                
            raise IncorrectSyntaxException(self.name)
        if items[1].isdigit():
            num_iterations = int(items[1])
        else:
            raise ActionException(self.name)
        #TODO check if items[1] is a var        
        if len(items) <=3:
            raise IncorrectSyntaxException(self.name)
        next_action = functions.parse_line(items[3:])
        logger.debug(f'Next action is {next_action}')
        if  isinstance(next_action, math_action.MathAction) or isinstance(next_action, set_action.SetAction):        
            return ForAction(num_iterations, next_action)
        else:
            raise ActionException(self.name)
    
    def __str__(self):
        return f'{self.__class__} num_iterations:{self.num_iterations} next_action:{self.next_action}'