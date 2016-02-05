import view.board.draw as util
import view.viewmath as vmth

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
    start_x, start_y = position
    stop_x, stop_y = dimensions
    color_scheme = int(log(tile.value, 2))+6

    util.draw_group(window,
                    [(y, x) for y in range(start_y, stop_y + 1)
                     for x in range(start_x, stop_x + 1)],
                    color_scheme=color_scheme,
                    character=" ")

    title_y = start_y
    title_x = start_x
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
    position, dimensions = vmth.convert_loc_to_pos(location, window.getmaxyx())
    try:
        draw_tile(window, tile, position, dimensions)
    except error:
        pass
