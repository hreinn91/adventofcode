from src.Tile import *
from src.Image import *

test_image_file = 'src/resources/test1'
test_image = Image(test_image_file)


def test_print_image():
    print('\n')
    test_image.print_tile_grid()
    print('\n')
    test_image.print_image()
    pass

