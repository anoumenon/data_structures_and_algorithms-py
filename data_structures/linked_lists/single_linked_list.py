from sl_node import ListNode
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

    def prepend(self, data: Any) -> ListNode:
        '''
        Add node to singly-linked list creation at head.
        O(1) time.
        '''
        if data is None:
            print('data absent')
            return False
        else:
            new_node = ListNode(data)
            new_node._next = self.head
            self.head = new_node
            self._length += 1
            print(self)
            return new_node

    def append(self, data: Any) -> ListNode:
        '''
        Add node to singly-linked list creation at tail.
        O(n) time.
        '''
        if data is None:
            print('data absent')
            return False

        else:
            new_node = ListNode(data)

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

    def find(self, data: Any) -> bool:
        if self.head is None:
            print(False)
            return False
        else:
            if self.head.data == data:
                print('Contains ' + str(data))
                return True
            else:
                curr = self.head
                while curr._next:
                    if curr.data == data:
                        print('Contains ' + str(data))
                        return True
                    curr = curr._next
                if curr.data == data:
                    print('Contains ' + str(data))
                    return True

        print('Doesn\'t contain ' + str(data))
        return False


ll = LinkedList()

ll.append('a')
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('e')
print(ll)
