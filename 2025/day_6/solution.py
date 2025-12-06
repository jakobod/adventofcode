import argparse
import time
from collections import defaultdict


def calculate_problem(operands, operator):
    expression = operator.join(operands)
    return eval(expression)


def part_one(lines):
    problems = defaultdict(list)

    for line in lines:
        for i, part in enumerate(line.split()):
            problems[i].append(part)

    res = 0
    for i in problems:
        problem = problems[i]
        operator = problem[len(problem)-1]
        problem.pop()
        res += calculate_problem(problem, operator)
    print(f"Result of expressions = {res}")


def part_two(lines):

    problems = defaultdict(list)
    operators = []
    current_problem_index = 0
    for i in range(0, len(lines[0])):
        operand = ''
        operator = ''
        for line in lines:
            if line[i].isdigit():
                operand += line[i]
            if line[i] in ['+', '-', '*', '/']:
                operator = line[i]
                operators.append(operator)

        if operand:
            problems[current_problem_index].append(operand)

        if not operand and not operator:
            current_problem_index += 1

    total = 0
    for i in problems:
        operands = problems[i]
        operator = operators[i]
        res = calculate_problem(operands, operator)
        print(f"operands={operands}, operator={operator}, res = {res}")
        total += res
    print(f"total={total}")


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
