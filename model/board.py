from model.plots.plot import Plot
from model.tiles.tile import Tile
from model.dice import roll
__author__ = 'Kellan Childers'

board = Plot(4, 4)


def place_tile(stdbrd):
    """Place a tile randomly on the board.

    :param stdbrd: the standard board
    :return: the board
    """
    tile = Tile(2, str(2)) if roll(1, 6) >= 2 else Tile(4, str(4))
    done = False
    if None not in stdbrd:
        raise IndexError("Could not place tile")
    while not done:
        x = roll(1, 4) - 1
        y = roll(1, 4) - 1
        if stdbrd[x][y] is None:
            stdbrd[x][y] = tile
            done = True
    return stdbrd


def replace_tile(stdbrd, location, new_tile):
    """Replace a tile on the board with another tile.

    :param stdbrd: the standard board
    :param location: the location to replace
    :param new_tile: the new tile to add into the location
    :return: the board
    """
    x, y = location
    stdbrd[x][y] = new_tile
    return stdbrd


def clear_location(stdbrd, location):
    """Remove a tile from a location on the board.

    :param stdbrd: the standard board
    :param location: the location to clear
    :return: the board
    """
    return replace_tile(stdbrd, location, None)


def clear_board(stdbrd):
    """Clear the board of all entries

    :param stdbrd: the standard board
    :return: the cleared board
    """
    for x in range(4):
        for y in range(4):
            clear_location(stdbrd, (x, y))
    return stdbrd
