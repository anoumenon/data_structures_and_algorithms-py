import pytest
from random import randint
from .selection import selection_sort


@pytest.fixture()
def shuffle_list():
    """generage shuffles list
    """
    ls = []
    for i in range(10):
        ls.append(randint(0, 10))
    return ls


@pytest.fixture()
def sorted_list(shuffle_list):
    """sort generated shuffled list
    """
    return selection_sort(shuffle_list)


def test_sort():
    """basic sort of unordered list
    """
    assert [1, 2, 3] == selection_sort([3, 2, 1])


def test_shuffle_list_is(shuffle_list):
    """endogenous test instantiation
    """
    assert shuffle_list


def test_already_sorted():
    """check passing of already sorted list
    """
    assert [1, 2, 3] == selection_sort([1, 2, 3])


def test_fixture_sort(shuffle_list, sorted_list):
    """sorting of unordered
    """
    assert sorted_list == selection_sort(shuffle_list)
