# Bellman–Ford algorithm implementation

This is a part of the project for Graphs Theory.

[![wakatime](https://wakatime.com/badge/github/sokoloowski/BellmanFord.svg)](https://wakatime.com/badge/github/sokoloowski/BellmanFord)
[![python](https://img.shields.io/badge/language-python-%23306998)](https://www.python.org/)

## Input

Script reads data from path specified as command line argument. Any text file will be accepted, but only specific JSON format will be interpreted correctly. Correct input data is a list of three lists:

- list of `n` vertices (should be integers from `0` to `n-1`),
- list of edges (in format `start, end, weight`),
- list of start and end  of route.

Example input file can be found in [this JSON file](examples/algo.json).

## Output

Script prints only necessary information - it's just one line.

## Usage

```
PS D:\BellmanFord> python .\main.py .\examples\algo.json
Total minimal cost of route from 0 to 3 equals to 4
```
