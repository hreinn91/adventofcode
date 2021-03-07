from src.Tile import *
from src.Image import *

test_image_path = 'src/test1'

def test_print_image():
    image = get_test_image()
    pass



def get_test_image():
    return Image(test_image_path)
