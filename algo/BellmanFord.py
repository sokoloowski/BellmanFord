from math import inf


def BellmanFord(edges: list) -> int:

    """
    This implementation takes in a graph, represented as lists of edges

    Returns `int` total cost of route
    """

    # Step 1: initialize graph
    vertices = [u for u, v, w in edges[:-1]]
    [vertices.append(v) for u, v, w in edges[:-1]]
    vertices = list(dict.fromkeys(vertices))  # remove duplicates
    distance = [inf for n in vertices]
    predecessor = [None for n in vertices]
    start, destination = edges[-1]

    distance[start] = 0  # The distance from the start to itself is, of course, zero

    # Step 2: relax edges repeatedly
    for vertex in vertices:
        for u, v, w in edges[:-1]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # Step 3: check for negative-weight cycles
    for vertex in vertices:
        for u, v, w in edges[:-1]:
            assert distance[u] + w >= distance[v], "Graph contains a negative-weight cycle"

    return distance[destination]
