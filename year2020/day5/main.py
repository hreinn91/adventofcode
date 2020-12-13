from math import ceil

test_passes = {
    'BFFFBBFRRR': [70, 7, 567],
    'FFFBBBFRRR': [14, 7, 119],
    'BBFFBBFRLL': [102, 4, 820]
}


def get_id(boardpass):
    if len(boardpass) != 10:
        raise ValueError('Not correct number of characters in : ' + str(boardpass))

    row = get_row(boardpass[0:7])
    col = get_col(boardpass[7:10])
    return get_id_from_rc(row, col)


def get_row(row, lower=0, upper=127):
    # Could also be that lower == upper
    if len(row) == 1:
        if row in ['F', 'L']:
            return int(lower)
        if row in ['B', 'R']:
            return int(upper)

    half = (upper - lower) / 2
    if row[0] in ['F', 'L']:
        return get_row(row[1:], lower, int(upper - half))
    elif row[0] in ['B', 'R']:
        return get_row(row[1:], ceil(lower + half), upper)
    else:
        raise ValueError('Wrong character in row : ' + str(row))


def get_col(col, lower=0, upper=7):
    return get_row(col, lower, upper)


def get_id_from_rc(row, col):
    return row * 8 + col


def test():
    for key in test_passes.keys():
        row = get_row(key[:7])
        col = get_col(key[7:10])
        idd = get_id(key)
        print('test done')


def main():
    boardpasses = open('input', 'r').read().split('\n')[:-1]
    ids = list(map(get_id, boardpasses))
    ids.sort()

    for i in range(0, len(ids)-1):
        if ids[i] + 1 != ids[i + 1]:
            print("Your seat is: " + str(ids[i] + 1))

    print("Highest seat on the boadingpass: " + str(ids[-1]))
    return


if __name__ == '__main__':
    main()
