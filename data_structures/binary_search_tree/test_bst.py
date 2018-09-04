from .bst import BinaryTree
import pytest


# FIXTURES


@pytest.fixture
def empty_bt():
    return BinaryTree()


@pytest.fixture
def root_tree():
    root_tree = BinaryTree([(8888, 'port')])
    return root_tree


@pytest.fixture
def tri_tree():
    tri_tree = BinaryTree([(3, 'a'), (1, 'b'), (5, 'c')])
    return tri_tree


@pytest.fixture
def five_tree():
    five_tree = BinaryTree([(3, 'a'), (1, 'b'), (5, 'c'), (2, 'c'), (.5, 'c')])
    return five_tree


@pytest.fixture
def com_tree():
    com_tree = BinaryTree([[3, 'a'], (.1, (
        'eggs', 'spam')), (500000, {50: 50})])
    return com_tree


# INSTANTIATION


def test_binary_tree_exists():
    """tree import
    """
    assert empty_bt


def test_root_tree(root_tree):
    """class inserts root
    """
    assert root_tree.root


# Node instantiation and appendage;

def test_insert_root(empty_bt):
    """insert a single node to an empty tree.
    """
    empty_bt.insert(315, 'Bloggity-blog-blogy-blog')
    assert empty_bt.count == 1


def test_insert_single(empty_bt):
    """insert a single node to an empty tree.
    """
    empty_bt.insert(315, 'Bloggity-blog-blogy-blog')
    assert empty_bt.count == 1
    empty_bt.insert(777, 'Bloggity-blog-blogy-blog')
    assert empty_bt.count == 2


def test_node_val(root_tree):
    """root recieves val after insert
    """
    assert root_tree.root.val == 8888


def test_node_data(root_tree):
    """root recieves data after import
    """
    assert root_tree.root.data == 'port'


def test_node_insert_by_count(tri_tree):
    """insert adds to count
    """
    assert tri_tree.count == 3


def test_L_child_val(tri_tree):
    """left node insertion val
    """
    assert tri_tree.root._left.val == 1


def test_L_child_data(tri_tree):
    """right node insertion data
    """
    assert tri_tree.root._left.data == 'b'


def test_R_child_val(tri_tree):
    """rigt node insertion val
    """
    assert tri_tree.root._right.val == 5


def test_R_child_data(tri_tree):
    """right node insertion data
    """
    assert tri_tree.root._right.data == 'c'


def test_L_child_parent(tri_tree):
    """left node insertion parent
    """
    assert tri_tree.root._left._parent.val == 3


def test_R_child_parent(tri_tree):
    """right node insertion parent
    """
    assert tri_tree.root._right._parent.val == 3


def test_complex_L_child_val(com_tree):
    """complex data
    """
    assert com_tree.root._left.val == .1


def test_complex_L_child_data(com_tree):
    """complex data
    """
    assert com_tree.root._left.data == ('eggs', 'spam')


def test_complex_R_child_val(com_tree):
    """complex data
    """
    assert com_tree.root._right.val == 500000


def test_complex_R_child_data(com_tree):
    """complex data
    """
    assert com_tree.root._right.data == {50: 50}


# TRAVERSAL


def test_preorder_traversal(five_tree):
    """ordered retrieval of nodes by val
    """
    values = five_tree.collect_vals('pr')
    assert values == [3, 1, 0.5, 2, 5]


def test_inorder_traversal(five_tree):
    """ordered retrieval of nodes by val
    """
    values = five_tree.collect_vals('in')
    assert values == [0.5, 1, 2, 3, 5]


def test_postorder_traversal(five_tree):
    """ordered retrieval of nodes by val
    """
    values = five_tree.collect_vals('po')
    assert values == [0.5, 2, 1, 5, 3]
