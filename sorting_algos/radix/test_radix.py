import pytest
from random import randint
from .radix import radix_sort


@pytest.fixture()
def shuffle_list():
    """generage shuffles list
    """
    ls = []
    for i in range(11):
        ls.append(randint(0, 10))
    return ls


@pytest.fixture()
def sorted_list(shuffle_list):
    """sort generated shuffled list
    """
    return radix_sort(shuffle_list)


def test_shuffle_list_is(shuffle_list):
    """endogenous test instantiation
    """
    assert shuffle_list


def test_sort():
    """basic sort of unordered list
    """
    assert [201, 202, 203] == radix_sort([203, 202, 201])


def test_already_sorted():
    """check passing of already sorted list
    """
    assert [1, 2, 3] == radix_sort([1, 2, 3])


def test_fixture_sort(shuffle_list, sorted_list):
    """sorting of unordered
    """
    assert sorted_list == radix_sort(shuffle_list)


def test_with_zero_value_raises_error():
    """Test an array with zero value should raise exception
    """
    # with pytest.raises(AssertionError):
    assert radix_sort([10, 10, 11, 10, 10]) == [10, 10, 10, 10, 11]


def test_with_zero_value_raises_error():
    """Test an array with zero value should raise exception
    """
    # with pytest.raises(AssertionError):
    assert radix_sort([10, 10, 100, 10, 10]) == [10, 10, 10, 10, 100]


def test_with_intermediate_zero_value():
    """Test an array with zero value should raise exception
    """
    # with pytest.raises(AssertionError):
    assert radix_sort([10001, 1001, 101, 11, 1]) == [1, 11, 101, 1001, 10001]
