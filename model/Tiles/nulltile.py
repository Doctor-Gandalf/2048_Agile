from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


class NullTile(Tile):
    def __init__(self):
        super(Tile, self).__init__(value=0, background='white')
