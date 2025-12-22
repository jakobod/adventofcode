#!/usr/bin/env python3

import argparse
import time
from collections import defaultdict
from itertools import combinations
from itertools import groupby


def calc_area(p1, p2):
    x_dist = abs(p1[0] - p2[0])+1
    y_dist = abs(p1[1] - p2[1])+1
    return x_dist * y_dist


def part_one(lines):
    points = [(int(x), int(y)) for line in lines for x, y in [line.split(',')]]
    max_area_pair = max((pair for pair in combinations(points, 2)),
                        key=lambda pair: calc_area(pair[0], pair[1]))
    print(f"{max_area_pair}: {calc_area(max_area_pair[0], max_area_pair[1])}")


def calculate_limits(points):
    """
    Given a list of (x, y) points representing a polygon (in order),
    connect them with straight lines (horizontal or vertical) and
    return the min and max x for each y row.
    """

    # Collect all points on the polygon edges
    edge_points = defaultdict(set)

    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]  # wrap to first point
        x1, y1 = p1
        x2, y2 = p2

        if y1 == y2:  # horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                edge_points[y1].add(x)
        elif x1 == x2:  # vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                edge_points[y].add(x1)

    # Build limits: for each row, get (min_x, max_x)
    limits = {}
    for y in sorted(edge_points.keys()):
        xs = edge_points[y]
        limits[y] = (min(xs), max(xs))

    return limits


def is_in_limits(point_pair, limits):
    p1, p2 = point_pair
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    for y in range(min_y, max_y+1):
        begin, end = limits[y]
        if (begin > min_x) or (end < max_x):
            return False
    return True


def part_two(lines):
    points = [(int(x), int(y)) for line in lines for x, y in [line.split(',')]]
    # print(points)
    limits = calculate_limits(points)

    # for limit in limits:
    #     print(f"{limit}: {limits[limit]}")

    max_area_pair = max((pair for pair in combinations(points, 2)
                         if is_in_limits(pair, limits)),
                        key=lambda pair: calc_area(pair[0], pair[1]))

    print(f"{max_area_pair}: {calc_area(max_area_pair[0], max_area_pair[1])}")


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
    stop = time.perf_counter()
    print(f"Runtime: {stop - start:.4f} seconds")
