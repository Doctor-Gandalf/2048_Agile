from model.tiles.tile import Tile
__author__ = 'Kellan Childers'


class TwoTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 2
        self.background = 'cyan'


class FourTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 4
        self.background = 'blue'


class EightTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 8
        self.background = 'green'


class SixteenTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 16
        self.background = 'yellow'


class ThirtyTwoTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 32
        self.background = 'magenta'


class SixtyFour(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 64
        self.background = 'red'


class OneTwentyEightTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 128
        self.background = 'red'


class TwoFiftySixTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 256
        self.background = 'red'


class FiveTwelveTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 512
        self.background = 'red'


class TenTwentyFourTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 1024
        self.background = 'red'


class TwentyFortyEightTile(Tile):
    def __init__(self):
        super(Tile, self).__init__()
        self.value = 2048
        self.background = 'red'
