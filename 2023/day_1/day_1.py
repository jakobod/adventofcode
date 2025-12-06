from itertools import groupby

# def create_elves(input):
#   with open(input, 'r') as f:
#     return [sum([int(s) for s in vals]) for vals in [list(group) for k, group in groupby([x.strip() for x in f.readlines()], bool) if k]]

def create_elves(input):
  with open(input, 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    grouped = [list(group) for k, group in groupby(lines, bool) if k]
    return [sum([int(s) for s in vals]) for vals in grouped]

elves = create_elves('input.txt')
elves.sort(reverse=True)
print(f'elf with the most things = {elves[0]}')
print(f'top three elves with the most things = {elves[0]+elves[1]+elves[2]}')
