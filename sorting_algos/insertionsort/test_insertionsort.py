import pytest
from .insertionsort import insertion_sort


@pytest.fixture()
def alist():
    return [54, 26, 93, 17, 77, 31, 44, 55, 20]


def test_insertion_sort():
    """
    """
    assert insertion_sort(alist()) == [17, 20, 26, 31, 44, 54, 55, 77, 93]
