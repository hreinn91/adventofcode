numeral_map = {1: 'I',
               5: 'V',
               10: 'X',
               50: 'L',
               100: 'C',
               500: 'D',
               1000: 'M'
               }

mappable_number = sorted(numeral_map.keys(), reverse=True)


def get_digits_by_power(number):
    digits = []
    number = str(number)
    i = 1
    for c in number:
        digits.append(int(c + '0' * (len(number) - i)))
        i = i + 1
    return digits


def is_number_in_map(number):
    return number in mappable_number


def convert_numeral(number):
    if number <= 0:
        return ''

    if is_number_in_map(number):
        return numeral_map[number]

    numeral = ''
    for digit in get_digits_by_power(number):
        numeral = numeral + convert_numeral_from_map(digit)

    return numeral


def convert_numeral_from_map(number):
    if is_number_in_map(number):
        return numeral_map[number]

    for key in mappable_number:
        if number > key:
            return convert_numeral(key) + convert_numeral(number - key)
        elif is_number_in_map(key - number):
            return convert_numeral(key - number) + convert_numeral(key)


if __name__ == '__main__':
    main()
