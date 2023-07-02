##
#  CIS 501 Data Structures
#  Lab # 1 - Linked Lists and Stacks
#  Application: Balancing Symbols
#  Description:  Test Driver
#  Development Environment:  MacOS Pyenv
#  Version:  Python 3.11.3
#  File:  sebastiancamposea1.py
#  Date:  7/01/23
##

from sebastiancamposstack import Stack, Node


class TestDriver:
    test_inputs: tuple = \
        (
            "([|)]",
            "() (() [()])",
            "{{([][])}()}",
            "asbnmfkhewf",
            "{'json':['array', 'thingy']}",
            "{'json':('array', 'thingy']}"
        )

    @staticmethod
    def validate_char_and_add_to_stack(stack: Stack, char: str) -> bool:
        if Node.validate_data_param(char) is False:
            return False
        if Node.is_opening(char):
            node = Node(char)
            stack.push(node)
        elif Node.is_closing(char):
            if stack.is_empty():
                raise AssertionError('Closing char can not be added to empty stack')
            top_of_stack = stack.peek().data
            if Node.get_matching(top_of_stack) != char:
                raise AssertionError(f'\n\tParsing error:\n\t\topened = {top_of_stack}\n\t\tclosed: {char}')
            stack.pop()
        return True

    @staticmethod
    def test_case_1():
        i = TestDriver.test_inputs[0]
        stack = Stack.create_stack()
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)

    @staticmethod
    def test_case_2():
        i = TestDriver.test_inputs[1]
        stack = Stack.create_stack()
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)

    @staticmethod
    def test_case_3():
        i = TestDriver.test_inputs[2]
        stack = Stack.create_stack()
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)

    @staticmethod
    def test_case_4() -> bool:
        """test pop from empty stack"""
        stack = Stack.create_stack()
        raised_value_error = False
        try:
            stack.pop()
        except ValueError:
            raised_value_error = True
        return raised_value_error

    @staticmethod
    def test_case_5():
        """test non symbol characters"""
        stack = Stack.create_stack()

        i = TestDriver.test_inputs[3]
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)

        i = TestDriver.test_inputs[4]
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)


    @staticmethod
    def test_case_6():
        """test non symbol characters"""
        stack = Stack.create_stack()

        i = TestDriver.test_inputs[5]
        for char in i:
            TestDriver.validate_char_and_add_to_stack(stack, char)



if __name__ == "__main__":
    """
    commented out run
    [PASSED test 1] Assertion error raised for input 1 "([|)]"

	Parsing error:
		opened = [
		closed: )

    [PASSED test 2] No exception raised for input 2 "() (() [()])"
    
    [PASSED test 3] No exception raise for input 3 "{{([][])}()}"
    
    [PASSED test 4] Value error raised when attempting to pop from empty stack
    
    [PASSED test 5] was able to parse "asbnmfkhewf" and "{'json':['array', 'thingy']}" with no error
    
    [PASSED test 6] Assertion error raised for input 6 "{'json':('array', 'thingy']}" unmatched opening "("
    
        Parsing error:
            opened = (
            closed: ]
    
    """
    try:
        TestDriver.test_case_1()
        print('[FAILED TEST 1]')
    except AssertionError as e:
        print(f'[PASSED test 1] Assertion error raised for input 1 "{TestDriver.test_inputs[0]}"')
        print(e)
    try:
        TestDriver.test_case_2()
        print(f'\n[PASSED test 2] No exception raised for input 2 "{TestDriver.test_inputs[1]}"')
    except AssertionError as e:
        print('[FAILED TEST 2]')
        print(e)
    try:
        TestDriver.test_case_3()
        print(f'\n[PASSED test 3] No exception raise for input 3 "{TestDriver.test_inputs[2]}"')
    except AssertionError as e:
        print('[FAILED TEST 3]')
        print(e)

    passed = TestDriver.test_case_4()
    if passed:
        print(f'\n[PASSED test 4] Value error raised when attempting to pop from empty stack')
    else:
        print(f'\n[FAILED TEST 4] Value error NOT raised when attempting to pop from empty stack')

    try:
        TestDriver.test_case_5()
        print(f'\n[PASSED test 5] was able to parse "{TestDriver.test_inputs[3]}" and "{TestDriver.test_inputs[4]}" with no error')
    except AssertionError as e:
        print('\n[FAILED TEST 5]')
        print(e)

    try:
        TestDriver.test_case_6()
        print('\n[FAILED TEST 6]')
    except AssertionError as e:
        print(f'\n[PASSED test 6] Assertion error raised for input 6 "{TestDriver.test_inputs[5]}" unmatched opening "("')
        print(e)
