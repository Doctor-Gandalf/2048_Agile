import view.misc.util as util
from curses import curs_set, color_pair
__author__ = 'Kellan Childers'


def initialize_window(stdscr):
    """Start up standard screen to allow easy startup for apps.

    :param stdscr: The standard screen used in curses
    :return: null
    """
    # Ensures a clean visual space.
    stdscr.clear()
    curs_set(False)

    # Set the background of the app to the secondary color.
    stdscr.bkgd(' ', color_pair(1))
    stdscr.refresh()


def draw_board(stdscr):
    """Draw 4x4 grid to act as background board.

    :param stdscr: The standard screen used in curses.
    :return: null
    """
    console_height, console_width = stdscr.getmaxyx()

    # This looks ugly but is the simplest way to color this many lines.
    game_height = console_height-1
    step = int((console_height-6)/4)+2
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)], 2)
    game_height -= step
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)], 2)
    game_height -= step
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)], 2)
    game_height -= step
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)], 2)
    util.draw_group(stdscr, [(0, x) for x in range(console_width)], 2)

    game_width = console_width-1
    step = int((console_width-6)/4)+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)], 2)
    game_width -= step+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)], 2)
    game_width -= step
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)], 2)
    game_width -= step+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)], 2)
    util.draw_group(stdscr, [(y, 0) for y in range(1, console_height)], 2)
