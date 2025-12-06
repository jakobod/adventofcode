def to_priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27


def duplicate(p):
    for c in p[0]:
        if c in p[1]:
            return c


def find_badge(g):
    for c in g[0]:
        if c in g[1] and c in g[2]:
            return c


def chunk(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    duplicates = [to_priority(duplicate(p)) for p in [
        [l[0:len(l)//2], l[len(l)//2:len(l)]] for l in lines]]
    print(sum(duplicates))

    chunked = chunk(lines, 3)
    badges = [to_priority(find_badge(p)) for p in chunked]
    print(sum(badges))
