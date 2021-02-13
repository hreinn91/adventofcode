from .Tile import Tile

class Image:
    def __init__(self, input_file):
        self.tiles = read_tiles_from_input_file(input_file)

    def assemble_image(self):
        pass


def get_tile_from_raw_string(raw_string):
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


def read_tiles_from_input_file(input_file):
    raw_tile = open(input_file, 'r').read().split('Tile ')[1:]
    tiles = list(map(get_tile_from_raw_string, raw_tile))
    return tiles
