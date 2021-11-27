import globals
from globals import logger
import actions.math_actions as math_action
import actions.for_action as for_action
import actions.set_action as set_action

def parse_line(items):
    logger.debug(f'Items left to parse {items}')
    if items[0] == 'for':                
        return for_action.ForAction.parse_from_line(items)
    if items[0] == 'set':
        return set_action.SetAction.parse_from_line(items)
    if items[0] in globals.MATH_OPS:
        return math_action.MathAction.parse_from_line(items)


def check_keywords(word):
    return word not in globals.MATH_OPS and word not in globals.MATH_KEYS and word not in globals.ACTION_OPS and word not in globals.ACTION_KEYS