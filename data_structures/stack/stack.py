from node import Node
from typing import Any


class Stack(object):
    '''
    Singly linked list creation.
    O(1) time.
    '''
    def __init__(self, iterable=[]):
        '''
        Initialized the list with a set of values, contained in an iterable.
        O(n) time.
        '''
        self._top = None
        self._length = 0

        if len(iterable) >= 1:
            for e in iterable:
                self.push(e)

    def __str__(self):
        return f'Top: {self._top} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Top: {self._top} | Length: {self._length}>'

    def __len__(self):
        """
        Returns the length of the linked list.
        O(n) time
        """
        curr = self._top
        count = 0
        while curr:
            count += 1
            curr = curr._next

        return self._length

    def push(self, data: Any) -> Node:
        """
        Adds a node to the head/top of the stack
        """
        if data is None:
            print('data absent')
            return False
        else:
            self._top = Node(data, self._top)
            self._length += 1
            return True

    def pop(self):
        """
        Removes and returns the top node in the stack
        and reasignes the nodes next node to the top.
        """
        if self._top:
            pop_node = self._top
        else:
            return False

        if self._top._next:
            self._top = self._top._next
        else:
            self._top = None

        self._length -= 1
        pop_node._next = None
        return pop_node

    def peek(self):
        """
        Takes no arguments and returns the Node at the top of the stack
        """
        if self._top:
            return self._top
        else:
            return False
