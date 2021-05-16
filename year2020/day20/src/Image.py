from .Tile import Tile, get_tiles_from_input_file
from math import sqrt


# # # # # # #
# ppp # ppp #
# ppp # ppp #
# ppp # ppp #
# # # # # # #
# ppp # ppp #
# ppp # ppp #
# ppp # ppp #
# # # # # # #

# This represents one Image of 4 tiles
# The image_size = 2 and tile_size 3
# Each tile consists of 3*3 pixels


class Image:
    def __init__(self, input_file):
        self.tiles_container = get_tiles_from_input_file(input_file)
        self.tile_ids = [tile.id for tile in self.tiles_container]
        self.size = int(sqrt(len(self.tiles_container)))
        self.tile_size = self.tiles_container[0].size

    def get_tile(self, tile_id):
        for tile in self.tiles_container:
            if tile.id == tile_id:
                return tile
        raise ValueError('Invalid tile_id - Id not in tiles_container')

    def print_tile_grid(self):
        for row in range(0, self.size):
            im_row_string = ''
            for col in range(0, self.size):
                im_row_string += str(self.tile_ids[col + row * self.size]) + ' '
            print(im_row_string)

    def print(self):
        tiles = [self.get_tile(tile_id) for tile_id in self.tile_ids]
        for im_row in range(0, self.size):
            tiles_row = tiles[im_row * self.size: im_row * self.size + self.size]
            for tile_row in range(0, self.tile_size):
                image_row_str = ''
                for im_col in range(0, self.size):
                    tile = tiles_row[im_col]
                    image_row_str += tile.rows[tile_row]
                print(image_row_str)

    def assemble(self):
        for i in range(0, self.size * self.size):
            tile = self.tiles_container[i]
            for j in range(i + 1, self.size * self.size):
                tile_to_compare = self.tiles_container[j]

