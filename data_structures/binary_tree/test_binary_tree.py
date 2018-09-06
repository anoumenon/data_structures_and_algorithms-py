from .binary_tree import BinaryTree
import pytest


@pytest.fixture
def empty_tree():
    return BinaryTree()


def test_tree_import():
    '''
    Finds Fx
    '''
    assert BinaryTree


def test_tree_instance(empty_tree):
    '''
    Check tree instantiation
    '''
    assert empty_tree.root is None
