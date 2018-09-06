# from .tqueue import Queue


class Node(object):
    """
    BST node.
    """

    def __init__(self, val, data, left=None, right=None, parent=None):
        """
        BST node.
        VAL for structure.
        DATA for information.
        LEFT and RIGHT children.
        PARENT for preceeding node.
        """
        self.val = val
        self.data = data
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        """
        return val and data of node
        """
        return(
            f'''VAL:{self.val} | DATA:{self.data}'''
        )

    def __repr__(self):
        """
        return val and children
        """
        return f'<Node | VAL:{self.val} | L: {self._left} | R: {self._right}>'


class BinaryTree:
    """
    Binary tree class.
    """
    def __init__(self, iterable=[]):
        """
        ROOT for head.
        COUNT for number of nodes held.
        """
        self.root = None
        self.count = 0
        for e in iterable:
            self.insert(val=e[0], data=e[1])

    def __str__(self):
        """
        return self information
        """
        return f'Root: {self.root} | Count: {self.count}'

    def __repr__(self):
        """
        return self information
        """
        return f'<Linked List | Root: {self.root} | Count: {self.count}>'

    def insert(self, val=None, data=None):
        """
        Creates a root of absent.
        Else, traverses by vals to append data.
        """

        if self.root is None:
            self.root = Node(val, data)
            self.count += 1
            return self.root

        node = self.root

        def _search_place(node, parent=None):
            """
            Called recursively to traverse and append.
            """
            # LEFT
            if val < node.val:
                if node._left is None:
                    node._left = Node(val, data, parent=node)
                    self.count += 1
                    return
                else:
                    return _search_place(node._left, node)
            # RIGHT
            elif val > node.val:
                if node._right is None:
                    node._right = Node(val, data, parent=node)
                    self.count += 1
                    return
                else:
                    return _search_place(node._right, node)
            # DUPLICATE
            elif val == node.val:
                raise ValueError
            # EDGE
            else:
                return False

        _search_place(node)

    def __inorder__(self, callable=lambda node: print(node)):

        """
        Go left, visit, go right.
        """
        def _walk(node=None):
            if node is None:
                return

            if node._left:
                _walk(node._left)

            callable(node)

            if node._right:
                _walk(node._right)

        _walk(self.root)

    def __preorder__(self, callable=lambda node: print(node)):

        """
        Visit, go left, go right.
        """
        def _walk(node=None):
            if node is None:
                return

            callable(node)

            if node._left:
                _walk(node._left)

            if node._right:
                _walk(node._right)

        _walk(self.root)

    def __postorder__(self, callable=lambda node: print(node)):

        """
        Left, right, visit.
        """
        def _walk(node=None):
            if node is None:
                return

            if node._left:
                _walk(node._left)

            if node._right:
                _walk(node._right)

            callable(node)

        _walk(self.root)

    def ordered_vals(self, type='in'):
        """
        Calls the specified traversal method,
        collects each val into a list and returns the list.
        """
        vals = []

        def _report(node):
            vals.append(node.val)

        if type == 'pr':
            self.__preorder__(_report)

        elif type == 'in':
            self.__inorder__(_report)

        elif type == 'po':
            self.__postorder__(_report)

        else:
            raise ValueError

        return vals

    def breadth_first_traversal(self):
        """
        Reaverses in breadth using a queue,
        prints and returns list of values.
        """
        queue = []

        def stack_o_rama(node):
            # FIFO:
            # push on | shift off
            queue.push(node.val)
