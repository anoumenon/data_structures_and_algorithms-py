from array_shift import insert_shift_array
import pytest


def test_insert_shift_array_exists():
    assert insert_shift_array


def test_list_gets_insert_even():
    expected = [1, 2, 'a', 3, 4]
    actual = insert_shift_array([1, 2, 3, 4], 'a')
    assert expected == actual


def test_list_gets_insert_odd():
    expected = [1, 2, 3, 'a', 4, 5]
    actual = insert_shift_array([1, 2, 3, 4, 5], 'a')
    assert expected == actual


def test_argument_must_be_valid_list():
    with pytest.raises(TypeError):
        insert_shift_array(1)
