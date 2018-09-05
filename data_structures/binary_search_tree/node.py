class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'<Node | Val: {self.value} | Next: {self._next}>'
