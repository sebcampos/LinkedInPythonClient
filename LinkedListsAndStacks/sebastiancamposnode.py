##
#  CIS 501 Data Structures
#  Lab # 1 - Linked Lists and Stacks
#  Application: Balancing Symbols
#  Description:  Test Driver
#  Development Environment:  MacOS Pyenv
#  Version:  Python 3.11.3
#  File:  sebastiancamposnode.py
#  Date:  7/01/23
##


from typing import Self


class Node:
    """Node class to be used in a linked list emulating a Stack Structure"""
    _data: str
    _next_node: Self or None

    def __init__(self, data: str, next_node: Self or None = None) -> Self:
        if self.validate_data_param(data) is False:
            raise ValueError("InvalidCharacter")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @property
    def next_node(self):
        return self._next_node

    @data.setter
    def data(self, new_data: str):
        self._data = new_data

    @next_node.setter
    def next_node(self, new_node):
        self._next_node = new_node

    def has_next_node(self) -> bool:
        return self.next_node is not None

    @staticmethod
    def validate_data_param(char: str) -> bool:
        return char in "({[]})"

    @staticmethod
    def is_opening(char: str) -> bool:
        return char in "({["

    @staticmethod
    def is_closing(char: str) -> bool:
        return char in "]})"

    @staticmethod
    def get_matching(char: str) -> str:
        correct_match: str
        match char:
            case "{":
                correct_match = "}"
            case "}":
                correct_match = "{"
            case "[":
                correct_match = "]"
            case "]":
                correct_match = "["
            case "(":
                correct_match = ")"
            case ")":
                correct_match = "("
            case _:
                correct_match = ""
        return correct_match
