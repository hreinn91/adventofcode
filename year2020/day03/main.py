

def get_input(filename):
    res = []
    with open(filename) as fp:
        for line in fp:
            res.append(line[:-1])
    return res


def count_trees(right, down, pos, path):
    if len(path) < down+1:
        return 0
    if pos+right >= len(path[0]):
        pos = pos - len(path[0])
    tree_count = count_trees(right, down, pos + right, path[down:])
    if path[down][pos+right] == '#':
        return 1 + tree_count
    return tree_count


def main():
    path = get_input('./input')
    res = [count_trees(1, 1, 0, path),
           count_trees(3, 1, 0, path),
           count_trees(5, 1, 0, path),
           count_trees(7, 1, 0, path),
           count_trees(1, 2, 0, path)]
    prod = 1
    for val in res:
        prod = prod * val
    print(res, prod)
    return


if __name__ == '__main__':
    main()

