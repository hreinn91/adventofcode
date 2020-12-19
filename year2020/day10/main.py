def part1(input_file):
    adapters = open(input_file, 'r').read().split('\n')
    adapters = list(map(int, adapters))
    # Add charginoutlet to list of adapters
    adapters.append(0)
    adapters.sort()

    low_difference = 0
    # Device has always a difference of 3 to highest adapter
    high_difference = 1

    for i in range(0, len(adapters) - 1):
        jolt_diff = adapters[i + 1] - adapters[i]
        if jolt_diff == 3:
            high_difference = high_difference + 1
        elif jolt_diff == 1:
            low_difference = low_difference + 1

    # print('Low difference: ' + str(low_difference))
    # print('High difference: ' + str(high_difference))
    return low_difference * high_difference


def get_permutation_map(suffizient_size):
    per_map = {1: 1}
    for i in range(2, 20):
        per_map[i] = per_map[i - 1] + i - 2
    return per_map


def part2(input_file):
    # Note no adapter diff of 2 was found in input
    adapters = open(input_file, 'r').read().split('\n')
    adapters = list(map(int, adapters))
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1]+3)
    permutations = 1

    per_map = get_permutation_map(30)

    # Count number of neighboring adapters with diff 1
    diff_1_count = 1
    for i in range(1, len(adapters)):
        current = adapters[i]
        previous = adapters[i-1]
        adapter_diff = adapters[i] - adapters[i - 1]
        if adapter_diff == 1:
            diff_1_count += 1
        elif adapter_diff == 3:
            permutations *= per_map[diff_1_count]
            diff_1_count = 1
        else:
            raise ValueError('Faulty data. Alla adapters should have 1 or 3 diff')
    return permutations


def main():
    low_high_difference_product = part1('input')
    print('Low high difference product: ' + str(low_high_difference_product))
    permutations = part2('input')
    print('You can connect your ridiculous adapters in this many different ways')
    print('>>>>>>>>>>>>>  ' + str(permutations))
    pass


if __name__ == '__main__':
    main()
