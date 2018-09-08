import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


def test_empty_graph_instance():
    assert graph_empty


def test_filled_graph_instance():
    assert graph_filled


def test_traversal_graph_instance():
    assert graph_filled_for_traversal


def test_add_vert(graph_empty):
    graph_empty.add_vert('A')
    assert graph_empty.graph['A'] == {}


def test_has_vert(graph_empty):
    graph_empty.add_vert('A')
    assert graph_empty.has_vert('A')


def test_has_vert_false(graph_empty):
    graph_empty.add_vert('A')
    assert graph_empty.has_vert('B') is False


def test_add_edge(graph_empty):
    graph_empty.add_vert('A')
    graph_empty.add_vert('B')
    graph_empty.add_edge('A', 'B', 315)
    assert graph_empty.graph['A']['B'] == 315


def test_get_neighbors(graph_empty):
    graph_empty.add_vert('A')
    graph_empty.add_edge('A', 'B', 3)
    graph_empty.add_edge('A', 'C', 1)
    graph_empty.add_edge('A', 'D', 5)
    assert graph_empty.get_neighbors('A') == {'B': 3, 'C': 1, 'D': 5}


def test_len_count(graph_empty):
    assert graph_empty.__len__() == 0
    graph_empty.add_vert('X')
    assert graph_empty.__len__() == 1
    graph_empty.add_vert('Y')
    assert graph_empty.__len__() == 2
    graph_empty.add_vert('Z')
    assert graph_empty.__len__() == 3
