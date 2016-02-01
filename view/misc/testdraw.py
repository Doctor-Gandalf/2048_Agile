import view.tilecolors.numbertiles as nt
from view.tilecolors.tileview import draw_tile
__author__ = 'Kellan Childers'


def test_draw(stdscr):
    """Draw all tiles to demonstrate appearance of each tile and test spacing.

    :param stdscr: The standard screen
    :return: null
    """
    draw_tile(stdscr, nt.two_tile, (1, 1), (4, 19))
    draw_tile(stdscr, nt.four_tile, (1, 21), (4, 39))
    draw_tile(stdscr, nt.eight_tile, (1, 41), (4, 58))
    draw_tile(stdscr, nt.sixteen_tile, (1, 60), (4, 78))

    draw_tile(stdscr, nt.thirty_two_tile, (6, 1), (10, 19))
    draw_tile(stdscr, nt.sixty_four_tile, (6, 21), (10, 39))
    draw_tile(stdscr, nt.one_twenty_eight_tile, (6, 41), (10, 58))
    draw_tile(stdscr, nt.two_fifty_six_tile, (6, 60), (10, 78))

    draw_tile(stdscr, nt.five_twelve_tile, (12, 1), (16, 19))
    draw_tile(stdscr, nt.ten_twenty_four_tile, (12, 21), (16, 39))
    draw_tile(stdscr, nt.twenty_forty_eight_tile, (12, 41), (16, 58))
    draw_tile(stdscr, nt.forty_ninety_six_tile, (12, 60), (16, 78))

    draw_tile(stdscr, nt.two_tile, (18, 1), (22, 19))
    draw_tile(stdscr, nt.two_tile, (18, 21), (22, 39))
    draw_tile(stdscr, nt.two_tile, (18, 41), (22, 58))
    draw_tile(stdscr, nt.two_tile, (18, 60), (22, 78))
