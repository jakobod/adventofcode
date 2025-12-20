import argparse
import time


def part_one(lines):

    for line in lines:
        increasing = None
        parts = line.split()
        last = parts[0]

        for num in parts[1:]:
            diff = num - last
            last = num
            increasing2 = (diff >= 0)
            if increasing != None and increasing != increasing2:


def part_two(lines):
    pass


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--part', default="1")
    args = parser.parse_args()

    print(f"Parsing {args.input_file}:")
    with open(args.input_file, "r") as input:
        lines = [line.rstrip() for line in input]

    if args.part == "1":
        part_one(lines)
    if args.part == "2":
        part_two(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
