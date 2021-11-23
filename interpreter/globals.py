import logging
import sys
import logger_formatter

fmt = logger_formatter.MyFormatter()
hdlr = logging.StreamHandler(sys.stdout)

hdlr.setFormatter(fmt)
logging.root.addHandler(hdlr)
logging.root.setLevel(logging.INFO)
logger = logging.getLogger("my_custom_logger")