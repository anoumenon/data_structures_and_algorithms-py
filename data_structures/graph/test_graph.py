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


@pytest.fixture()
def bi_directional():
    """Set up a graph for traversal.
    """
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'D': 10},
        'B': {'A': 10, 'C': 10, 'D': 10},
        'C': {'B': 10, 'G': 10},
        'D': {'A': 10, 'B': 10, 'E': 10, 'H': 10, 'F': 10},
        'E': {'D': 10},
        'F': {'D': 10, 'H': 10},
        'G': {'C': 10},
        'H': {'D': 10, 'F': 10},
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


@pytest.fixture()
def flight_graph():
    """Set up a graph for traversal.
    """
    g = Graph()
    g.graph = {
        'Pandora': {'Arendelle': 150,},
        'Arendelle': {'Pandora': 150, 'Metroville': 82, 'Monstropolis': 105},
        'Metroville': {'Narnia': 37, 'Arendelle': 82, 'Monstropolis': 105, 'Naboo': 26},
        'Monstropolis': {'Arendelle': 42, 'Metroville': 105, 'Naboo': 73},
        'Naboo': {'Monstropolis': 73, 'Metroville': 26, 'Narnia': 250},
        'Narnia': {'Metroville': 37, 'Naboo': 250},
        'Single': {}
    }
    return g


def test_get_edges(flight_graph):
    """get edges method operational
    """
    assert flight_graph.get_edges(['Pandora', 'Arendelle', 'Pandora'])


def test_get_edge_val_round_trip(flight_graph):
    """gathers value total of round trip
    """
    assert flight_graph.get_edges([
        'Pandora', 'Arendelle', 'Pandora']) == [True, 300]


def test_get_edge_val(flight_graph):
    """gather value of trip
    """
    assert flight_graph.get_edges([
        'Pandora', 'Arendelle', 'Metroville']) == [True, 232]


def test_absent_path(flight_graph):
    """attempts absent path, returns false and 0
    """
    assert flight_graph.get_edges([
        'Arendelle', 'Monstropolis', 'Wonderland']) == [False, 0]


def test_instance_is_graph(bi_directional):
    """graph is graph.
    """
    assert isinstance(bi_directional, Graph)


def test_depth_first_method_avalible(bi_directional):
    """attempts absent path, returns false and 0
    """
    assert bi_directional.depth_first


def test_depth_first_correct_traversal(bi_directional):
    """given input, check correct ordered output
    """
    assert bi_directional.depth_first('A') == [
        'A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']


def test_absent_vert(bi_directional):
    """given a vert not included in the method, return false
    """
    assert bi_directional.depth_first(
        "IT'S B A N A N A S") is False


# removed for built in handling, kept for posterity.

# def test_vertex_does_not_exist(bi_directional):
#     """given a vert not included in the method
#     """
#     with pytest.raises(KeyError):
#         assert bi_directional.depth_first('K')


