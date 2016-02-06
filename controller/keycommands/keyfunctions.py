__author__ = 'Kellan Childers'
"""Place functions which interact with the model here.
   Only functions defined here can be executed from a key command or mouse input."""


def end():
    """Quit the game."""
    return False


def skip():
    """Continue the game without executing a function."""
    return True


def move(direction):
    """Move all tiles a given direction.

    :param direction: The direction to move the tiles
    :return:
    """
    return True


def move_up():
    """Move straight up.
    Convenience function for user facing portion.

    :return: result of move(direction)
    """
    return move('up')


def move_down():
    """Move straight up.
    Convenience function for user facing portion.

    :return: result of move(direction)
    """
    return move('down')


def move_left():
    """Move straight up.
    Convenience function for user facing portion.

    :return: result of move(direction)
    """
    return move('left')


def move_right():
    """Move straight up.
    Convenience function for user facing portion.

    :return: result of move(direction)
    """
    return move('right')
