import curses
from math import floor
__author__ = 'Kellan Childers'


def add_title(window, title,  window_y=0, bold=True, underline=True, color_scheme=1):
    """Add a title centered on a line.

    :param window: the window to title
    :param title: the title to add
    :param window_y: the height of the title
    :param bold: whether or not to bold the title (default True)
    :type bold: Boolean
    :param underline: whether or not to underline the title (default True)
    :type underline: Boolean
    :param color_scheme: the scheme to use for coloring the title (default 1)
    :return: null
    """
    height, width = window.getmaxyx()
    _, title_x = center(height, width, 1, len(title))
    window.addstr(window_y, title_x, title,
                  (curses.A_BOLD if bold else 0) |
                  (curses.A_UNDERLINE if underline else 0)|
                  (curses.color_pair(color_scheme)))
    window.refresh()


def center(console_height, console_width, window_height, window_width):
    """Find point to start window on center.

    :param console_height: the height of the console
    :param console_width: the width of the console
    :param window_height: the height of the window
    :param window_width: the width of the window
    :return: a tuple representing the coordinates of the start window
    """
    start_y = floor((console_height-window_height)/2)
    start_x = floor((console_width-window_width)/2)
    return start_y, start_x


def color_border(window, start_y, start_x, stop_y, stop_x, color_scheme):
    """Create a border around a window in a certain color.

    :param window: The window to add a border to.
    :param start_y: The y portion of the starting coordinate on the screen
    :param start_x: The x portion of the starting coordinate on the screen
    :param stop_y: The y portion of the ending coordinate on the screen
    :param stop_x: The x portion of the ending coordinate on the scree
    :param color_scheme: The color to paint the border
    :return:
    """
    # You'll want to make this use draw_group. Don't.
    try:
        for i in range(start_y, stop_y):
            window.addstr(i, start_x, ' ', curses.color_pair(color_scheme))
            window.addstr(i, stop_x, ' ', curses.color_pair(color_scheme))
        for i in range(start_x, stop_x):
            window.addstr(start_y, i, ' ', curses.color_pair(color_scheme))
            window.addstr(stop_y, i, ' ', curses.color_pair(color_scheme))
        # for loops fail to add last element.
        window.addstr(stop_y, stop_x, ' ', curses.color_pair(color_scheme))
    except curses.error:
        # curses.error is raised at end of line and can safely be ignored.
        pass
    window.refresh()


def draw_group(window, group, color_scheme, character=' '):
    """Draw a group of points

    :param window:
    :param group: The list of points in form (y, x) to draw
    :param character: The type of character to draw (default space)
    :type character: String
    :param color_scheme: The number of the color scheme to use for coloring
    :return:
    """
    try:
        for point in group:
            window.addstr(point[0], point[1], character, curses.color_pair(color_scheme))
    except curses.error:
        # curses.error is raised at end of line and can safely be ignored.
        pass

    window.refresh()


def size_lim(console_height, console_width, bound_height, bound_width):
    """Limit the size of a window if the console is over a certain size.

    :param console_height: the height of the window
    :param console_width: the width of the window
    :param bound_height: the minimum height to start binding the window
    :param bound_width: the minimum width to start binding the window
    :return: a pair of dimensions for the window
    """
    y = console_height if console_height <= bound_height else floor(7*console_height/8)
    x = console_width if console_width <= bound_width else floor(7*console_width/8)
    return y, x
