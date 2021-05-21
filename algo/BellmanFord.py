from math import inf
from typing import Tuple


def BellmanFord(vertices: list, edges: list, source: int) -> Tuple[list, list]:

    # This implementation takes in a graph, represented as
    # lists of vertices (represented as integers [0...n-1]) and edges,
    # and fills two arrays (distance and predecessor) holding
    # the shortest path from the source to each vertex

    # Step 1: initialize graph
    distance = [
        inf for n in vertices
    ]  # Initialize the distance to all vertices to infinity
    predecessor = [None for n in vertices]  # And having a null predecessor

    distance[source] = 0  # The distance from the source to itself is, of course, zero

    # Step 2: relax edges repeatedly
    for v in vertices:
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # Step 3: check for negative-weight cycles
    for u, v, w in edges:
        assert distance[u] + w >= distance[v], "Graph contains a negative-weight cycle"

    return (distance, predecessor)
