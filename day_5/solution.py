import argparse
import time


def merge_ranges(ranges):
    # Sort by start value
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for begin, end in sorted_ranges[1:]:
        last_begin, last_end = merged[-1]
        # If current range overlaps or is adjacent to last range, merge them
        if begin <= last_end + 1:
            merged[-1] = (last_begin, max(last_end, end))
        else:
            merged.append((begin, end))

    return merged


def is_in_range(ingredient, ranges):
    for begin, end in ranges:
        if begin <= ingredient and ingredient <= end:
            print(f"{ingredient} is between ({begin}, {end})")
            return True
    return False


def parse_input_first(ranges, ingredients):
    num_fresh = 0
    for ingredient in ingredients:
        if is_in_range(ingredient, ranges):
            num_fresh += 1
    print(f"fresh = {num_fresh}")


def parse_input_second(ranges):
    ranges = merge_ranges(ranges)
    num_fresh_ids = 0
    for begin, end in ranges:
        num_fresh_ids += end-begin+1
    print(f'num_fresh_ids={num_fresh_ids}')


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--mode', default="1")
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [line.strip() for line in input]
    ranges = [(int(begin), int(end))
              for begin, end in [l.split('-') for l in lines if '-' in l]]
    ingredients = [int(l.strip()) for l in lines if l and '-' not in l]

    if args.mode == "1":
        parse_input_first(ranges, ingredients)
    if args.mode == "2":
        parse_input_second(ranges)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
