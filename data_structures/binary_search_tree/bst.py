class Node(object):
    """
    BST node.
    VAL for structure
    DATA for information
    LEFT and RIGHT children
    """

    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self._left = left
        self._right = right
        self._parent = None

    def __str__(self):
        pass

    def __repr__(self):
        pass


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None
        self.count = 0
        for e in iterable:
            self.__insert__(e[0], e[1])

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __insert__(self, val, data):

        if self.root is None:
            self.root = Node(val, data)
            self.count += 1
            return

        node = self.root

        def _insert(node):
            if val < node.val:
                if node._left is None:
                    node._left = Node(val, data)
                    self.count += 1
                    return
                else:
                    return _insert(node._left)
            elif val > node.val:
                if node._right is None:
                    node._right = Node(val, data)
                    self.count += 1
                    return
                else:
                    return _insert(node._right)
            else:
                return False

        _insert(node)

    def __inorder__(self, callable=lambda node: print(node)):

        """
        Go left, visit, go right.
        """
        def _walk(node=None):
            if node is None:
                return

            if node.left:
                _walk(node.left)

            callable(node)

            if node.right:
                _walk(node.right)

        _walk(self.root)

    def __preorder__(self, callable=lambda node: print(node)):

        """
        Visit, go left, go right.
        """
        def _walk(node=None):
            if node is None:
                return

            callable(node)

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)

    def __postorder__(self, callable=lambda node: print(node)):

        """
        Left, right, visit.
        """
        def _walk(node=None):
            if node is None:
                return

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

            callable(node)

        _walk(self.root)
