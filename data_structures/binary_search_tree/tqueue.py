from .node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        """
        Returns a nicely formatted display of Queue
        """
        current_node = self.front
        output = f'(Head: {self.front})'

        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'

        return output + ''

    def __len__(self):
        """
        Return length of Queue
        """
        return self._length

    def enqueue(self, value):
        """
        Accepts a value of any type and creates a new Node in the Queue.
        Args: value (object): Any
        Return: Node
        """
        if not self.front:
            self.front = Node(value)

        else:
            newNode = Node(value)
            current = self.front

            while current._next:
                current = current._next
            current._next = newNode

            self.back = Node(value)

        self._length += 1

        return self.front

    def dequeue(self):
        """
        Removes and returns the first value in the queue
        """
        temp = self.front
        self.front = temp._next
        temp._next = None

        self._length -= 1
        return temp.value

    def peek(self):
        """
        Show node at front of stack
        """
        return self.front.value
