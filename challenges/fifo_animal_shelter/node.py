class Node(object):
    '''
    Node in a stack.
    '''

    def __init__(self, spec, tag, _next=None):
        self.spec = spec
        self.tag = tag
        self._next = _next

    def __data__(self):
        return f'{self._data}'

    def __repr__(self):
        return(
            f'<Node | tag: {self.tag} |'
            ' spec: {self.spec} | Prev: {self._next}>'
            )
