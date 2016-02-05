import view.board.util as util

from curses import color_pair, error
from math import log
from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


def draw_tile(window, tile, position, dimensions):
    """Draw a tile at a place on the window.
    Note: the first row will be one character shorter than the others when the console height is odd.

    :param window: The window to draw the tile to
    :param tile: The tile to draw
    :type tile: Tile
    :param position: The position of the top-left corner of the tile (y, x coordinate system)
    :param dimensions: The size of the area to draw the tile in (y, x coordinate system)
    :return: null
    """
    color_scheme = int(log(tile.value, 2))+6

    util.draw_group(window,
                    [(y, x) for y in range(position[0], dimensions[0] + 1)
                     for x in range(position[1], dimensions[1] + 1)],
                    color_scheme=color_scheme,
                    character=" ")

    title_y = position[0]
    title_x = position[1]
    window.addstr(title_y, title_x, str(tile.value), color_pair(color_scheme))

    window.refresh()


def draw_tile_on_board(window, tile, location):
    """Draw a tile at a place on the board.

    :param window: the window to draw the tile to
    :param tile: the tile to draw
    :type tile: Tile
    :param location: the location on the board to draw to
    :return: null
    """
    x, y = location
    x = (x-1) * 20 + 1
    y = (y-1) * 6 + 1
    end_x = x + 18
    end_y = y + 4
    y += 1 if y == 0 else 0
    end_x -= 1 if location[0] == 4 else 0
    end_y -= 1 if location[1] == 4 else 0

    position = y, x
    dimensions = end_y, end_x
    try:
        draw_tile(window, tile, position, dimensions)
    except error:
        pass
