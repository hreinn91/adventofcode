import copy


def parse_instructions(instructions, current=0, accumilator=0, history=[]):
    if current in history:
        return accumilator
    elif current >= len(instructions):
        print('Accumilatior after correction: ' + str(accumilator))
        raise RuntimeError('We break the recursion here.')

    history.append(current)
    inst = instructions[current]
    if inst[0] == 'nop':
        return parse_instructions(instructions, current + 1, accumilator, history)
    elif inst[0] == 'acc':
        accumilator = accumilator + int(inst[1])
        return parse_instructions(instructions, current + 1, accumilator, history)
    elif inst[0] == 'jmp':
        current = current + int(inst[1])
        return parse_instructions(instructions, current, accumilator, history)
    else:
        raise ValueError('Invalid instruction')


def part1():
    instructions = open('input', 'r').read().split('\n')
    instructions = list(map(lambda x: x.split(' '), instructions))
    history = []
    accumilator = parse_instructions(instructions, history=history)
    print('Accumilator after loop: ' + str(accumilator))
    return instructions, history


def part2(instructions, history):
    nop_instructions = set()
    jmp_instructions = set()
    for inst in history:
        if instructions[inst][0] == 'nop':
            nop_instructions.add(inst)
        elif instructions[inst][0] == 'jmp':
            jmp_instructions.add(inst)

    for nop_index in nop_instructions:
        improved_instructions = copy.deepcopy(instructions)
        improved_instructions[nop_index][0] = 'jmp'
        try:
            parse_instructions(improved_instructions, history=[])
        except RuntimeError:
            print('Instructions finished with exceptions correctly.')

    for jmp_index in jmp_instructions:
        improved_instructions = copy.deepcopy(instructions)
        improved_instructions[jmp_index][0] = 'nop'
        try:
            parse_instructions(improved_instructions, history=[])
        except RuntimeError:
            print('Instructions finished with exceptions correctly.')

    print('done')


def main():
    instrucions, history = part1()
    part2(instrucions, history)


if __name__ == '__main__':
    main()
