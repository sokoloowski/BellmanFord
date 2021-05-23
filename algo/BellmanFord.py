from math import inf


def BellmanFord(edges: list) -> int:

    """
    This implementation takes in a graph, represented as
    lists of vertices (represented as integers [0...n-1]) and edges,
    and fills two arrays (distance and predecessor) holding
    the shortest path from the start to each vertex

    Returns `Tuple` with `distance: list` and `predecessor: list`
    """

    # Step 1: initialize graph
    vertices = [edge[0] for edge in edges if len(edge) == 3]
    [vertices.append(edge[1]) for edge in edges if len(edge) == 3]
    vertices = list(dict.fromkeys(vertices))  # remove duplicates
    distance = [inf for n in vertices]
    predecessor = [None for n in vertices]
    start, destination = [edge for edge in edges if len(edge) == 2][0]

    distance[start] = 0  # The distance from the start to itself is, of course, zero

    # Step 2: relax edges repeatedly
    for vertex in vertices:
        try:
            for u, v, w in edges[:-1]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
        except IndexError:
            print("Incorrect input format!")

    # Step 3: check for negative-weight cycles
    for vertex in vertices:
        try:
            for u, v, w in edges[:-1]:
                assert (
                    distance[u] + w >= distance[v]
                ), "Graph contains a negative-weight cycle"
        except IndexError:
            print("Incorrect input format!")

    return distance[destination]
