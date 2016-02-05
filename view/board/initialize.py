import view.board.draw as util
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
    util.color_hash(stdscr, (0, 0), (console_width, console_height), 2)
    util.color_border(stdscr, (0, 0), (console_width, console_height), 2)
    util.add_title(stdscr, "2048 Agile Edition by Kellan Childers",
                   color_scheme=2, underline=False)
