import sys
import json
from algo.BellmanFord import BellmanFord

if len(sys.argv) == 1:
    print("No file specified!")
    sys.exit()

filename = sys.argv[1]
f = open(filename)
edges = json.loads(f.read())

distance, predecessor = BellmanFord(edges)
print(f"Total minimal cost of route from {ends[0]} to {ends[1]} equals to {distance[ends[1]]}")
