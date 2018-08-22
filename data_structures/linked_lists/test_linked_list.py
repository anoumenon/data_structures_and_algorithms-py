from .linked_list import LinkedList
from .node import Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    return ll

def test_linked_list_exists():
    '''
    Finds Fx
    '''
    assert LinkedList

def test_init_with_list():
    '''
    Check init with input list
    '''
    ll = LinkedList([1, 2, 3])
    assert ll.read_off() == [1, 2, 3]

def test_create_instance_of_node():
    '''
    Node creation
    '''
    n = Node('x')
    assert isinstance(n, Node)


def test_create_instance_of_list():
    '''
    List instantiation
    '''
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    '''
    Test for head attribute on list class
    '''
    assert empty_list._head is None


def test_default_property_length(empty_list):
    '''
    Test for length attribute on list class
    '''
    assert empty_list._head is None
    assert empty_list._length == 0


def test_read_off_reads_off(small_list):
    '''
    Test for itteration and collection of node data
    '''
    assert small_list.read_off() == [1, 2, 3, 4]


def test_append_successful_to_empty(empty_list):
    '''
    appending when list is empty, adds as head
    '''
    assert empty_list._head is None
    empty_list.append('x')
    assert empty_list._head._data == 'x'


def test_append_successful_to_full(small_list):
    '''
    appending when list has nodes, adds as tail
    '''
    assert small_list.read_off() == [1, 2, 3, 4]
    small_list.append('x')
    assert small_list.read_off() == [1, 2, 3, 4, 'x']


def test_prepend_successful_to_empty(empty_list):
    '''
    prepending when list is empty, adds as head
    '''
    assert empty_list._head is None
    empty_list.prepend('x')
    assert empty_list._head._data == 'x'


def test_prepend_successful_to_full(small_list):
    '''
    prepending when list has nodes, adds as head
    '''
    assert small_list.read_off() == [1, 2, 3, 4]
    small_list.prepend('x')
    assert small_list.read_off() == ['x', 1, 2, 3, 4]


def test_length_of_list_increases_on_append(empty_list):
    '''
    length attribute incriments on append
    '''
    assert len(empty_list) == 0
    empty_list.append('x')
    assert len(empty_list) == 1


def test_length_of_list_increases_on_prepend(empty_list):
    '''
    length attribute incriments on prepend
    '''
    assert len(empty_list) == 0
    empty_list.prepend('x')
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    '''
    checks list for requested value, true if present
    '''
    actual = small_list.includes(4)
    assert actual is True
    assert small_list.includes(4) is True


def test_includes_returns_false_if_not_exists(small_list):
    '''
    checks list for requested value, false if not present
    '''
    actual = small_list.includes('American soverignty')
    assert actual is False
    assert small_list.includes('American soverignty') is False
