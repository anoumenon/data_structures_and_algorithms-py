from fifo_animal_shelter import Shelter
import pytest


@pytest.fixture
def empty_shelter():
    return Shelter()


def test_shelter_exists():
    """
    Check shelter import
    """
    assert empty_shelter

# def test_queue_enqueues_iterable(tripple_queue):
#     """
#     assert that the queue can be instantiated with multiple nodes
#     """
#     assert len(tripple_queue) == 3


# def test_queue_enqueues_single(tripple_queue):
#     """
#     assert that the queue will enqueue a single node
#     """
#     assert len(tripple_queue) == 3
#     tripple_queue.enqueue('a')
#     assert len(tripple_queue) == 4


# def test_queue_dequeues_single(tripple_queue):
#     """
#     assert that the queue will dequeue a node
#     """
#     assert len(tripple_queue) == 3
#     tripple_queue.dequeue()
#     assert len(tripple_queue) == 2
