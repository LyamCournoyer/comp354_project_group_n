import unittest
import actions.set_action as set_action
import actions.math_actions as math_action

import variables
from custom_exceptions import IncorrectSyntaxException,VariableIsKeywordException, VariableIsKeywordException

class ExpectedResult():
    def __init__(self, line, _type, expected_result, reason=''):
        self.line = line
        self.items = self.line.split()
        self.type = _type
        self.expected_result = expected_result
        self.reason = reason

class TestSetActions(unittest.TestCase):

    def test_parsing_and_actions(self):
        valid_lines_to_test = [
            ExpectedResult('set x to 5', set_action.SetAction, 5, 'x gets set to 5'),
            ExpectedResult('set x to 56', set_action.SetAction, 56, 'x gets set to 56'),
            ExpectedResult('set xyx to 88', set_action.SetAction, 88, 'xyx gets set to 88'),
        ]
        
        for expected_res in valid_lines_to_test:
            my_variables = variables.Variables()
            with self.subTest(msg=f'Test {expected_res.reason}: "{expected_res.line}" is of type {expected_res.type} with result {expected_res.expected_result}'):
                parsed_action = set_action.SetAction.parse_from_line(expected_res.items)
                self.assertIsInstance(parsed_action, expected_res.type)
                action_res = parsed_action.action(my_variables)
                self.assertEqual(action_res, expected_res.expected_result)

    ## Check that numbers and keywords used as variable names throws exceptions
    def test_exceptions(self):
        lines_expected_exception = [
            'set add to 5',
            'set subtract to 88',
            'set 23 to 12',
            'setttt a to b'
        ]

        for expected_exception in lines_expected_exception:
            with self.assertRaises(IncorrectSyntaxException):
                set_action.SetAction.parse_from_line(expected_exception)

    ## Check that using set allows for equation chaining
    def test_chained_equations(self):
        
        chained_equations_lines = [
            ExpectedResult('set x to add 6 to 9', set_action.SetAction, math_action.AddAction, 'an addition gets set'),
            ExpectedResult('set x to subtract 88 from 100', set_action.SetAction, math_action.SubAction, 'a subtraction gets set'),
        ]

        for expected_equations in chained_equations_lines:
            my_variables = variables.Variables()
            with self.subTest(msg=f'Test {expected_equations.reason}: "{expected_equations.line}" is of type {expected_equations.type} with result {expected_equations.expected_result}'):
                parsed_action = set_action.SetAction.parse_from_line(expected_equations.items)
                self.assertIsInstance(parsed_action, expected_equations.type)
                action_res = parsed_action.action(my_variables)
                self.assertIsInstance(action_res, expected_equations.expected_result)

if __name__ == '__main__':
    unittest.main()