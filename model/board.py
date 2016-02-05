from model.plots.plot import Plot
from model.tiles.tile import Tile
from model.dice import roll
from controller.tilecontroller import next_tile
__author__ = 'Kellan Childers'

board = Plot(4, 4)


def place_tile(stdbrd):
    """Place a tile randomly on the board.

    :param stdbrd: the standard board
    :return: null
    """
    tile = Tile(2, str(2)) if roll(1, 6) >= 3 else Tile(4, str(4))
    done = False
    while not done:
        x = roll(1, 4) - 1
        y = roll(1, 4) - 1
        if stdbrd[x][y] is None:
            stdbrd[x][y] = tile
            done = True
