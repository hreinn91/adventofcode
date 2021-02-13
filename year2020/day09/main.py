def is_weakness(number, preambles):
    for i in range(0, len(preambles)):
        for j in range(i + 1, len(preambles)):
            if number == preambles[i] + preambles[j]:
                return False
    return True


def fetch_weakness(preamble, xmas_data):
    for i in range(preamble, len(xmas_data)):
        if is_weakness(xmas_data[i], xmas_data[i - preamble:i]):
            return i, xmas_data[i]
    raise RuntimeError('You are a failure Hreinn.')


def part1(preamble, input_file):
    xmas_data = open(input_file, 'r').read().split('\n')
    xmas_data = list(map(int, xmas_data))
    index, weakness = fetch_weakness(preamble, xmas_data)
    print('Weakness is: ' + str(weakness))
    print('At index: ' + str(index))
    return xmas_data, weakness


def break_up_xmas(xmas, limit):
    xmas_break = []
    holder = []
    for i in xmas:
        if i >= limit:
            if holder:
                xmas_break.append(holder)
            holder = []
        else:
            holder.append(i)
    return xmas_break


def fetch_contueue_set(xmas, limit):
    for i in range(0, len(xmas)):
        sol = [xmas[i]]
        sum = xmas[i]
        for j in range(i + 1, len(xmas)):
            sum = sum + xmas[j]
            sol.append(xmas[j])
            if sum == limit and len(sol) > 1:
                return sol
            elif sum >= limit:
                break
    raise RuntimeError('I could not find the solution sorry.')


def part2(xmas, weakness):
    xmas_breakup = break_up_xmas(xmas, weakness)
    for breakup in xmas_breakup:
        try:
            return fetch_contueue_set(breakup, weakness)
        except RuntimeError:
            print()


def main():
    xmas_data, weakness = part1(25, 'input')
    sol_set = part2(xmas_data, weakness)
    sol_set.sort()
    print(sol_set)
    print(sol_set[0] + sol_set[-1])
    return


if __name__ == '__main__':
    main()
