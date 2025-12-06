def create_int_matrix(lines):
    m = []
    for l in lines:
        m.append([int(x) for x in l])
    return m


def is_visible(matrix, x, y):
    tree = matrix[y][x]
    return (all(other_tree < tree for other_tree in matrix[y][:x]) or
            all(other_tree < tree for other_tree in matrix[y][x+1:]) or
            all(matrix[i][x] < tree for i in range(0, y)) or
            all(matrix[i][x] < tree for i in range(y+1, len(matrix))))


def count_visible_trees(matrix):
    visible = (len(matrix[0])*2) + ((len(matrix)-2)*2)
    for y, line in enumerate(matrix[1: -1], 1):
        for x, tree in enumerate(line[1: -1], 1):
            if is_visible(matrix, x, y):
                visible += 1
    return visible


with open('input.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]
    m = create_int_matrix(lines)
    for l in m:
        print(l)
    print(count_visible_trees(m))
