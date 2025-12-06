import argparse
import time


def parse_input_second(l1, l2):
    res = 0
    for first in l1:
        mult = 0
        for second in l2:
            if second == first:
                mult += 1
        res += (first*mult)
    print(res)


def parse_input_first(l1, l2):
    l1.sort()
    l2.sort()
    res = 0

    for first, second in zip(l1, l2):
        res += abs(first-second)
    print(res)


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--mode', default="1")
    args = parser.parse_args()

    print(f"Parsing {args.input_file}:")
    with open(args.input_file, "r") as input:
        lines = [l.strip() for l in input]

    l1 = []
    l2 = []
    for l in lines:
        parts = l.split('   ')
        l1.append(int(parts[0]))
        l2.append(int(parts[1]))

    if args.mode == "1":
        parse_input_first(l1, l2)
    if args.mode == "2":
        parse_input_second(l1, l2)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
