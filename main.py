import sys
import json
from algo.BellmanFord import BellmanFord

if len(sys.argv) == 1:
    print("No file specified!")
    sys.exit()

filename = sys.argv[1]
f = open(filename)
edges = json.loads(f.read())

try:
    distance = BellmanFord(edges)
    print(f"Total minimal cost of route from {edges[-1][0]} to {edges[-1][1]} equals to {distance}")
except AssertionError:
    print("Incorrect input data! Cannot execute algorithm!")
except IndexError:
    print("Incorrect input data format!")
finally:
    sys.exit()
