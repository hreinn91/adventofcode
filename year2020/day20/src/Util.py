from .Tile import Tile

def get_tiles_from_input_file(input_file):
    raw_tile_string = open(input_file, 'r').read().split('Tile ')[1:]
    tiles = list(map(string_to_tile, raw_tile_string))
    return {tile.id: tile for tile in tiles}


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
