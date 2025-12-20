import argparse
import time
import math
from collections import defaultdict
from itertools import combinations
from tqdm import tqdm


class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def distance_to(self, other):
        """
        Euclidean distance to another Point
        """
        return math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2 +
            (other.z - self.z) ** 2
        )

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return (
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y) and
            math.isclose(self.z, other.z)
        )

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        if not math.isclose(self.x, other.x):
            return self.x < other.x
        if not math.isclose(self.y, other.y):
            return self.y < other.y
        return self.z < other.z

    def __hash__(self):
        # Round coordinates to a fixed precision (e.g., 9 decimal places)
        return hash((
            round(self.x, 9),
            round(self.y, 9),
            round(self.z, 9)
        ))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


def add_to_circuits(vertex, circuits):
    new_circuit = set(vertex)
    for i in range(len(circuits) - 1, -1, -1):
        circuit = circuits[i]
        if any(p in circuit for p in vertex):
            new_circuit.update(circuit)
            del circuits[i]
    circuits.append(new_circuit)


def part_one(lines, num_connections):
    points = [Point(x, y, z) for x, y, z in [line.split(',')
                                             for line in lines]]
    circuits = [set([p]) for p in points]
    distances = [(vertex[0].distance_to(vertex[1]), vertex)
                 for vertex in combinations(points, 2)]
    distances.sort(key=lambda pair: pair[0])

    for _, vertex in distances[:num_connections]:
        add_to_circuits(vertex, circuits)

    circuits.sort(key=len, reverse=True)
    res = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    print(res)


def part_two(lines):
    points = [Point(x, y, z) for x, y, z in [line.split(',')
                                             for line in lines]]

    circuits = [set([p]) for p in points]

    distances = [(vertex[0].distance_to(vertex[1]), vertex)
                 for vertex in combinations(points, 2)]
    distances.sort(key=lambda pair: pair[0])

    for _, vertex in distances:
        add_to_circuits(vertex, circuits)

        if len(circuits) == 1:
            print(vertex)
            print(vertex[0].x*vertex[1].x)
            break


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--part', default="1")
    parser.add_argument('--num-connections', default=1000)
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [line.strip() for line in input]

    if args.part == "1":
        part_one(lines, args.num_connections)
    if args.part == "2":
        part_two(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
