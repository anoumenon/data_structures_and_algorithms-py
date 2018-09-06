from queue import Queue
import pytest


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


def test_queue_class_exists():
    """Test import
    """
    assert Queue


def test_queue_instantiation(empty_queue):
    """Test instantiation
    """
    assert isinstance(empty_queue, Queue)


def test_insertion_increases_length(empty_queue):
    """Check for length attribute increase on appendage
    """
    assert len(empty_queue) == 0
    empty_queue.enqueue(315)
    assert len(empty_queue) == 1


def test_default_value_of_front(empty_queue):
    """Test empty front is None
    """
    assert empty_queue.front is None
