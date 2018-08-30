from .multi_bracket_validation import multi_bracket_validation
# import pytest


def test_multi_bracket_validation_exists():
    """
    Check stack import
    """
    assert multi_bracket_validation


def test_single_pair():
    """
    str
    """
    check = multi_bracket_validation('()')
    assert check is True


def test_dynamic_pair():
    """
    assert that the stack can be instantiated with nodes
    """
    check = multi_bracket_validation('[({}{})]')
    assert check is True


def test_complex_pair():
    """
    assert that the stack can be instantiated with nodes
    """
    check = multi_bracket_validation('{[][][{()()()}][({}{})]}')
    assert check is True


def test_null_in():
    """
    assert that the stack can be instantiated with nodes
    """
    check = multi_bracket_validation(None)
    assert check is False


def test_narwhall():
    """
    assert that the stack can be instantiated with nodes
    """
    check = multi_bracket_validation('narwhall')
    assert check is True
