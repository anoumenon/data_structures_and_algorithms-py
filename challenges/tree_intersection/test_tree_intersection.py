import pytest
from .tree_intersection import tree_intersection
from .bst import BinaryTree


def test_imports():
    """connected to necesary files
    """
    assert pytest
    assert tree_intersection


@pytest.fixture
def tree_a():
    """tree one
    """
    t = BinaryTree([(150, 'a'), (100, 'a'), (250, 'b'), (75, 'c'), (
        160, 'c'), (200, 'c'), (350, 'a'), (125, 'b'), (175, 'c'), (
            300, 'c'), (500, 'c')])
    return t


@pytest.fixture
def tree_b():
    """tree two
    """
    t = BinaryTree([(42, 'a'), (100, 'a'), (600, 'b'), (15, 'c'), (
        160, 'c'), (200, 'c'), (350, 'a'), (125, 'b'), (175, 'c'), (
            4, 'c'), (500, 'c')])
    return t


def test_fixture_contents(tree_a, tree_b):
    """verify that trees have the associated propery to compare
    """
    assert tree_a.contents == [
        150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    assert tree_b.contents == [
        42, 100, 600, 15, 160, 200, 350, 125, 175, 4, 500]


def test_intersection_reads(tree_a, tree_b):
    """verify that comparison is made
    """
    assert tree_intersection(tree_a, tree_b) == [
        100, 160, 200, 350, 125, 175, 500]
