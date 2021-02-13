numeral_map = {1: 'I',
               5: 'V',
               10: 'X',
               # 50: 'L',
               # 100: 'C',
               # 500: 'D',
               # 1000: 'M'
               }

mappable_number = sorted(numeral_map.keys(), reverse=True)


def convert_numeral_simple(number):
    if number == 0:
        return ''

    converted_number = ''
    for key in mappable_number:
        while number >= key:
            converted_number = converted_number + numeral_map[key]
            number = number - key

    return converted_number


def convert_odd_numbers(number):
    if number == key - 1:
        return converted_number + 'I' + convert_numeral(key)


def main():
    pass
