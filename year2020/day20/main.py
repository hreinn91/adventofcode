from .Tile import Tile
from .Image import Image


# Execute part1
def part1():
    full_image = Image('day20/test1')
    tiles = full_image.tiles
    tile1 = tiles[0]
    tile2 = tiles[1]
    tile1.neighbour_top = tile2

    return


def main():
    part1()
    return
