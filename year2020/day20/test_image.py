from src.Tile import *
from src.Image import *

test_image_path = 'src/resources/test1'


def test_print_image():
    print('\n')
    image = get_test_image()
    image.print_image()
    pass


def get_test_image():
    return Image(test_image_path)
