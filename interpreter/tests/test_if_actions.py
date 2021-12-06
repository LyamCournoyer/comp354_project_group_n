import unittest
import actions.if_action as if_action
import variables
from custom_exceptions import IncorrectSyntaxException

class ExpectedResult():
    def __init__(self, line, _type, expected_result, reason=''):
        self.line = line
        self.items = self.line.split()
        self.type = _type
        self.expected_result = expected_result
        self.reason = reason

class TestIfActions(unittest.TestCase):

    def test_parsing_and_actions(self):
        lines_to_test = [
            ExpectedResult('if 1 is less than 2 add 1 to 34', if_action.IfAction, 35, 'Less than condition is true'),
            ExpectedResult('if 3 is greater than 1 add 27 to 27', if_action.IfAction, 54, 'Greater than condition is true'),
        ]
        
        for expected_res in lines_to_test:
            my_variables = variables.Variables()
            with self.subTest(msg=f'Test {expected_res.reason}: "{expected_res.line}" is of type {expected_res.type} with result {expected_res.expected_result}'):
                parsed_action = if_action.IfAction.parse_from_line(expected_res.items)
                self.assertIsInstance(parsed_action, expected_res.type )
                action_res = parsed_action.action(my_variables)
                self.assertEqual(action_res, expected_res.expected_result)

    def test_exceptions(self):
        lines_expected_exception = [
            'if 2 is greater than 2 add 1 to 34',
            'if 3 is less than 2 add 1 to 34',
            'if 3 is leeeeees than 2 add 1 to 34',
            'ifeee 3 is leeeeees than 2 add 1 to 34',
        ]

        for expected_exception in lines_expected_exception:
            with self.assertRaises(IncorrectSyntaxException):
                if_action.IfAction.parse_from_line(expected_exception)

if __name__ == '__main__':
    unittest.main()