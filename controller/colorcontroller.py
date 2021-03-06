from os import chdir, getcwd
from os.path import dirname, realpath, join
from curses import init_pair
from json import load

from view.colors.colordict import colors

__author__ = 'Kellan Childers'


def create_colorschemes():
    """Set up colorschemes based on colors.config file.
    Colors allowed are limited to 8 curses colors.

    :return: null
    """
    # App has to change directories in case it was opened outside its folder.
    # Applying dirname multiple times goes one level back each time.
    chdir(dirname(dirname(realpath(__file__))))

    # os.getcwd here returns the path of the whole app, not /controller.
    with open(join(getcwd(), 'settings/colors.config'), 'r') as config_file:
        colormap = load(config_file)

    for _, color in colormap.items():
        if color not in colors:
            raise KeyError("Could not assign colors")

    # Sets the three main colors for the app screen.
    # First color: text. Second color: background.
    init_pair(1, colors[colormap["primary"]], colors[colormap["secondary"]])
    init_pair(2, colors[colormap["secondary"]], colors[colormap["primary"]])
    init_pair(3, colors[colormap["secondary"]], colors[colormap["tertiary"]])
    init_pair(4, colors[colormap["tertiary"]], colors[colormap["secondary"]])
    init_pair(5, colors[colormap["primary"]], colors[colormap["tertiary"]])
    init_pair(6, colors[colormap["tertiary"]], colors[colormap["primary"]])


def set_scheme(background_color):
    """Set up pair 7 as black with a background color
    Note: depreciated. Any time a color scheme is changed, it is changed for all drawn characters

    :param background_color: The color to use for the background
    :return: null
    """
    if background_color not in colors:
        raise KeyError("Could not assign colors")

    init_pair(7, colors["black"], colors[background_color])
