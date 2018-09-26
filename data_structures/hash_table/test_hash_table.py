import pytest
from .hash_table import HashTable


@pytest.fixture()
def empty_table():
    t = HashTable()
    return t


def test_empty_table(empty_table):
    assert empty_table


def test_hash_one(empty_table):
    empty_table.put('key', 'value')
    assert empty_table.buckets is None

