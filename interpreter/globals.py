import logging
import sys
import logger_formatter

### Setup logger
class InfoFilter(logging.Filter):
   def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)

__fmt = logger_formatter.MyFormatter()
__hdlr = logging.StreamHandler(sys.stdout)
__hdlr.setFormatter(__fmt)
__hdlr.addFilter(InfoFilter())
__hdlr2 = logging.StreamHandler()
__hdlr2.setFormatter(__fmt)
__hdlr2.setLevel(logging.WARNING)
logging.root.addHandler(__hdlr)
logging.root.addHandler(__hdlr2)
logging.root.setLevel(logging.INFO)
logger = logging.getLogger("my_custom_logger")

#Keyword
MATH_OPS = ['add', 'subtract', 'multiply', 'divide', 'modulo']
MATH_KEYS = ['by', 'to', 'from']
ACTION_OPS = ['set', 'for', 'if']
ACTION_KEYS = ['times', 'than']
IF_CONDITIONS = ['less', 'greater']




