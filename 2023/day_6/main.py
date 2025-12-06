from collections import Counter


def find_marker(msg, length):
    parts = [msg[i:i+length] for i in range(0, len(msg) - length-1)]
    for i, part in enumerate(parts):
        if Counter(part).most_common()[0][1] == 1:
            return (part, i+length)


with open('input.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]
    for l in lines:
        print(find_marker(l, 4))
    for l in lines:
        print(find_marker(l, 14))
