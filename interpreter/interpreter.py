
import os
import sys
import logging
import argparse

from globals import logger
from functions import parse_line

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
    # lines = ['for 10 times add 1 to 2', 'add x to 3']
    logger.debug(lines)
    line_number = 0
    for line in lines:
        line_number += 1
        parsed_lined = parse_line(line.split())
        logger.debug(parsed_lined)
        try:
            parsed_lined.action(global_variables)
        except Exception  as e:
            logger.error(f'Line {line_number}: {e}')



class Variables:
    def __init__(self):
        self.__items = {}
    
    def add(self, name, val):       
        self.__items[name] = val
    
    def get(self, name):        
        logger.debug('Getting variable: {}'.format(name)) 
        if name in self.__items:
            return self.__items[name]
        else:
            raise

if __name__ == "__main__":
    args = parser.parse_args()
    file_ = args.file
    #TODO validate file exists
    main(file_, args.debug)
    