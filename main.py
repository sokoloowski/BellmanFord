import sys
import json
from algo.BellmanFord import BellmanFord

if len(sys.argv) == 1:
    print("No file specified!")
    sys.exit()

filename = sys.argv[1]
f = open(filename)
vertices, edges, ends = json.loads(f.read())

distance, predecessor = BellmanFord(vertices, edges, ends[0])
print(f"Total minimal cost of route from {ends[0]} to {ends[1]} equals to {distance[ends[1]]}")
