class Tile:
    def __init__(self, tile_id, segment):
        self.id = tile_id
        self.segment_length = len(segment[0])
        self.segment = segment
        self.boarder_top = segment[0]
        self.boarder_bottom = segment[-1]
        self.boarder_left = ""
        self.boarder_right = ""
        for row in segment:
            self.boarder_left = self.boarder_left + row[0]
            self.boarder_right = self.boarder_right + row[-1]
        self.neighbour_top = None
        self.neighbour_bottom = None
        self.neighbour_left = None
        self.neighbour_right = None

    def print_tile(self):
        for row in self.segment:
            print(row)


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
