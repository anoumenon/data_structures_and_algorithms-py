from .node import Node
from typing import Any


class LinkedList(object):
    '''
    Singly linked list creation.
    O(1) time.
    '''
    def __init__(self, iterable=[]):
        '''
        Initialized the list with a set of values, contained in an iterable.
        O(n) time.
        '''
        self._head = None
        self._length = 0
        if len(iterable) >= 1:
            for e in iterable:
                self.append(e)

    def __str__(self):
        return f'Head: {self._head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self._head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    # def __iter__(self):
    #     pass

    # def __next__(self):
    #     pass

    def prepend(self, data: Any) -> Node:
        '''
        Add node to singly-linked list creation at head.
        O(1) time.
        '''
        if data is None:
            print('data absent')
            return False
        else:
            self._head = Node(data, self._head)
            self._length += 1
            return True

    def append(self, data: Any) -> Node:
        '''
        Add node to singly-linked list creation at tail.
        O(n) time.
        '''
        if data is None:
            print('data absent')
            return False

        else:
            new_node = Node(data)

            if self._head is None:
                self._head = new_node
                self._length += 1
                # print('appended ' + str(new_node) + ' as head')
                return new_node

            else:
                curr = self._head
                while curr._next:
                    curr = curr._next

                curr._next = new_node
                self._length += 1
                return new_node

    def includes(self, data: Any) -> bool:
        '''
        Search the linked list for for a given value.
        O(n) time.
        '''
        if self._head is None:
            print('No head.')
            return False

        else:
            curr = self._head
            pos = 0
            while curr is not None:
                if curr._data == data:
                    print('Contains ' + str(data) + ' at pos: ' + str(pos))
                    return (True)
                curr = curr._next
                pos += 1

            print('Doesn\'t contain ' + str(data))
            return False

    def read_off(self):
        '''
        Reads off the values in order.
        O(n) time
        '''
        vals = []

        if self._head is not None:
            curr = self._head
            while curr:
                vals.append(curr._data)
                curr = curr._next
            print(vals)
            return(vals)

    def insert_before(self, i_data, s_data):
        '''
        Add a new node with the given i_data immediately
        before the first s_data node
        O(n) time.
        '''
        if self._head is not None:

            curr = self._head
            n = Node(i_data)

            if self._head._data == s_data:
                n._next, self._head = curr, n
                self._length += 1
            else:
                prev = None
                while curr:
                    if curr._data == s_data:
                        n._next, prev._next = curr, n
                        self._length += 1
                    prev, curr = curr, curr._next

    def insert_after(self, i_data, s_data):
        '''
        Add a new node with the given i_data immediately
        after the first s_data node
        O(n) time.
        '''
        if self._head is not None:

            n = Node(i_data)
            curr = self._head

            while curr:
                if curr._data == s_data:
                    n._next = curr._next
                    curr._next = n
                    self._length += 1
                curr = curr._next

    def kth_from_end(self, k):
        '''
        Moves down the linked list to find
        a node that is k pisitions from the tail of the list.
        tortise and hare solution.
        O(n) time.
        '''

        t = self._head
        h = self._head

        for i in range(k):
            if h is not None:
                h = h._next
            else:
                raise IndexError

        while h._next is not None:
            t = t._next
            h = h._next

        return t._data
