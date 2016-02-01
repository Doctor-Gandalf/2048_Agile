from model.tiles.tile import Tile
from controller.colorcontroller import set_tiles

__author__ = 'Kellan Childers'

tile_types = set_tiles()

two_tile = Tile(2, tile_types["2"])
four_tile = Tile(4, tile_types["4"])
eight_tile = Tile(8, tile_types["8"])
sixteen_tile = Tile(16, tile_types["16"])
thirty_two_tile = Tile(32, tile_types["32"])
sixty_four_tile = Tile(64, tile_types["64"])
one_twenty_eight_tile = Tile(128, tile_types["128"])
two_fifty_six_tile = Tile(256, tile_types["256"])
five_twelve_tile = Tile(512, tile_types["512"])
ten_twenty_four_tile = Tile(1024, tile_types["1024"])
twenty_forty_eight_tile = Tile(2048, tile_types["2048"])
forty_ninety_six_tile = Tile(4096, tile_types["4096"])
