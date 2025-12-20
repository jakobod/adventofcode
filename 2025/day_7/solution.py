import argparse
import time
from collections import defaultdict


def find_start_index(line):
    return line.index('S')


def part_one(lines):
    num_splits = 0
    beams = set()
    beams.add(find_start_index(lines[0]))
    for line in lines[1:]:
        for index, char in enumerate(line):
            if char == '^' and index in beams:
                num_splits += 1
                beams.remove(index)
                beams.update([index-1, index+1])

    print(f'number of splits = {num_splits}')


def part_two(lines):
    current_beams = defaultdict(lambda: 0)
    current_beams[find_start_index(lines[0])] += 1
    for line in lines[1:]:
        future_beams = defaultdict(lambda: 0)
        for beam in current_beams:
            current_beamcount = current_beams[beam]
            char = line[beam]

            if char == '^':
                future_beams[beam-1] += current_beamcount
                future_beams[beam+1] += current_beamcount
            else:
                future_beams[beam] += current_beamcount

        current_beams = future_beams

    total_beams = 0
    for beam in current_beams:
        total_beams += current_beams[beam]
    print(f'number of beams = {total_beams}')


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--part', default="1")
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [line for line in input]

    if args.part == "1":
        part_one(lines)
    if args.part == "2":
        part_two(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
