# # # #  #
# 'pppp' #
# 'pppp' #
# 'pppp' #
# 'pppp' #
# # # #  #

# This represents one Tile
# With 4 rows of 4 pixels
# Every Tile is assumed to be quadratic


class Tile:
    def __init__(self, tile_id, rows):
        self.id = tile_id
        self.size = len(rows[0])
        self.rows = rows
        self.boarder_top = ''
        self.boarder_bottom = ''
        self.boarder_left = ''
        self.boarder_right = ''
        self.set_boarders()

    def set_boarders(self):
        self.boarder_top = self.rows[0]
        self.boarder_bottom = self.rows[-1]
        self.boarder_left = ''
        self.boarder_right = ''
        for row in self.rows:
            self.boarder_left += row[0]
            self.boarder_right += row[-1]

    def print_tile(self):
        print('\n')
        for row in self.rows:
            print(row)

    def flip(self):
        self.rows = [row[::-1] for row in self.rows]
        self.set_boarders()

    def rotate(self):
        rotated_rows = ['' for row in self.rows]
        for row in range(0, self.size):
            for col in range(0, self.size):
                pixel = self.rows[row][col]
                rotated_rows[col] = pixel+rotated_rows[col]
        self.rows = rotated_rows
        self.set_boarders()


def get_tiles_from_input_file(input_file):
    raw_tile_string = open(input_file, 'r').read().split('Tile ')[1:]
    tiles = list(map(string_to_tile, raw_tile_string))
    return tiles


def string_to_tile(raw_string):
    raw_string_split = raw_string.split(':')
    tile_id = int(raw_string_split[0])
    raw_string_split = raw_string_split[1].split('\n')

    if len(raw_string_split) == 11:
        raw_string_split = raw_string_split[1:]
    elif len(raw_string_split) == 13:
        raw_string_split = raw_string_split[1:-2]
    else:
        raise RuntimeError(' Wrong size raw input')

    return Tile(tile_id, raw_string_split)
