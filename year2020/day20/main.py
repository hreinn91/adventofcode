def get_tile_from_raw_string(raw_string):
    raw_string_split = raw_string.split(':')
    tile_id = int(raw_string_split[0])
    raw_string_split = raw_string_split[1].split('\n')

    # Clean out unnecessary characters from the raw input
    # The last tile in the list has different set of unnecessary characters.
    if len(raw_string_split) == 11:
        raw_string_split = raw_string_split[1:]
    elif len(raw_string_split) == 13:
        raw_string_split = raw_string_split[1:-2]
    else:
        raise RuntimeError(' Wrong size raw input')

    return Tile(tile_id, raw_string_split)


# The [1:] throws away empty char at the start of raw input
# When splitting on 'Tile '
def read_tiles_from_input_file(input_file):
    # Split the raw input into segments of raw input
    raw_tile = open(input_file, 'r').read().split('Tile ')[1:]

    # Now map the segment of raw input to actual ImageSegmetns with correct id
    tiles = list(map(get_tile_from_raw_string, raw_tile))
    return tiles


class Tile:
    def __init__(self, tile_id, segment):
        self.id = tile_id
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

    def set_neighbour_top(self):


class Image:
    def __init__(self, input_file):
        self.tiles = read_tiles_from_input_file(input_file)

    def assemble_image(self):
        pass


# Execute part1
def part1():
    full_image = Image('test1')
    tiles = full_image.tiles
    tile1 = tiles[0]
    tile2 = tiles[1]
    tile1.neighbour_top = tile2

    return


def main():
    part1()
    return


if __name__ == '__main__':
    main()
