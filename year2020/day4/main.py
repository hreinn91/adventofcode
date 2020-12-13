import re
from sortedcontainers import SortedDict as sd

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_field = 'cid'


def main():
    passports_raw = open("./input", "r").read()[:-1].split('\n\n')
    passports = []
    valid_count = 0
    valid_count_permissive = 0
    valid_count_strict = 0
    number_of_passports = len(passports_raw)
    for raw in passports_raw:
        passport = get_passport_from_raw(raw)
        passports.append(passport)
        print_pssp(passport)
        valid_count = valid_count + is_valid(passport, valid_fields, optional_field)
        valid_count_permissive = valid_count_permissive + is_valid(passport, valid_fields)
        valid_count_strict = valid_count_strict + is_valid_strict(passport)

    print(" ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ")
    print(" > > > " + str(number_of_passports) + " : Number of passports.")
    print(" > > > " + str(valid_count) + " : Valid passports")
    print(" > > > " + str(valid_count_permissive) + " : Almost valid passports")
    print(" > > > " + str(valid_count_strict) + " : Very valid passports")
    print(" ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ")
    return


def get_passport_from_raw(raw):
    raw = re.split(' |\n|:', raw)
    dic = {}
    for i in range(0, len(raw), 2):
        dic[raw[i]] = raw[i + 1]
    return sd(dic)


def is_valid_strict(pssp):
    if is_valid(pssp, valid_fields) == 0:
        return 0

    if not is_valid_number(pssp['byr'], 1920, 2002):
        return 0
    if not is_valid_number(pssp['iyr'], 2010, 2020):
        return 0
    if not is_valid_number(pssp['eyr'], 2020, 2030):
        return 0

    hgt = pssp['hgt']
    metric = hgt[-2:]
    hgt = hgt[:-2]
    if metric == 'cm':
        if not is_valid_number(hgt, 150, 193):
            return 0
    elif metric == 'in':
        if not is_valid_number(hgt, 59, 76):
            return 0
    else:
        return 0

    hcl = pssp['hcl']
    if hcl[0] == '#':
        hcl = hcl[1:]
        if not len(hcl) == 6 or not is_valid_af09(hcl):
            return 0
    else:
        return 0

    ecl = pssp['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0

    pid = pssp['pid']
    if len(pid) != 9 or not pid.isnumeric():
        return 0

    return 1


def is_valid_af09(hcl):
    for c in hcl:
        if not c.isnumeric() and c not in ['a', 'b', 'c', 'd', 'e', 'f']:
            return False

    return True


def is_valid_number(numb, low_bound, high_bound):
    return numb.isnumeric() and low_bound <= int(numb) <= high_bound


def is_valid(pssp, fields, optional=None):
    for field in fields:
        if field not in pssp:
            return 0
    if optional is not None and optional not in pssp:
        return 0
    return 1


def print_pssp(pssp):
    print("1------------")
    for key in pssp:
        print(key + ":" + pssp[key])
    print("2------------\n")
    return


if __name__ == '__main__':
    main()
