##
#  CIS 501 Data Structures
#  Lab # 1 - Linked Lists and Stacks
#  Application: Balancing Symbols
#  Description:  Test Driver
#  Development Environment:  MacOS Pyenv
#  Version:  Python 3.11.3
#  File:  sebastiancamposstack.py
#  Date:  7/01/23
##

from sebastiancamposnode import Node


class Stack:
    """Using the Node Class manages the linked list of nodes as a stack"""
    _top_of_stack: Node or None

    @staticmethod
    def validate_stack_is_not_empty(func):
        """Decorator used to raise value error if the stack is empty"""
        def _is_stack_empty(self, *args, **kwargs):
            if self.is_empty():
                raise ValueError("Stack is empty")
            return func(self, *args, **kwargs)

        return _is_stack_empty

    @classmethod
    def create_stack(cls, data: str or None = None):
        """
        Creates an instance of the Stack Class
        :param data: optional arg, will instantiate the class with a node with the value of data
        :return: Stack Instance
        """
        if data is None:
            return cls()
        return cls(data)

    @classmethod
    def delete_stack(cls):
        """
        deletes the stack class
        :return:
        """
        del cls

    def __init__(self, data: str or None = None):
        """
        Stack instance constructor
        :param data: optional arg, will instantiate the class with a node with the value of data
        :return: Stack Instance
        """
        if data is None:
            self._top_of_stack = None
        else:
            self._top_of_stack = Node(data)

    def __str__(self):
        string = ""
        if self.is_empty():
            return string
        tmp_node = self.top_of_stack
        while tmp_node.has_next_node():
            string += tmp_node.data + "\n"
            tmp_node = tmp_node.next_node
        return string

    @property
    def top_of_stack(self) -> Node:
        """
        Getter for the top of the stack
        :return: Node
        """
        return self._top_of_stack

    @top_of_stack.setter
    def top_of_stack(self, new_node: Node) -> None:
        """
        Setter for the top of the stack
        :return: void
        """
        if self._top_of_stack is not None:
            new_node.next_node = self._top_of_stack
            self._top_of_stack = new_node
            return
        self._top_of_stack = new_node

    def push(self, new_node: Node) -> None:
        """
        Pushes a node to the top of the stack
        :param new_node: Node
        :return: void
        """
        self.top_of_stack = new_node

    @validate_stack_is_not_empty
    def pop(self) -> None:
        """
        removes node from top of stack
        :return: void
        """
        node = self.top_of_stack
        if self._top_of_stack.has_next_node():
            self._top_of_stack = node.next_node
        else:
            self._top_of_stack = None

    @validate_stack_is_not_empty
    def peek(self):
        """
        Returns the Node on top of the stack
        :return: Node
        """
        return self.top_of_stack

    def is_empty(self) -> bool:
        """
        Returns True if stack is empty
        :return:
        """
        return self.top_of_stack is None

