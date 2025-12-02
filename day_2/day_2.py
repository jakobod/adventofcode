import argparse
import time
from itertools import groupby


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def is_invalid_id(num):
  if num >= 11:
    strnum = str(num)
    partlen = int(len(strnum)/2)
    while partlen > 0:
      if int(len(strnum)) % partlen == 0:
        parts = [strnum[i:i+partlen] for i in range(0, len(strnum), partlen)]
        if all_equal(parts):
          return True
      partlen -= 1
  return False


def parse_input_second(ranges):
  sum = 0
  for r in ranges:
    begin, end = [int(x) for x in r.split('-')]
    # print(f"begin = {begin}, end = {end}")
    for num in range(begin, end+1):
      if is_invalid_id(num):
        sum += num
  print(f"Sum of all invalid numbers = {sum}")


def parse_input_simple(ranges):
  sum = 0
  for r in ranges:
    begin, end = [int(x) for x in r.split('-')]
    for num in range(begin, end+1):
      if num >= 11:
        strnum = str(num)
        halflen = int(len(strnum)/2)      
        parts = [strnum[i:i+halflen] for i in range(0, len(strnum), halflen)]
        if all_equal(parts):
          sum += num
  print(f"Sum of all invalid numbers = {sum}")


def main():
  parser = argparse.ArgumentParser(prog='adventofcode day_2')
  parser.add_argument('input_file')
  parser.add_argument('--mode', default="1")
  args = parser.parse_args()

  print(f"Parsing {args.input_file}:")
  with open(args.input_file, "r") as input:
    lines = [l.strip() for l in input]
    ranges = lines[0].split(',')

    if args.mode == "1":
      parse_input_simple(ranges)
    if args.mode == "2":
      parse_input_second(ranges)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
