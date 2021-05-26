from json.decoder import JSONDecodeError
from algo.AlgorithmExceptions import AlgorithmException, DataFormatException, InputDataException, MissingRouteException
import sys
import json
from math import isinf
from algo.BellmanFord import BellmanFord

if len(sys.argv) == 1:
    print("No file specified!")
    sys.exit()

filename = sys.argv[1]
try:
    f = open(filename)
except FileNotFoundError:
    print(f"File {filename} not found!")
    sys.exit()

try:
    edges = json.loads(f.read())
except JSONDecodeError:
    print(f"Invalid format in JSON file: {filename}")
    sys.exit()

try:
    distance = BellmanFord(edges)
    for i, cost in enumerate(distance):
        if isinf(cost):
            print(f"\033[41mNo route to {i} vertex\033[0m")
        else:
            print(f"Minimal distance to {i} vertex: {cost}")
except InputDataException:
    print("Incorrect input data! Cannot execute algorithm!")
except DataFormatException:
    print("Incorrect input data format!")
except MissingRouteException:
    print(f"Cannot calculate route from {edges[-1][0]} to {edges[-1][1]} - no connection between vertices")
except AlgorithmException:
    print("An error occurred while the algorithm was running")
finally:
    sys.exit()
