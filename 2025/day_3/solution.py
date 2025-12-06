import argparse
import time


def remove_at(string, index):
    return string[:index] + string[index + 1:]


def remove_and_maximize(val):
    current_max = 0
    for i in range(0, len(val)):
        new_num = remove_at(val, i)
        if int(current_max) < int(new_num):
            current_max = new_num
    return current_max


def find_biggest_joltage(line, num_numbers):
    current_num = line[len(line)-num_numbers:]
    line = line[:len(line)-num_numbers]
    line = line[::-1]

    while line:
        if int(line[0]) >= int(current_num[0]):
            current_num = remove_and_maximize(line[0] + current_num)
        line = line[1:]
    return int(current_num)


def parse_input_first(lines):
    joltage = 0
    for l in lines:
        joltage += find_biggest_joltage(l, 2)
    print(f"Total Joltage = {joltage}")


def parse_input_second(lines):
    joltage = 0
    for l in lines:
        joltage += find_biggest_joltage(l, 12)
    print(f"Total Joltage = {joltage}")


def main():
    parser = argparse.ArgumentParser(prog='adventofcode day_2')
    parser.add_argument('input_file')
    parser.add_argument('--mode', default="1")
    args = parser.parse_args()

    with open(args.input_file, "r") as input:
        lines = [l.strip() for l in input]

        if args.mode == "1":
            parse_input_first(lines)
        if args.mode == "2":
            parse_input_second(lines)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.4f} seconds")
