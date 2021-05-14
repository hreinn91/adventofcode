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
        self.image_size = int(sqrt(len(self.tiles_container)))
        self.tile_size = self.tiles_container[0].size
        self.pixle_size = self.image_size * self.tile_size

    def get_tile(self, tile_id):
        for tile in self.tiles_container:
            if tile.id == tile_id:
                return tile
        raise ValueError('Invalid tile_id - Id not in tiles_container')

    def validate_image(self):
        pass

    def print_tile_grid(self):
        for row in range(0, self.image_size):
            im_row_string = ''
            for col in range(0, self.image_size):
                im_row_string += str(self.tile_ids[col + row * col]) + ' '
            print(im_row_string)

    def print_image(self):
        tiles = [self.get_tile(tile_id) for tile_id in self.tile_ids]
        for im_row in range(0, self.image_size):
            tiles_row = tiles[im_row * self.image_size: im_row * self.image_size + self.image_size]
            for tile_row in range(0, self.tile_size):
                image_row_str = ''
                for im_col in range(0, self.image_size):
                    tile = tiles_row[im_col]
                    image_row_str += tile.rows[tile_row]
                print(image_row_str)

    def make_tile_grid(self):
        tile_grid = []
        for tile_row in range(0, self.image_size):
            row_of_tiles = self.tiles_container[
                           self.image_size * tile_row: self.image_size + self.image_size * tile_row]
            tile_grid.append(row_of_tiles)
        return tile_grid
