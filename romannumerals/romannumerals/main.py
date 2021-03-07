from math import pow

numeral_map = {1: 'I',
               5: 'V',
               10: 'X',
               50: 'L',
               100: 'C',
               500: 'D',
               1000: 'M'
               }

mappable_number = sorted(numeral_map.keys(), reverse=True)


def is_number_mapped(number):
    return number in mappable_number


def by_power_of_ten(number):
    parsed_numbers = []
    i = 0
    for c in sorted(str(number), reverse=True):
        parsed_numbers.append(int(c) * int(pow(10, i)))
        i += 1
    parsed_numbers.reverse()
    return parsed_numbers



def convert_numeral(number):
    if number <= 0:
        return ''

    if is_number_mapped(number):
        return numeral_map[number]

    for key in mappable_number:
        if number >= key:
            return convert_numeral(key) + convert_numeral(number - key)
        elif is_number_mapped(key - number):
            return convert_numeral(key - number) + convert_numeral(key)



if __name__ == '__main__':
    for char in 'abc':
        print(char)