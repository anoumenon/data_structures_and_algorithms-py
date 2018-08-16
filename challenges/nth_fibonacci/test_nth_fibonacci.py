from nth_fibonacci import nth_fibonacci
# import pytest


def test_nth_fibonacci_exists():
    assert nth_fibonacci


def test_index():
    expected = 5
    actual = nth_fibonacci(5)
    assert expected == actual


def test_zero():
    expected = 0
    actual = nth_fibonacci(0)
    assert expected == actual


def test_two():
    expected = 1
    actual = nth_fibonacci(2)
    assert expected == actual


def test_not_int():
    expected = -1
    actual = nth_fibonacci('a')
    assert expected == actual
