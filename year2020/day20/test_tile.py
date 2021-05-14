from src.Tile import *
from src.Image import *

top_boarder = '..##.#..#.'
bottom_boarder = '..###..###'
left_boarder = '.#####..#.'
right_boarder = '...#.##..#'


def test_print_tile():
    tiles = get_tiles_from_input_file('src/resources/tile_2311')
    tile_2311 = tiles[0]
    assert tile_2311.id == 2311
    tile_2311.print_tile()
    assert tile_2311.boarder_left == left_boarder
    assert tile_2311.boarder_right == right_boarder
    assert tile_2311.boarder_top == top_boarder
    assert tile_2311.boarder_bottom == bottom_boarder


def test_flip_tile():
    tiles = get_tiles_from_input_file('src/resources/tile_2311')
    tile_2311 = tiles[0]
    tile_2311.print_tile()
    tile_2311.flip()
    tile_2311.print_tile()
    assert tile_2311.boarder_left == right_boarder
    assert tile_2311.boarder_right == left_boarder
    assert tile_2311.boarder_top == '.#..#.##..'
    assert tile_2311.boarder_bottom == '###..###..'


def test_rotate_tile():
    tiles = get_tiles_from_input_file('src/resources/tile_2311')
    tile_2311 = tiles[0]
    tile_2311.print_tile()
    tile_2311.rotate()
    tile_2311.print_tile()
    assert tile_2311.boarder_right == top_boarder
    assert tile_2311.boarder_bottom == right_boarder[::-1]
    assert tile_2311.boarder_left == bottom_boarder
    assert tile_2311.boarder_top == left_boarder[::-1]
