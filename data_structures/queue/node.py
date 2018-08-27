class Node(object):
    '''
    Node in a stack.
    '''

    def __init__(self, data, _next=None, _prev=None):
        self._data = data
        self._next = _next
        self._prev = _prev

    def __data__(self):
        return f'{self._data}'

    def __repr__(self):
        return(
            f'<Node | data: {self._data} |'
            ' Next: {self._next} | Prev: {self._prev}>'
            )
