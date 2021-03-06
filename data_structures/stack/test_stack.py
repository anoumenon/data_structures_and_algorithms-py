from stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def triple_stack():
    return Stack([1, 2, 3])


def test_stack_exists():
    """
    Check stack import
    """
    assert empty_stack


def test_stack_stacks_iterable(triple_stack):
    """
    assert that the stack can be instantiated with nodes
    """
    assert len(triple_stack) == 3


def test_stack_push(triple_stack):
    """
    assert that a node my be removed and returned with pop
    """
    assert len(triple_stack) == 3
    taller = triple_stack.push(4)
    assert len(triple_stack) == 4
    assert taller


def test_stack_pop(triple_stack):
    """
    assert that a node my be removed and returned with pop
    """
    assert len(triple_stack) == 3
    pop_node = triple_stack.pop()
    assert len(triple_stack) == 2
    assert pop_node


def test_stack_pop_value(triple_stack):
    """
    assert that the last value pushed is first removed
    """
    assert len(triple_stack) == 3
    pop_node = triple_stack.pop()
    assert len(triple_stack) == 2
    assert pop_node._data == 3


def test_pop_empty_false(empty_stack):
    """
    assert that trying to pop and empty stack returns false
    """
    assert len(empty_stack) == 0
    pop_node = empty_stack.pop()
    assert pop_node is False
