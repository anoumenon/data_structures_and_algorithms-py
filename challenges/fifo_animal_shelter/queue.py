from node import Node
# from typing import Any


class Queue(object):
    '''
    Singly linked list class as queue.
    '''
    def __init__(self):
        '''
        Instantiation
        O(1) time.
        '''
        self._front = None
        self._back = None

    def __str__(self):
        return(
             f'Front: {self._front}')

    def __repr__(self):
        return(
            f'<Linked List | Front: {self._front}')

    def enqueue(self, animal, tags) -> Node:
        """
        String
        """
        sheltered = Node(animal, tags)

        if self._back:
            self._back._next = sheltered
            self._back = sheltered
        else:
            self._back = sheltered
            self._front = sheltered

    def dequeue(self):
        """
        String
        """
        if self._front:
            return_node = self._front
            return_node._next = None
            if self._front._next:
                self._front = self._front._next
            else:
                self._front = None
            return return_node
        else:
            print('fresh out of them')
            return False
