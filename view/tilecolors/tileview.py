import view.viewmath as vmth
import view.board.draw as draw
from view.board.initialize import reset_screen

from curses import color_pair, error
from math import log

from model.board import place_tile
from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


def take_turn(stdscr, stdbrd, *args, tile_count=1):
    """Execute a turn of the game.

    :param stdscr: the standard screen
    :param stdbrd: the standard board
    :param tile_count: the number of tiles to add (default 1)
    :param args: any extra functions to execute
    :return: a key
    """
    reset_screen(stdscr)
    if args:
        for function in args:
            function(stdbrd)
    try:
        for _ in range(tile_count):
            place_tile(stdbrd)
    except IndexError:
        return 'q'
    draw_board(stdscr, stdbrd)
    # Wait until a key is pressed; useful for testing startup visuals.
    return stdscr.getkey()


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

    draw.draw_group(window,
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
    if tile is None:
        return
    position, dimensions = vmth.convert_loc_to_pos(location, window.getmaxyx())
    try:
        draw_tile(window, tile, position, dimensions)
    except error:
        pass


def draw_board(window, stdbrd):
    """Draw the contents of the board.

    :param window: the window to draw on
    :param stdbrd: the standard board
    :return: null
    """
    for x in range(4):
        for y in range(4):
            draw_tile_on_board(window, stdbrd[x][y], (x, y))
