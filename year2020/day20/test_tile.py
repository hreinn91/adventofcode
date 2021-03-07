from src.Tile import *
from src.Image import *



def test_print_tile():
    print('\n')
    tile = get_tile()
    tile.print_tile()


def get_tile():
    image = Image('src/test1')
    return image.tiles[0]
