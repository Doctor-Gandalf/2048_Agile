import view.misc.util as util
from controller.colorcontroller import set_scheme
from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


def draw_tile(window, tile, position, dimensions):
    """Draw a tile at a place on the board

    :param window: The window to draw the tile to
    :param tile: The tile to draw
    :type tile: Tile
    :param position: The position of the top-left corner of the tile (y, x coordinate system)
    :param dimensions: The size of the area to draw the tile in (y, x coordinate system)
    :return: null
    """
    set_scheme(tile.background)
    util.draw_group(window,
                    [(y, x) for y in range(position[0], dimensions[0]+1)
                     for x in range(position[1], dimensions[1]+1)],
                    character=str(tile.value),
                    color_scheme=7)
