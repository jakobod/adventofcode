from timeit import timeit


def is_contained(p1, p2):
    return (int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1])) or (int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]))


def is_overlapping(p1, p2):
    return (int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[0])) or (int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[0]))


def run():
    with open('input.txt', 'r') as f:
        lines = [l.strip().split(',') for l in f.readlines()]
        parts = [[l[0].split('-'), l[1].split('-')] for l in lines]

        contained = 0
        overlapping = 0
        for p in parts:
            if is_contained(p[0], p[1]):
                contained += 1
            if is_overlapping(p[0], p[1]):
                overlapping += 1
        return contained, overlapping


print(timeit(run, number=100))
