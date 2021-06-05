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
        self.next_top = None
        self.next_bottom = None
        self.next_left = None
        self.next_right = None

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
                rotated_rows[col] = pixel + rotated_rows[col]
        self.rows = rotated_rows
        self.set_boarders()

    # A free tile is not matched with other tiles
    def is_free(self):
        return self.next_top is None and \
               self.next_bottom is None and \
               self.next_left is None and \
               self.next_right is None

    def match(self, tile, flipped=False):
        match_success = self.match_boarders(tile)
        if not match_success and self.is_free():
            print('Rotating')
            self.rotate()
            match_success = self.match_boarders(tile)
        if not match_success and self.is_free():
            print('Rotating')
            self.rotate()
            match_success = self.match_boarders(tile)
        if not match_success and self.is_free():
            print('Rotating')
            self.rotate()
            match_success = self.match_boarders(tile)
        if not match_success and self.is_free() and not flipped:
            print('Rotating and Flipping')
            self.rotate()
            self.flip()
            match_success = self.match(tile, True)
        return match_success

    def match_boarders(self, tile):
        if self.next_top is None and tile.next_bottom is None and self.boarder_top == tile.boarder_bottom:
            self.next_top = tile.id
            tile.next_bottom = self.id
            return True
        if self.next_bottom is None and tile.next_top is None and self.boarder_bottom == tile.boarder_top:
            self.next_bottom = tile.id
            tile.next_top = self.id
            return True
        if self.next_left is None and tile.next_right is None and self.boarder_left == tile.boarder_right:
            self.next_left = tile.id
            tile.next_right = self.id
            return True
        if self.next_right is None and tile.next_left is None and self.boarder_right == tile.boarder_left:
            self.next_right = tile.id
            tile.next_left = self.id
            return True
        return False

