from itertools import groupby


def chunk(lines, n):
    for i in range(0, len(lines), n+1):
        yield lines[i:i + n].strip()


def parse_containers(lines):
    stacks = [list(chunk(l, 3)) for l in lines[:-1]]
    stacks.reverse()
    result = [list() for i in range(0, len(stacks[0]))]
    for s in stacks:
        for i, e in enumerate(s):
            if e:
                result[i].append(e)
    return result


def parse_commands(commands):
    parts = [c.split(' ') for c in commands]
    return [(int(p[1]), int(p[3])-1, int(p[5])-1) for p in parts]


def execute_commands(containers, commands):
    for rep, src, dst in commands:
        print(f'{src} -> {dst} for {rep}')
        tmp = []
        for i in range(0, rep):
            tmp.append(containers[src][-1])
            containers[src].pop()
        tmp.reverse()
        for c in tmp:
            containers[dst].append(c)
        tmp.clear()
    return containers


with open('input.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]
    groups = [list(group) for line, group in groupby(lines, bool) if line]
    containers = parse_containers(groups[0])
    commands = parse_commands(groups[1])
    containers_after = execute_commands(containers, commands)
    for c in containers_after:
        print(c[-1].strip('[]'), end='')
    print()
