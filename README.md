# Bellman–Ford algorithm implementation

This is a part of the project for Graphs Theory.

[![wakatime](https://wakatime.com/badge/github/sokoloowski/BellmanFord.svg)](https://wakatime.com/badge/github/sokoloowski/BellmanFord)
[![python](https://img.shields.io/badge/language-python-%23306998)](https://www.python.org/)

## Input

Script reads data from path specified as command line argument. Any text file will be accepted, but only specific JSON format will be interpreted correctly. Correct input data is a list of edge with specified weight. Additionaly, last element of the list must contain begin and end of route:

```json
[
    ["start_of_edge_1", "end_of_edge_1", "weight_1"],
    ["start_of_edge_2", "end_of_edge_2", "weight_2"],
    ["start_of_edge_...", "end_of_edge_...", "weight_..."],
    ["start_of_edge_n-1", "end_of_edge_n-1", "weight_n-1"],
    ["start_of_edge_n", "end_of_edge_n", "weight_n"],
    ["start"]
]
```

All values should be numbers. Example input file can be found in [this JSON file](examples/algo.json). Last element of JSON array must be an one-element array.

## Output

Script prints distance to every vertex. In case there is no connection between start and n-th vertex, script prints information about no route.

If an error occurs, information about the cause is displayed.

## Usage

```
PS D:\BellmanFord> python .\main.py .\examples\algo.json
Minimal distance to 0 vertex: 0
Minimal distance to 1 vertex: 1
Minimal distance to 2 vertex: 2
Minimal distance to 3 vertex: 4
Minimal distance to 4 vertex: 3
```
