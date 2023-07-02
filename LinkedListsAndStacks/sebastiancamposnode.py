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

    def __init__(self, data: str, next_node: Self or None = None):
        """
        Builds a node instance
        :param data: string data for node value
        :param next_node: Instance of Node optional arg
        """
        if self.validate_data_param(data) is False:
            raise ValueError("InvalidCharacter")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """String value of node"""
        return self._data

    @property
    def next_node(self):
        """
        Returns the adjacent node or none if none exist
        :return: Node or None
        """
        return self._next_node

    @data.setter
    def data(self, new_data: str):
        """
        Setter for private data attribute
        :param new_data:
        :return: void
        """
        self._data = new_data

    @next_node.setter
    def next_node(self, new_node):
        """
        Sets the next node value, raises and error
        if new_node is not of type Node
        :param new_node: Node instance
        :return: void
        """
        if type(new_node) != Node:
            raise ValueError('Can not add non Node class as next node')
        self._next_node = new_node

    def has_next_node(self) -> bool:
        """
        Returns True if current instance has
        a next node value that is not none
        :return: bool
        """
        return self.next_node is not None

    @staticmethod
    def validate_data_param(char: str) -> bool:
        """
        Returns True if char is a valid symbol
        :param char: string character
        :return: bool
        """
        return char in "({[]})"

    @staticmethod
    def is_opening(char: str) -> bool:
        """
        Returns True if char is a valid opening symbol
        :param char: string character
        :return: bool
        """
        return char in "({["

    @staticmethod
    def is_closing(char: str) -> bool:
        """
        Returns True if char is a valid closing symbol
        :param char: string character
        :return: bool
        """
        return char in "]})"

    @staticmethod
    def get_matching(char: str) -> str:
        """
        Returns the matching symbol for the given
        char, or empty string if char is not a valid symbol
        :param char: string character
        :return: bool
        """
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
