from math import inf
from typing import Tuple, List
from .AlgorithmExceptions import AlgorithmException, InputDataException, DataFormatException, MissingRouteException


def BellmanFord(edges: list) -> Tuple[List[int], List[int]]:

    """
    This implementation takes in a graph, represented as lists of edges

    Returns `Tuple` cost of route and predecessor for each node
    """

    # Step 1: initialize graph
    try:
        vertices = [u for u, v, w in edges[:-1]]
        [vertices.append(v) for u, v, w in edges[:-1]]
    except ValueError:
        raise DataFormatException
    vertices = list(dict.fromkeys(vertices))  # remove duplicates
    distance = [inf for n in vertices]
    predecessor = [None for n in vertices]
    try:
        start = edges[-1][0]
    except ValueError:
        raise DataFormatException

    try:
        distance[start] = 0  # The distance from the start to itself is, of course, zero
    except TypeError:
        raise DataFormatException

    # Step 2: relax edges repeatedly
    for vertex in vertices:
        for u, v, w in edges[:-1]:
            try:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
            except IndexError:
                raise AlgorithmException

    # Step 3: check for negative-weight cycles
    for vertex in vertices:
        for u, v, w in edges[:-1]:
            if distance[u] + w < distance[v]:
                raise InputDataException

    return (distance, predecessor)
