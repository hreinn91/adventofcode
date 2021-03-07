from .Tile import Tile, get_tiles_from_input_file
from math import sqrt


class Image:
    def __init__(self, input_file):
        self.tiles = get_tiles_from_input_file(input_file)
        self.tile_length = int(sqrt(len(self.tiles)))
        self.pixle_length = self.tile_length * self.tiles[0].segment_length
        self.tile_grid = self.make_tile_grid()

    def make_tile_grid(self):
        tile_grid = []
        for i in range(0, self.tile_length):
            for j in range(0, self.tile_length):
                tile_grid.append(self.tiles[j + self.tile_length * i])
        return tile_grid

    def validate_image(self):
        pass

    def print_image(self):
        pass
