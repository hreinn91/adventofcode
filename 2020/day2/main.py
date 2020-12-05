import os

def get_input(filename):
    res = []
    with open(filename) as fp:
        for line in fp:
            res.append(line[:-1])

    return res


def parse_line(line):
    entry = line.split()
    bound = list(map(int, entry[0].split('-')))
    letter = entry[1][0]
    password = entry[2]
    return bound, letter, password


    return

def is_valid(bound, letter, password):
    occurance = 0
    for let in password:
        if let == letter:
            occurance = occurance + 1

    if occurance >= bound[0] and occurance <= bound[1]:
        return 1

    return 0

def is_valid_new_rules(bound, letter, password):
    rule1 = bound[0] - 1
    rule2 = bound[1] - 1
    if letter == password[rule1] and letter != password[rule2]:
        return 1
    if letter != password[rule1] and letter == password[rule2]:
        return 1

    return 0


def count_valid(filename):
    entries = get_input(filename)
    count = 0
    count_new_rules = 0
    for entry in entries:
        bound, letter, password = parse_line(entry)
        count = count + is_valid(bound, letter, password)
        count_new_rules = count_new_rules + is_valid_new_rules(bound, letter,
                password)

    return count, count_new_rules


def main():
    print(list(count_valid('./input')))
    return


if __name__ == '__main__':
    main()



