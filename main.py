from json.decoder import JSONDecodeError
from algo.AlgorithmExceptions import AlgorithmException, DataFormatException, InputDataException, MissingRouteException
import sys
import json
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
    print(f"Total minimal cost of route from {edges[-1][0]} to {edges[-1][1]} equals to {distance}")
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
