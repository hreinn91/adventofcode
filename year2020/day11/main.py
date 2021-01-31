import copy


class Seats:

    def __init__(self, input_file):
        self.seats = open(input_file, 'r').read().split('\n')
        self.seats = list(map(list, self.seats))
        self.next_state = copy.deepcopy(self.seats)
        self.n_rows = len(self.seats)
        self.n_cols = len(self.seats[0])

    def get_seat(self, row, col):
        return self.seats[row][col]

    def is_seat(self, row, col):
        return self.seats[row][col] == 'L' or self.seats[row][col] == '#'

    def is_vacant_seat(self, row, col):
        return self.seats[row][col] == 'L'

    def is_occupied_seat(self, row, col):
        return self.seats[row][col] == '#'

    def count_occupied_seats(self):
        return str(self.seats).count('#')

    def get_seats_in_sight(self, row, col):
        # print("row: " + str(row) + " col: " + str(col))
        seats_in_sight = []
        for i in range(row - 1, -1, -1):
            if self.is_seat(i, col):
                seats_in_sight.append(self.get_seat(i, col))
                break
        for i in range(row + 1, self.n_rows):
            if self.is_seat(i, col):
                seats_in_sight.append(self.get_seat(i, col))
                break
        for j in range(col - 1, -1, -1):
            if self.is_seat(row, j):
                seats_in_sight.append(self.get_seat(row, j))
                break
        for j in range(col + 1, self.n_rows):
            if self.is_seat(row, j):
                seats_in_sight.append(self.get_seat(row, j))
                break
        # Second quadrant
        min_d = min(row, col)
        for d in range(1, min_d + 1):
            y_pos = row - d
            x_pos = col - d
            if self.is_seat(y_pos, x_pos):
                seats_in_sight.append(self.get_seat(y_pos, x_pos))
                break
        # First quadrant
        min_d = min(row, self.n_cols - col)
        for d in range(1, min_d + 1):
            y_pos = row - d
            x_pos = col + d
            if self.is_seat(y_pos, x_pos):
                seats_in_sight.append(self.get_seat(y_pos, x_pos))
                break
        # Third quadrant
        min_d = min(self.n_rows - row, col)
        for d in range(1, min_d + 1):
            y_pos = row + d
            x_pos = col - d
            if self.is_seat(y_pos, x_pos):
                seats_in_sight.append(self.get_seat(y_pos, x_pos))
                break
        # Fourth quadrant
        min_d = min(self.n_rows - row, self.n_cols - col)
        for d in range(1, min_d):
            y_pos = row + d
            x_pos = col + d
            if self.is_seat(y_pos, x_pos):
                seats_in_sight.append(self.get_seat(y_pos, x_pos))
                break

        return seats_in_sight

    def get_adjacent_seats(self, row, col):
        adjacent_seats = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.n_rows and 0 <= j < self.n_cols:
                    adjacent_seats.append(self.get_seat(i, j))
        self_seat = self.get_seat(row, col)
        adjacent_seats.remove(self_seat)
        return adjacent_seats

    def seat_state_iterate(self, row, col):
        adjacent_seats = self.get_adjacent_seats(row, col)
        if self.is_vacant_seat(row, col) and adjacent_seats.count('#') == 0:
            self.next_state[row][col] = '#'
        if self.is_occupied_seat(row, col) and adjacent_seats.count('#') >= 4:
            self.next_state[row][col] = 'L'

    def next_round(self):
        for i in range(0, len(self.seats)):
            for j in range(0, len(self.seats[0])):
                if self.is_seat(i, j):
                    self.seat_state_iterate(i, j)

        is_steady_state = self.seats == self.next_state
        self.seats = copy.deepcopy(self.next_state)
        return is_steady_state

    def seat_state_iterate_improved(self, row, col):
        seats_in_sight = self.get_seats_in_sight(row, col)
        if self.is_vacant_seat(row, col) and seats_in_sight.count('#') == 0:
            self.next_state[row][col] = '#'
        if self.is_occupied_seat(row, col) and seats_in_sight.count('#') >= 5:
            self.next_state[row][col] = 'L'

    def next_round_improved(self):
        for i in range(0, len(self.seats)):
            for j in range(0, len(self.seats[0])):
                if self.is_seat(i, j):
                    self.seat_state_iterate_improved(i, j)

        is_steady_state = self.seats == self.next_state
        self.seats = copy.deepcopy(self.next_state)
        return is_steady_state

    def print_state(self, round=''):
        print('> State ' + str(round) + ' <')
        for row in self.seats:
            print(''.join(row))
        print('----------\n')


def part1():
    seats = Seats('input')
    steady_state = False
    round = 0
    while not steady_state:
        # print(seats.count_occupied_seats())
        # seats.print_state(round)
        steady_state = seats.next_round()
        round += 1
    return seats.count_occupied_seats()


def part2(input_file):
    seats = Seats(input_file)
    steady_state = False
    round = 0
    seats.get_seats_in_sight(1, 8)
    # while not steady_state:
    #     seats.print_state(round)
    #     steady_state = seats.next_round_improved()
    #     round += 1
    return seats.count_occupied_seats()


def main():
    # occupied_count = part1()
    # print('Number of occupied seats in steady state: ' + str(occupied_count))
    occupied_count = part2('test3')
    print('Number of occupied seats in improved steady state: ' + str(occupied_count))

    return


if __name__ == '__main__':
    main()
