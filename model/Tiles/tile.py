from abc import ABCMeta
__author__ = 'Kellan Childers'


class Tile(metaclass=ABCMeta):
    def __init__(self, value=0, background="white"):
        self.value = value
        self.background = background

    def get_value(self):
        return self.value

    def get_background(self):
        return self.background