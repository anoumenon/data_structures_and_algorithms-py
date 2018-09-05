from .tqueue import Queue
import pytest
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def empty_queue():
    """Reusable testing fixture of an empty queue
    """
    return Queue()


@pytest.fixture
def small_queue():
    """Reusable testing fixture for short queue
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


@contextmanager
def captured_output():
    '''Helper function for testing stdout'''
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_queue_class_exists():
    """Test that the queue module was properly imported
    """
    assert Queue


def test_can_instantiate_empty_queue(empty_queue):
    """Test that test fixture is of the expected class
    """
    assert isinstance(empty_queue, Queue)


def test_insertion_of_value_increases_length(empty_queue):
    """Test that the queue's length increases after enqueuing a new value
    """
    assert len(empty_queue) == 0
    empty_queue.enqueue(100)
    assert len(empty_queue) == 1


def test_default_value_of_front(empty_queue):
    """Test that the front property is none prior to enqueuing
    """
    assert empty_queue.front is None
