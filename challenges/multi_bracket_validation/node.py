class Node(object):
    '''
    Node in a singly linked list.
    '''

    def __init__(self, data, _next=None):
        self._data = data
        self._next = _next

    def __data__(self):
        return f'{self._data}'

    def __repr__(self):
        return f'<Node | data: {self._data} | Next: {self._next}>'
