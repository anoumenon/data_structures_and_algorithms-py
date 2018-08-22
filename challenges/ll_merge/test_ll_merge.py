from .linked_list import LinkedList
from .ll_merge import merge_lists
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def list_a_short():
    ll_a = LinkedList(['a', 'b', 'c', 'd'])
    return ll_a


@pytest.fixture
def list_a_long():
    ll_a = LinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    return ll_a


@pytest.fixture
def list_b_short():
    ll_b = LinkedList([1, 2, 3, 4, 5])
    return ll_b


@pytest.fixture
def list_b_long():
    ll_b = LinkedList([1, 2, 3, 4, 5, 6, 7])
    return ll_b


def test_linked_list_exists():
    '''
    Check creation of list
    '''
    assert LinkedList
