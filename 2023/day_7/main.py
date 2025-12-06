def create_dir_tree(lines, dir):
    while len(lines) != 0:
        line = lines[0]  # get line for calculation
        lines = lines[1:]  # remove line

        if line == '$ cd ..':
            break

        elif line.startswith('$ cd '):
            line = line.replace('$ cd ', '')
            if line not in dir:
                dir[line] = {}
            lines = create_dir_tree(lines, dir[line])

        elif line[0].isdigit():
            parts = line.split(' ')
            dir[parts[1]] = parts[0]

        elif line.startswith('dir '):
            parts = line.split(' ')
            dir[parts[1]] = {}
    return lines


def print_dir(root, indent):
    for k in root:
        if type(root[k]) is dict:
            print('  '*indent + f'- {k} (dir)')
            print_dir(root[k], indent+1)
        else:
            print('  '*indent + f'- {k} (file, size={root[k]})')


def calculate_dir_size(directory, result):
    size = 0
    for k in directory:
        if type(directory[k]) is dict:
            calculated_size = calculate_dir_size(directory[k], result)
            result.append((k, calculated_size))
            size += calculated_size
        else:
            size += int(directory[k])
    return size


with open('input.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]
    root = {'/': {}}
    create_dir_tree(lines, root)
    sizes = []
    calculate_dir_size(root, sizes)

    sizes.sort(reverse=True, key=lambda x: x[1])
    currently_used = 70000000 - int(sizes[0][1])
    needed_free_space = 30000000 - currently_used
    print(needed_free_space)

    print(
        f'dir to delete = {[x for x in sizes if (int(x[1]) >= needed_free_space)][-1]}')

    # for name, size in sizes:
    #     if size >
