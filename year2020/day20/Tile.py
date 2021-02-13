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
