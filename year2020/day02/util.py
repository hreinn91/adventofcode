import os


def get_input(filename):
    res = []
    with open(filename) as fp:
        for line in fp:
            res.append(int(line[:-1]))

    return res



