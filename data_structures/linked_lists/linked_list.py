from node import Node
from typing import Any


class LinkedList(object):
    '''
    Singly linked list creation.
    O(1) time.
    '''
    def __init__(self):

        self.head = None
        self._length = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    # def __iter__(self):
    #     pass
    # Dunder  init str repr len
    # reg prepend append find
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
            self.head = Node(data, self.head)
            self._length += 1


            # new_node = ListNode(data)
            # new_node._next = self.head
            # self.head = new_node
            # self._length += 1

            print(self)
            return self.head

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

            if self.head is None:
                self.head = new_node
                self._length += 1
                print('appended ' + str(new_node) + ' as head')
                return new_node

            else:
                curr = self.head
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
        if self.head is None:
            print('No head.')
            return False

        else:
            curr = self.head
            pos = 0
            while curr is not None:
                if curr.data == data:
                    print('Contains ' + str(data) + ' at pos: ' + str(pos))
                    return (True, pos)
                curr = curr._next
                pos += 1

            print('Doesn\'t contain ' + str(data))
            return False

    def insert_before(self, i_data, s_data):
        '''
        Moves through the list searching for a target val.
        Places a new node in the list before that val.
        O(n) time.
        '''
        if self.head is None:
            print('no list for insertion')
            return False

        curr = self.head
        while curr.next.data is not s_data:
            curr = curr.next

        new_node = Node(i_data)
        new_node.next, curr.next = curr.next, new_node

    def insert_after(self, i_data, s_data):
        '''
        Moves through the list searching for a target val.
        Places a new node in the list after that val.
        O(n) time.
        '''
        if self.head is None:
            print('no list for insertion')
            return False

        curr = self.head
        while curr.data != s_data:
            curr = curr.next
            if curr is None:
                print('target not found, node not appended')
                return(False)
        new_node = Node(i_data)
        new_node.next, curr.next = curr.next, new_node

    # def insert(self, data: Any):

    #     self.head = ListNode(data, self.head)
    #     self._length += 1


# .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node


ll = LinkedList()

ll.append('a')
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
ll.prepend('prepended')
