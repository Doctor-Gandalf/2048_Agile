import view.misc.util as util

from curses import color_pair
from math import log, floor
from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


def draw_tile(window, tile, position, dimensions):
    """Draw a tile at a place on the board.
    Note: the first row will be one character shorter than the others when the console height is odd.

    :param window: The window to draw the tile to
    :param tile: The tile to draw
    :type tile: Tile
    :param position: The position of the top-left corner of the tile (y, x coordinate system)
    :param dimensions: The size of the area to draw the tile in (y, x coordinate system)
    :return: null
    """
    color_scheme = int(log(tile.value, 2))+6

    util.draw_group(window, [(y, x) for y in range(position[0], dimensions[0] + 1)
                             for x in range(position[1], dimensions[1] + 1)],
                    color_scheme=color_scheme,
                    character=" ")

    title_y = position[0]
    title_x = position[1]
    window.addstr(title_y, title_x, str(tile.value), color_pair(color_scheme))

    window.refresh()
