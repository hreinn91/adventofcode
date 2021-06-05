from src.Tile import *
from src.Image import *


# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171


def test_assembe_1_2_image():
    image_1_2 = Image('src/resources/test1_2')
    image_1_2.assemble()
    image_1_2.print_tile_grid()
    assert image_1_2.tile_grid == [1951, 2311]


def test_assembe_1_3_image():
    image_1_3 = Image('src/resources/test1_3')
    image_1_3.assemble()
    image_1_3.print_tile_grid()
    assert image_1_3.tile_grid == [1951, 2311, 3079]


def test_assembe_2_2_image():
    image_2_2 = Image('src/resources/test2_2')
    image_2_2.assemble()
    image_2_2.print_tile_grid()


def test_assembe_2_2_rotate_flip_image():
    image_2by2 = Image('src/resources/test2_2')
    tile_1427 = image_2by2.tiles_map[1427]
    tile_1427.flip()
    tile_1951 = image_2by2.tiles_map[1951]
    tile_1951.rotate()
    image_2by2.assemble()
    image_2by2.print_tile_grid()
    pass
