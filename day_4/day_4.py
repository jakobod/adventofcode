import argparse
import time


def print_matrix(matrix):
    for l in matrix:
        for c in l:
            print(c, end='')
        print()
    print()


def parse_matrix(lines):
    return [list(line) for line in lines]


def remove_marked(matrix, to_remove):
    for x, y in to_remove:
        matrix[y][x] = 'x'
    return matrix


def check_surrounding(matrix, x, y):
    if matrix[y][x] != '@':
        return False

    symbols = []
    for y_off in [-1, 0, +1]:
        for x_off in [-1, 0, +1]:
            if ((y_off != 0) or (x_off != 0)) and (0 <= (y + y_off) < len(matrix)) and (0 <= x+x_off < len(matrix[y+y_off])):
                symbol = matrix[y + y_off][x+x_off]
                # print(f"found {symbol} at {y+y_off}, {x+x_off}")
                symbols.append(symbol)
    # print(f"{y},{x}: {symbols}")
    return symbols.count('@') < 4


def parse_input_first(lines):
    matrix = parse_matrix(lines)
    x = 0
    y = 0
    count = 0
    to_remove = []

    while True:
        new_count = 0
        print_matrix(matrix)

        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if check_surrounding(matrix, x, y):
                    new_count += 1
                    to_remove.append((x, y))
        matrix = remove_marked(matrix, to_remove)
        if new_count != 0:
            count += new_count
        else:
            print(f"count={count}")
            break


def parse_input_second(lines):
    pass


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--mode', default="1")
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [line.strip() for line in input]

    if args.mode == "1":
        parse_input_first(lines)
    if args.mode == "2":
        parse_input_second(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
