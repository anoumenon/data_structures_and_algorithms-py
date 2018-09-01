from bst import BinaryTree
import pytest


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
def com_tree():
    com_tree = BinaryTree([(3, 'a'), (.1, ('eggs', 'spam')), (5, {50: 50})])
    return com_tree


def test_binary_tree_exists():
    assert empty_bt


def test_root_tree(root_tree):
    assert root_tree.root


def test_node_val(root_tree):
    assert root_tree.root.val == 8888


def test_node_data(root_tree):
    assert root_tree.root.data == 'port'


def test_node_insert_by_count(tri_tree):
    assert tri_tree.count == 3


def test_L_child_val(tri_tree):
    assert tri_tree.root._left.val == 1


def test_L_child_data(tri_tree):
    assert tri_tree.root._left.data == 'b'


def test_R_child_val(tri_tree):
    assert tri_tree.root._right.val == 5


def test_R_child_data(tri_tree):
    assert tri_tree.root._right.data == 'c'


def test_complex_L_child_val(com_tree):
    assert com_tree.root._left.val == .1


def test_complex_L_child_data(com_tree):
    assert com_tree.root._left.data == ('eggs', 'spam')


def test_complex_R_child_val(com_tree):
    assert com_tree.root._right.val == 5


def test_complex_R_child_data(com_tree):
    assert com_tree.root._right.data == {50: 50}
