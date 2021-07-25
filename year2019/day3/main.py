def get_input(filename):
    raw_split = open(filename, 'r').read().split('\n')
    wire_1 = raw_split[0].split(',')
    wire_2 = raw_split[1].split(',')
    return wire_1, wire_2


def norm_l1(x, y):
    dx = abs(x)
    dy = abs(y)
    return dx + dy


class Wires:
    def __init__(self, filename):
        self.wire_1, self.wire_2 = get_input(filename)
        self.grid = self.get_grid(self.wire_1, self.wire_2)
        self.intersections = self.get_intersections(self.grid)
        self.manhattan_distance = self.get_shortest_intersection(self.intersections)

    @staticmethod
    def get_grid(wire_1, wire_2):
        grid = {}
        Wires.populate_grid(grid, wire_1)
        Wires.populate_grid(grid, wire_2)
        return grid

    @staticmethod
    def populate_grid(grid, instructions):
        x = 0
        y = 0
        grid[(x, y)] = 'o'
        for instruction in instructions:
            direction, length = Wires.parse(instruction)
            value = '.'
            for i in range(0, length):
                if direction == 'R':
                    x = x + 1
                    value = '-'
                elif direction == 'L':
                    x = x - 1
                    value = '-'
                elif direction == 'U':
                    y = y + 1
                    value = '|'
                elif direction == 'D':
                    y = y - 1
                    value = '|'
                else:
                    raise ValueError('Unknown direction : ' + str(direction))

                if (x, y) in grid:
                    grid[(x, y)] = 'X'
                elif i == length - 1:
                    grid[(x, y)] = '+'
                else:
                    grid[(x, y)] = value
        pass

    @staticmethod
    def parse(instruction):
        return instruction[0], int(instruction[1])

    def print_instructions(self):
        print(self.wire_1)
        print(self.wire_2)

    @staticmethod
    def get_grid_dimensions(grid):
        x_size = 0
        y_size = 0
        for key in grid.keys():
            if x_size < key[0]:
                x_size = key[0]
            if y_size < key[1]:
                y_size = key[1]

        return x_size, y_size

    def print_grid(self, grid):
        x_size, y_size = self.get_grid_dimensions(grid)
        for y in range(-100, y_size + 2):
            row = []
            for x in range(-100, x_size + 2):
                if (x, y) in grid:
                    row.insert(x, grid[(x, y)])
                else:
                    row.insert(x, '.')
            print(''.join(row))
        pass

    @staticmethod
    def get_intersections(grid):
        intersections = {}
        for key, value in grid.items():
            if value == 'X':
                intersections[key] = value
        return intersections

    @staticmethod
    def get_shortest_intersection(intersections):
        if len(intersections) == 0:
            raise RuntimeError('Get distance error')

        first_key = list(intersections.keys())[0]
        manhattan_distance = norm_l1(first_key[0], first_key[1])
        for key in intersections.keys():
            temp_distance = norm_l1(key[0], key[1])
            if temp_distance < manhattan_distance:
                manhattan_distance = temp_distance
        return manhattan_distance


if __name__ == '__main__':
    wires = Wires('input1.txt')
    wires.print_grid(wires.grid)
    print(wires.manhattan_distance)

    print("Done")
