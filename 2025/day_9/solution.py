#!/usr/bin/python3

import argparse
import time
import math
from collections import defaultdict
from itertools import combinations


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def calc_area(self, other):
        """
        Euclidean distance to another Point
        """
        x_dist = abs(self.x - other.x)+1
        y_dist = abs(self.y - other.y)+1
        return x_dist * y_dist

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return (
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y)
        )

    def __hash__(self):
        # Round coordinates to a fixed precision (e.g., 9 decimal places)
        return hash((
            round(self.x, 9),
            round(self.y, 9)
        ))

    def __repr__(self):
        return f"({self.x}, {self.y})"


def part_one(lines):
    points = [Point(x, y) for line in lines for x, y in [line.split(',')]]
    max_area_pair = max((pair for pair in combinations(points, 2)),
                        key=lambda pair: pair[0].calc_area(pair[1]))
    print(f"{max_area_pair}: {max_area_pair[0].calc_area(max_area_pair[1])}")


def part_two(lines):
    pass


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--part', default="1")
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [line.strip() for line in input]

    if args.part == "1":
        part_one(lines)
    if args.part == "2":
        part_two(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
