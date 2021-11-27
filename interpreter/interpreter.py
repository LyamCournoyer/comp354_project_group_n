
import os
import sys
import logging
import argparse

from globals import logger
from functions import parse_line
from variables import Variables
from custom_exceptions import VariableException

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='file to run')
parser.add_argument('--debug', help='run with debug output', action='store_true')
args = parser.parse_args()


def main(file_, run_with_debug=False):
    if run_with_debug:
        logging.root.setLevel(logging.DEBUG)
    global_variables = Variables()
    lines = None
    #TODO better way to read maybe
    with open(file_, 'r') as f:
        lines = f.read().splitlines()    
    logger.debug(lines)
    line_number = 0
    for line in lines:
        line_number += 1
        items = line.split()
        if not items:
            #nothing to do on a empty line
            continue 
        parsed_lined = parse_line(items)
        logger.debug(parsed_lined)
        try:
            parsed_lined.action(global_variables)
        except VariableException as e:
            logger.error(f'Line {line_number}: {e}')
            logger.debug(f'Current variables {global_variables}')
        except Exception  as e:
            logger.error(f'Unknown error at: Line {line_number}')
            logger.debug(f'Unknown error at: Line {line_number}: {e}')




if __name__ == "__main__":
    args = parser.parse_args()
    file_ = args.file
    #TODO validate file exists
    main(file_, args.debug)
    