
import os
import sys
import logging
from globals import logger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='file to run')
parser.add_argument('--debug', help='run with debug output', action='store_true')
args = parser.parse_args()
mathOps = ['add', 'subtract', 'multiply', 'divide', 'modulo']

def main(file_, run_with_debug=False):
    if run_with_debug:
        logging.root.setLevel(logging.DEBUG)
    global_variables = Variables()
    global_variables.add('x', 4)
    lines = None
    #TODO better way to read maybe
    with open(file_, 'r') as f:
        lines = f.read().splitlines()
    # lines = ['for 10 times add 1 to 2', 'add x to 3']
    logger.debug(lines)
    for line in lines:
        parsed_lined = parse_line(line.split())
        logger.debug(parsed_lined)
        try:
            parsed_lined.action(global_variables)
        except Exception  as e:
            logger.error(e)


class Action:
    def __init__(self, code, variables):
        pass
    
    def get_type(self):
        return self.type
    def parse_from_line(self):
        pass

class ForAction(Action):
    def __init__(self, num_iterations, next_action):
        self.type = 'for'
        self.steps = [num_iterations, next_action]
        self.num_iterations = num_iterations
        self.next_action = next_action
    
    def action(self, variables):
        self.num_iterations = self.steps[0]        
        for i in range(0, self.num_iterations):
            self.steps[1].action(variables)

    @classmethod 
    def parse_from_line(self,items):
        num_iterations = None
        if items[0] != 'for':
            raise        
        if items[2] != 'times':                
            raise
        if items[1].isdigit():
            num_iterations = int(items[1])
        else:
            raise
        #TODO check if items[1] is a var        
        if len(items) <=3:
            raise
        next_action = parse_line(items[3:])
        if not isinstance(next_action, MathAction):
            raise
        return ForAction(num_iterations, next_action)
    
    def __str__(self):
        return f'{self.__class__} num_iterations:{self.num_iterations} next_action:{self.next_action}'

class MathAction(Action):
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
            value = variables.get(var)
            #TODO make sure it's not a keyword, otherwise assume variable            
            
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
    
class SetAction(Action):
    def __init__(self):
        pass

def parse_line(items):
    logger.debug(f'Items left to parse {items}')
    if items[0] == 'for':                
        return ForAction.parse_from_line(items)
    if items[0] in mathOps:
        return MathAction.parse_from_line(items)

class Variables:
    def __init__(self):
        self.__items = {}
    
    def add(self, name, val):       
        self.__items[name] = val
    
    def get(self, name):        
        #TODO raise if doesn't exist
        logger.debug('Getting variable: {}'.format(name)) 
        return self.__items[name]


if __name__ == "__main__":
    args = parser.parse_args()
    file_ = args.file
    #TODO validate file exists
    main(file_, args.debug)
    