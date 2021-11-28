import unittest
import actions.math_actions as math_action
import variables

class ExpectedResult():
    def __init__(self, line, _type, expected_result, reason=''):
        self.line = line
        self.items = self.line.split()
        self.type = _type
        self.expected_result = expected_result
        self.reason = reason
    


class TestMathActions(unittest.TestCase):

    def test_parsing_and_actions(self):
        lines_to_test = [
            ExpectedResult('add 1 to 1', math_action.AddAction, 2, 'Add 2 integers'),
            ExpectedResult('add value_is_5 to 1', math_action.AddAction, 6, 'Add 1 integer and 1 variable'),
            ExpectedResult('add value_is_5 to value_is_10', math_action.AddAction, 15, 'Add 2 variables'),
            
            ExpectedResult('subtract 1 from 50', math_action.SubAction, 49, 'Subtract 2 integers'),
            ExpectedResult('subtract value_is_5 from 50', math_action.SubAction, 45, 'Subtract 1 integer and 1 variable'),
            ExpectedResult('subtract value_is_5 from value_is_10', math_action.SubAction, 5, 'Subtract 2 variables'),

            ExpectedResult('multiply 5 by 8', math_action.MultAction, 40, 'Multiply 2 integers'),
            ExpectedResult('multiply value_is_5 by 5', math_action.MultAction, 25, 'Multiply 1 integer and 1 variable'),
            ExpectedResult('multiply value_is_5 by value_is_10', math_action.MultAction, 50, 'Multiply 2 variables'),

            ExpectedResult('divide 100 by 5', math_action.DivAction, 20, 'Divide 2 integers'),
            ExpectedResult('divide value_is_5 by 5', math_action.DivAction, 1, 'Divide integer and 1 variable'),
            ExpectedResult('divide value_is_5 by value_is_10', math_action.DivAction, 0.5, 'Divide 2 variables'),

            ExpectedResult('modulo 5 by 3', math_action.ModAction, 2, 'Modulo 2 integers'),
            ExpectedResult('modulo value_is_5 by 2', math_action.ModAction, 1, 'Modulo 1 integer and 1 variable'),
            ExpectedResult('modulo value_is_5 by value_is_10', math_action.ModAction, 5, 'Modulo 2 variables'),

        ]
        
        for expected_res in lines_to_test:
            my_variables = variables.Variables()
            my_variables.add('value_is_5', 5)
            my_variables.add('value_is_10', 10)
            with self.subTest(msg=f'Test {expected_res.reason}: "{expected_res.line}" is of type {expected_res.type} with result {expected_res.expected_result}'):
                parsed_action = math_action.MathAction.parse_from_line(expected_res.items)
                self.assertIsInstance(parsed_action, expected_res.type )
                action_res = parsed_action.action(my_variables)
                self.assertEqual(action_res, expected_res.expected_result)



if __name__ == '__main__':
    unittest.main()