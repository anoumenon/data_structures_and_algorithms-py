import random


class Node(object):
    '''
    Node in a singly linked list.
    '''

    def __init__(self, val, _left=None, _right=None):
        self.val = val
        self._left = _left
        self._right = _right
        self._parent = None

    def __val__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | val: {self.val}>'


class BinaryTree(object):
    '''
    Singly linked list creation.
    O(1) time.
    '''
    def __init__(self, iterable=[]):
        '''
        Initialized the list with a set of values, contained in an iterable.
        O(n) time.
        '''
        self.root = None
        self.count = 0

    def __str__(self):
        return f'Root: {self.root} | Count: {self.count}'

    def __repr__(self):
        return f'<Binary Tree | Root: {self.root} | Count: {self.count}>'

    def __len__(self):
        """
        Returns the length of the linked list.
        O(n) time
        """
        pass

    def insert_above(self, val, target):
        """Insert a node of the value given above a node with a target val.
        Parent maintains branch side.
        """
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        def _walk(node):
            if val == target:
                print('duplicate value')
                raise IndexError

            if node.val == target:
                # Target aquired
                # if not inserting before root:
                if node._parent:
                    new_node._parent = node._parent
                    # to which side is this node from it's parent?
                    # Maintain child orientations.
                    if node._parent._left == node:
                        new_node._left = node
                        node._parent._left = new_node
                        self.count += 1
                        return
                    elif node._parent._right == node:
                        new_node._right = node
                        node._parent._right = new_node
                        self.count += 1
                        return
                # Insert before root? make new root.
                # Old head left or right? random.
                else:
                    rand = random.randint(1, 3)
                    if rand > 1:
                        new_node._right = self.root
                    else:
                        new_node._left = self.root
                    self.root = new_node
                    self.count += 1
                    return
            # keep searching
            else:
                if node._left:
                    _walk(node._left)
                if node._right:
                    _walk(node._right)

            return False

        _walk(self.root)

    def insert_below(self, val, target, side='L'):
        """Insert a node of a val below to the L or R of a node with a target val
        Children maintain branch side.
        """
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        def _walk(node):
            if node.val == target:
                if side is 'L':
                    if node._left:
                        new_node._left = node._left
                        node._left = new_node
                        self.count += 1
                        return
                    else:
                        node._left = new_node
                        self.count += 1
                        return

                elif side is 'R':
                    if node._right:
                        new_node._right = node._right
                        node._right = new_node
                        self.count += 1
                        return
                    else:
                        node._right = new_node
                        self.count += 1
                        return

            else:
                if node._left:
                    _walk(node._left)
                if node._right:
                    _walk(node._right)

        _walk(self.root)

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
