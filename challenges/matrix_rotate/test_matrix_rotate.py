from matrix_rotate import matrix_rotate
import pytest


def test_matrix_rotate_exists():
    assert matrix_rotate


def test_rotation():
    expected = [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
    actual = matrix_rotate([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    assert expected == actual


def test_argument_must_be_valid_matrix():
    with pytest.raises(TypeError):
        matrix_rotate({'A': 'a'})
