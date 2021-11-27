import logging
import sys
import logger_formatter

### Setup logger
__fmt = logger_formatter.MyFormatter()
__hdlr = logging.StreamHandler(sys.stdout)
__hdlr.setFormatter(__fmt)
logging.root.addHandler(__hdlr)
logging.root.setLevel(logging.INFO)
logger = logging.getLogger("my_custom_logger")

#Keyword
MATH_OPS = ['add', 'subtract', 'multiply', 'divide', 'modulo']
MATH_KEYS = ['by', 'to', 'from']
ACTION_OPS = ['set', 'for', 'if']
ACTION_KEYS = ['times', 'than']
IF_CONDITIONS = ['less', 'greater']




