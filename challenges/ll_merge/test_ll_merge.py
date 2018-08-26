from .linked_list import LinkedList
from .ll_merge import merge_lists
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def empty_list2():
    return LinkedList()


@pytest.fixture
def list_a_short():
    ll_a = LinkedList(['a', 'b', 'c'])
    return ll_a


@pytest.fixture
def list_a_long():
    ll_a = LinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    return ll_a


@pytest.fixture
def list_b_short():
    ll_b = LinkedList([1, 2, 3])
    return ll_b


@pytest.fixture
def list_b_long():
    ll_b = LinkedList([1, 2, 3, 4, 5, 6, 7])
    return ll_b


def test_linked_list_exists():
    '''
    Check linked_list import
    '''
    assert empty_list


def test_merge_function_exists():
    '''
    Check ll_merge import
    '''
    assert merge_lists


def test_Index_error_for_empty_lists(empty_list, empty_list2):
    '''
    If passed two empty lists
    '''
    merged = merge_lists(list_a_short, list_b_short)
    assert merged == 'No nodes to test'
