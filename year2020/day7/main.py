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

# Correct answer: 287
def main():
    rules = open('./input', 'r').read().split('\n')
    my_color = 'shiny gold'
    permissive_colors = {my_color}
    add_permissive_color(rules, permissive_colors)


    print('Number: ' + str(len(permissive_colors) - 1))
    print('Number: ' + str(permissive_colors))
    return


if __name__ == '__main__':
    main()
