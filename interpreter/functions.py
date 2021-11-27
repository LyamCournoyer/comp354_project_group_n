import globals
from globals import logger
import actions.math_actions as math_action
import actions.for_action as for_action
import actions.set_action as set_action
import actions.if_action as if_action
from variables import Variables

def parse_line(items):
    logger.debug(f'Items left to parse {items}')
    if items[0] == 'for':                
        return for_action.ForAction.parse_from_line(items)
    elif items[0] == 'set':
        return set_action.SetAction.parse_from_line(items)
    elif items[0] in globals.MATH_OPS:
        return math_action.MathAction.parse_from_line(items)
    elif items[0] == 'if':
        return if_action.IfAction.parse_from_line(items)
    


def check_keywords(word):
    return word not in globals.MATH_OPS and word not in globals.MATH_KEYS and word not in globals.ACTION_OPS and word not in globals.ACTION_KEYS


def get_var(var, _variables: Variables): 
    """
    Determine if the passed value is a literal or a variable.
    """    
    try: 
        value = float(var)
    except:
        if check_keywords(var): 
            value = _variables.get(var)
        else:
            raise          
        
    logger.debug('Using value {}'.format(value))
    return value

def set_var(var, _variables: Variables):
    """
    Determine if the passed value is a literal or a variable.
    """    
    try: 
        value = float(var)
    except:
        if check_keywords(var): 
            value = _variables.get(var)
        else:
            raise          
    
    logger.debug('Using value {}'.format(value))
    return value