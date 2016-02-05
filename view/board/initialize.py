import view.board.draw as draw
from curses import curs_set, color_pair
__author__ = 'Kellan Childers'


def initialize_window(stdscr):
    """Start up standard screen to allow easy startup for apps.

    :param stdscr: the standard screen used in curses
    :return: null
    """
    # Ensures a clean visual space.
    stdscr.clear()
    curs_set(False)

    # Set the background of the app to the secondary color.
    stdscr.bkgd(' ', color_pair(1))
    stdscr.refresh()


def draw_board_background(stdscr):
    """Draw 4x4 grid to act as background board.

    :param stdscr: the standard screen used in curses.
    :return: null
    """
    console_height, console_width = stdscr.getmaxyx()
    draw.color_hash(stdscr, (0, 0), (console_width, console_height), 2)
    draw.color_border(stdscr, (0, 0), (console_width, console_height), 2)
    draw.add_title(stdscr, "2048 Agile Edition by Kellan Childers",
                   color_scheme=2, underline=False)


def reset_board(stdscr):
    """Reset appearance between ticks to allow new tiles to be drawn

    :param stdscr: the standard screen used in curses
    :return: null
    """
    stdscr.clear()
    draw_board_background(stdscr)
