import os
from json import load
from curses import init_pair
from controller.colordict import colors
__author__ = 'Kellan Childers'


def create_colorschemes():
    """Set up colorschemes based on colors.config file.
    Colors allowed are limited to 8 curses colors.

    :return: null
    """
    # os.getcwd here returns the path of the whole app, not /controller.
    with open(os.path.join(os.getcwd(), 'settings/colors.config'), 'r') as config_file:
        colormap = load(config_file)

    for _, color in colormap.items():
        if color not in colors:
            raise KeyError("Could not assign colors")

    # Sets the three main colors for the app screen.
    # First color: text. Second color: background.
    init_pair(1, colors[colormap["primary"]], colors[colormap["secondary"]])
    init_pair(2, colors[colormap["secondary"]], colors[colormap["tertiary"]])
    init_pair(3, colors[colormap["primary"]], colors[colormap["tertiary"]])
