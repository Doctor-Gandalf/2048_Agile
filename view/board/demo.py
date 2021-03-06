from model.tiles.tile import Tile
from controller.tilecontroller import next_tile
__author__ = 'Kellan Childers'


def demo(stdbrd):
    """Add all tiles to board to demonstrate appearance of each tile and test spacing.

    :return: null
    """
    tile = Tile(2, str(2))
    for x in range(4):
        for y in range(4):
            stdbrd[x][y] = tile
            tile = next_tile(tile) if tile.value != 4096 else Tile(2, str(2))
