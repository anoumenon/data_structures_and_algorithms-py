from .fifo_animal_shelter import Shelter
import pytest


@pytest.fixture
def empty_shelter():
    return Shelter()


@pytest.fixture
def bi_single_shelter():
    shelter = Shelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    return shelter


def test_shelter_import(empty_shelter):
    """
    Check shelter import
    """
    assert Shelter


def test_shelter_counts_dog(empty_shelter):
    """shelter class queues dog
    """
    empty_shelter.enqueue('dog')
    assert empty_shelter.count == 1


def test_shelter_counts_cat(empty_shelter):
    """shelter class queues cat
    """
    empty_shelter.enqueue('cat')
    assert empty_shelter.count == 1


def test_shelter_takes_dog(empty_shelter):
    """shelter class queues dog
    """
    empty_shelter.enqueue('dog')
    assert empty_shelter.dogs._front


def test_shelter_takes_cat(empty_shelter):
    """shelter class queues cat
    """
    empty_shelter.enqueue('cat')
    assert empty_shelter.cats._front


def test_shelter_dequeues_dog(bi_single_shelter):
    """adopt a dog
    """
    assert bi_single_shelter.dogs._front
    bi_single_shelter.dequeue('dog')
    assert bi_single_shelter.dogs._front is None


def test_shelter_dequeues_cat(bi_single_shelter):
    """adopt a cat
    """
    assert bi_single_shelter.cats._front
    bi_single_shelter.dequeue('cat')
    assert bi_single_shelter.cats._front is None


def test_shelter_dequeues_either_dog(empty_shelter):
    """either select takes lower tag
    """
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('cat')
    assert empty_shelter.cats._front
    assert empty_shelter.dogs._front
    empty_shelter.dequeue('either')
    assert empty_shelter.dogs._front is None
    assert empty_shelter.cats._front


def test_shelter_dequeues_either_cat(empty_shelter):
    """either select takes lower tag
    """
    empty_shelter.enqueue('cat')
    empty_shelter.enqueue('dog')
    assert empty_shelter.cats._front
    assert empty_shelter.dogs._front
    empty_shelter.dequeue('either')
    assert empty_shelter.dogs._front
    assert empty_shelter.cats._front is None


def test_empty_shelter_reject_service(empty_shelter):
    """trying to adopt from an empty shelter should return False
    """
    assert empty_shelter.dequeue('either') is False
    assert empty_shelter.dequeue('cat') is False
    assert empty_shelter.dequeue('dog') is False
