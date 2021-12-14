#!/usr/bin/python3
""" Module defines a class node of a singly linked
list and Singly linked list """


class Node:
"""  Class defines a node """
    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self)
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
""" Class defines SinglyLinkedList """
    __head = None

    def __init__(self):
        self.__head = __head

    def sorted_insert(self, value):
        self
