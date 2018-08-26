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


def test_equal_length_lists(list_a_short, list_b_short):
    '''
    Standard merge given two short lists
    '''
    merged = merge_lists(list_a_short, list_b_short)
    read = merged.read_off()
    assert read == (['a', 1, 'b', 2, 'c', 3])


def test_list_one_longer(list_a_long, list_b_short):
    '''
    Standard merge given a long and short list
    '''
    merged = merge_lists(list_a_long, list_b_short)
    read = merged.read_off()
    assert read == (['a', 1, 'b', 2, 'c', 3, 'd', 'e', 'f', 'g'])


def test_list_two_longer(list_a_short, list_b_long):
    '''
    Standard merge given a long and short list
    '''
    merged = merge_lists(list_a_short, list_b_long)
    read = merged.read_off()
    assert read == (['a', 1, 'b', 2, 'c', 3, 4, 5, 6, 7])


def test_empty_first_list(empty_list, list_a_short):
    '''
    Standard merge given a long and short list
    '''
    merged = merge_lists(empty_list, list_a_short)
    assert merged == 'first list empty'


def test_empty_second_list(list_a_short, empty_list):
    '''
    Standard merge given a long and short list
    '''
    merged = merge_lists(list_a_short, empty_list)
    assert merged == 'second list empty'
