from os import chdir, getcwd
from os.path import dirname, realpath, join
from curses import init_pair
from json import load

from model.tiles.tile import Tile
from view.colors.colordict import colors
__author__ = 'Kellan Childers'


def set_tiles():
    """Load the tile colors and make sure they are valid.

    :return: A dictionary of tile values and background colors
    """
    # App has to change directories in case it was opened outside its folder.
    # Applying dirname multiple times goes one level back each time.
    chdir(dirname(dirname(realpath(__file__))))

    # os.getcwd here returns the path of the whole app, not /controller.
    with open(join(getcwd(), 'settings/tiles.config'), 'r') as config_file:
        tile_dict = load(config_file)

    for value, color in tile_dict.items():
        if color not in colors:
            raise KeyError("Could not assign colors")

    return tile_dict


def set_tile_colors():
    """Set up the color schemes 7 through 18 for use with tiles.

    :return: null
    """
    tile_dict = set_tiles()

    for i in range(1, len(tile_dict.items())+1):
        value = 2**i
        init_pair(i+6, colors["black"], colors[tile_dict[str(value)]])


def next_tile(tile):
    """Get the next tile in the sequence.

    :param tile: the current tile
    :return: the next tile in the sequence
    """
    next_value = tile.value * 2
    # I don't know why str(next_value works when it's not a color but I'm not questioning it.
    return Tile(next_value, str(next_value))
