import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import actions.for_action as for_action
import actions.math_actions as math_action
import actions.set_action as set_action
import variables
from custom_exceptions import IncorrectSyntaxException

class ExpectedResult():
    def __init__(self, line, _type, next_action,reason=''):
        self.line = line
        self.items = self.line.split()
        self.type = _type
        self.next_action = next_action
        self.reason = reason

class TestForActions(unittest.TestCase):


    def test_parsing_and_actions(self):
        
        lines_to_test = [
            ExpectedResult('for 2 times add 10 to 10',for_action.ForAction, math_action.AddAction ,'For loop addition'),
            ExpectedResult('for 5 times subtract 20 from 20',for_action.ForAction, math_action.SubAction,'For loop subtraction'),
            ExpectedResult('for 5 times set x to 34',for_action.ForAction, set_action.SetAction,'For loop subtraction')
        ]

        for expected_res in lines_to_test:
            my_variables = variables.Variables()
            with self.subTest(msg=f'Test {expected_res.reason}: "{expected_res.line}" is of type {expected_res.type}'):
                parsed_action = for_action.ForAction.parse_from_line(expected_res.items)
                self.assertIsInstance(parsed_action, expected_res.type)
                self.assertIsInstance(parsed_action.next_action,expected_res.next_action)

    def test_exceptions(self):
        lines_expected_exception = [
            'for 10 times set test_for to add zzzs to test_for',
            'for zzz times set test_for to add zzzs to test_for',
            'for 12 times add zz to zz',
        ]

        for expected_exception in lines_expected_exception:
            with self.assertRaises(IncorrectSyntaxException):
                for_action.ForAction.parse_from_line(expected_exception)

if __name__ == '__main__':
    unittest.main()

