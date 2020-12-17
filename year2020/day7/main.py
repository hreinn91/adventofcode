def get_color(rule):
    return rule[0] + ' ' + rule[1]


def add_permissive_color(rules, permissive_colors):
    current_size = len(permissive_colors)
    for rule in rules:
        rule = rule.split(' ')
        bag_color = get_color(rule)
        can_contain = ' '.join(rule[2:])
        for color in list(permissive_colors):
            if color in can_contain:
                permissive_colors.add(bag_color)
    if len(permissive_colors) > current_size:
        add_permissive_color(rules, permissive_colors)
    return


def part1():
    print(' - Part 1: Different colors of bags that can fit shiny gold -  ')
    rules = open('./input', 'r').read().split('\n')
    my_color = 'shiny gold'
    permissive_colors = {my_color}
    add_permissive_color(rules, permissive_colors)
    print('Number: ' + str(len(permissive_colors) - 1))
    print('Number: ' + str(permissive_colors))


def parse_rule(rule):
    rule = rule.split(' ')
    key = rule[0] + ' ' + rule[1]
    can_contain = ' '.join(rule[4:]).split(', ')
    return key, can_contain


def parse_capacity(capacity):
    capacity = capacity.split(' ')
    return int(capacity[0]), capacity[1] + ' ' + capacity[2]


def fetch_capacity(target, rules):
    for rule in rules:
        key, capacity = parse_rule(rule)
        if key == target:
            return capacity

    raise ResourceWarning('target not in rules: ' + str(target))


def target_bag_capacity(target, rules):
    capacity_list = fetch_capacity(target, rules)
    if 'no other bags' in str(capacity_list):
        return 0
    target_count = 0
    for capacity in capacity_list:
        count, bag = parse_capacity(capacity)
        target_count = target_count + count + count * target_bag_capacity(bag, rules)
    return target_count


def part2():
    print(' - Part 2: How many bags can good old shiny bag fit -  ')
    rules = open('./input2', 'r').read().split('\n')
    target = 'shiny gold'
    count = target_bag_capacity(target, rules)
    print(target + ' can hold this number of bags  > > > >  ' + str(count))


def main():
    part1()
    print('\n\n')
    part2()

    return


if __name__ == '__main__':
    main()
