from node import Node
from typing import Any


class Queue(object):
    '''
    Singly linked list creation.
    O(1) time.
    '''
    def __init__(self, iterable=[]):
        '''
        Initialized the list with a set of values, contained in an iterable.
        O(n) time.
        '''
        self._front = None
        self._back = None
        self._length = 0

        if len(iterable) >= 1:
            for e in iterable:
                self.enqueue(e)

    def __str__(self):
        return(
             f'Front: {self._front} | '
             'Back: {self._back} | Length: {self._length}')

    def __repr__(self):
        return(
            f'<Linked List | Front: {self._front} |'
            ' Back: {self._back} | Length: {self._length}>')

    def __len__(self):
        """
        Returns the length of the queue.
        """
        curr = self._front
        len = 0
        while curr:
            curr = curr._prev
            len += 1
        return len

    def enqueue(self, data: Any) -> Node:
        """
        Adds a node to the back of the queue
        """
        if self._back:
            new_node = Node(data, _next=self._back)
            self._back._prev = new_node
            self._back = new_node
        else:
            new_node = Node(data)
            self._back = new_node
            self._front = new_node
        self._length += 1

    def dequeue(self):
        """
        Removes from the front of the queue and returns
        """
        if self._front:
            return_node = self._front
            if self._front._prev:
                self._front = self._front._prev
                return_node._prev = None
                self._front._next = None
            else:
                self._front = None
        self._length -= 1
        return return_node
