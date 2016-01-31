import curses

import view.misc.util as util

__author__ = 'Kellan Childers'


def initialize_window(stdscr):
    """Start up standard screen to allow easy startup for apps.

    :param stdscr: the standard screen used in curses
    :return: null
    """
    # Ensures a clean visual space.
    stdscr.clear()
    curses.curs_set(False)

    # Set the background of the app to the secondary color.
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()


def draw_board(stdscr):
    console_height, console_width = stdscr.getmaxyx()

    game_height = console_height-1
    step = int((console_height-6)/4)+1
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)])
    game_height -= step+1
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)])
    game_height -= step
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)])
    game_height -= step+1
    util.draw_group(stdscr, [(game_height, x) for x in range(console_width)])
    util.draw_group(stdscr, [(1, x) for x in range(console_width)])

    game_width = console_width-1
    step = int((console_width-6)/4)+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)])
    game_width -= step+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)])
    game_width -= step
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)])
    game_width -= step+1
    util.draw_group(stdscr, [(y, game_width) for y in range(1, console_height)])
    util.draw_group(stdscr, [(y, 0) for y in range(1, console_height)])
