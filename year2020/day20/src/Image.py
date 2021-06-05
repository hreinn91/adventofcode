from .Tile import Tile
from .Util import get_tiles_from_input_file
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
        # Improvement would be to put tiles in map rather than list!
        self.tiles_map = get_tiles_from_input_file(input_file)
        self.tile_ids = list(self.tiles_map.keys())
        self.tile_grid = []
        self.size = int(sqrt(len(self.tiles_map)))
        self.tile_size = next(iter(self.tiles_map.values())).size

    def print_tile_grid(self):
        for row in range(0, self.size):
            im_row_string = ''
            for col in range(0, self.size):
                im_row_string += str(self.tile_grid[col + row * self.size]) + ' '
            print(im_row_string)

    def print(self):
        tiles = [self.tiles_map[tile_id] for tile_id in self.tile_ids]
        for im_row in range(0, self.size):
            tiles_row = tiles[im_row * self.size: im_row * self.size + self.size]
            for tile_row in range(0, self.tile_size):
                image_row_str = ''
                for im_col in range(0, self.size):
                    tile = tiles_row[im_col]
                    image_row_str += tile.rows[tile_row]
                print(image_row_str)

    def assemble(self):
        number_of_tiles = len(self.tile_ids)
        for i in range(0, number_of_tiles):
            tile_id = self.tile_ids[i]
            tile = self.tiles_map[tile_id]
            for j in range(i + 1, number_of_tiles):
                tile_to_compare_id = self.tile_ids[j]
                tile_to_compare = self.tiles_map[tile_to_compare_id]
                tile.match(tile_to_compare)
        self.assemble_tile_grid()

    def assemble_tile_grid(self):
        top_left_corner = self.find_top_left_corner()
        self.append_to_grid(top_left_corner, top_left_corner)

    def find_top_left_corner(self):
        top_left_corner = None
        for id, tile in self.tiles_map.items():
            if not tile.is_free() and tile.next_top is None and tile.next_left is None:
                top_left_corner = tile
        if top_left_corner is None:
            raise RuntimeError('Assembly failed - Top left corner missing.')
        return top_left_corner

    def append_to_grid(self, start_of_row, current_tile):
        if current_tile is None:
            if start_of_row.next_bottom is None:
                return
            else:
                next_row = self.tiles_map[start_of_row.next_bottom]
                return self.append_to_grid(next_row, next_row)


        # Fix None problem
        self.tile_grid.append(current_tile.id)
        self.append_to_grid(start_of_row, self.tiles_map[current_tile.next_right])
