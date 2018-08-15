from array_binary_search import binary_search
import pytest


def test_binary_search_exists():
    assert binary_search


def test_single_index():
    expected = 2
    actual = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    assert expected == actual


def test_all_index():
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    actual = []
    for i in range(1, 10):
        actual.append(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], i))
    assert expected == actual


def val_not_indexed():
    expected = -1
    actual = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    assert expected == actual


def test_argument_must_be_valid_list():
    with pytest.raises(TypeError):
        binary_search(1)
