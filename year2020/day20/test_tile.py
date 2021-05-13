from src.Tile import *
from src.Image import *



def test_print_tile():
    tiles = get_tiles_from_input_file('src/resources/tile_2311')
    tile_2311 = tiles[0]
    assert tile_2311.id == 2311
    tile_2311.print_tile()


