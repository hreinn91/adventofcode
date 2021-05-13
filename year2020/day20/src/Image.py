from .Tile import Tile, get_tiles_from_input_file
from math import sqrt


class Image:
    def __init__(self, input_file):
        self.tiles = get_tiles_from_input_file(input_file)
        self.tile_length = int(sqrt(len(self.tiles)))
        self.segment_length = self.tiles[0].size
        self.pixle_length = self.tile_length * self.segment_length
        self.tile_grid = self.make_tile_grid()

    def make_tile_grid(self):
        tile_grid = []
        for tile_row in range(0, self.tile_length):
            tile_grid.append(self.tiles[self.tile_length * tile_row: self.tile_length + self.tile_length * tile_row])
        return tile_grid

    def validate_image(self):
        pass

    def print_image(self):
        for row in range(0, self.tile_length):
            tile_columns = self.tile_grid[row]
            for segment_index in range(0, self.segment_length):
                for column in range(0, self.tile_length):
                    tile = tile_columns[column]
                    segment = tile.segment[segment_index]
                    print(segment)
                print('\n')
        pass
