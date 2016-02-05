from model.tiles.tile import Tile
from controller.tilecontroller import next_tile
from view.tilecolors.tileview import draw_tile_on_board
__author__ = 'Kellan Childers'


def demo(stdscr):
    """Draw all tiles to demonstrate appearance of each tile and test spacing.

    :param stdscr: The standard screen
    :return: null
    """
    tile = Tile(2, str(2))
    for x in range(4):
        for y in range(4):
            draw_tile_on_board(stdscr, tile, (x, y))
            tile = next_tile(tile) if tile.value != 4096 else Tile(2, str(2))
