from queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def tripple_queue():
    return Queue([1, 2, 3])


def test_queue_exists():
    """
    Check queue import
    """
    assert empty_queue


def test_queue_enqueues_iterable(tripple_queue):
    """
    assert that the queue can be instantiated with multiple nodes
    """
    assert len(tripple_queue) == 3


def test_queue_enqueues_single(tripple_queue):
    """
    assert that the queue will enqueue a single node
    """
    assert len(tripple_queue) == 3
    tripple_queue.enqueue('a')
    assert len(tripple_queue) == 4


def test_queue_dequeues_single(tripple_queue):
    """
    assert that the queue will dequeue a node
    """
    assert len(tripple_queue) == 3
    tripple_queue.dequeue()
    assert len(tripple_queue) == 2
