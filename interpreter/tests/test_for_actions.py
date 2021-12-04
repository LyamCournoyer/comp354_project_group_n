import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import actions.for_action as for_action
import actions.set_action as set_action
import variables
from custom_exceptions import IncorrectSyntaxException

class ExpectedResult():
    def __init__(self, line, _type, expected_result, reason=''):
        self.line = line
        self.items = self.line.split()
        self.type = _type
        self.expected_result = expected_result
        self.reason = reason

class TestForActions(unittest.TestCase):


##TODO finish testing with setting before valid for loops are tested
    def test_parsing_and_actions(self):
        setup = [
            'set x to 1',
            'set y to 54',
        ]

        lines_to_test = [
            ExpectedResult('for 2 times set x to add 10 to x',for_action.ForAction,20,'For loop twice')
        ]

        for line in setup:
            parsed_action = set_action.SetAction.parse_from_line(line.split())
            my_variables = variables.Variables()
            action_res = parsed_action.action(my_variables)

        for expected_res in lines_to_test:
            my_variables = variables.Variables()
            with self.subTest(msg=f'Test {expected_res.reason}: "{expected_res.line}" is of type {expected_res.type} with result {expected_res.expected_result}'):
                parsed_action = for_action.ForAction.parse_from_line(expected_res.items)
                self.assertIsInstance(parsed_action, expected_res.type )
                action_res = parsed_action.action(my_variables)
                self.assertEqual(action_res, expected_res.expected_result)

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

