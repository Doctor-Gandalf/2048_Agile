import controller.keycommands.keyfunctions as kf
__author__ = 'Kellan Childers'
"""Compile all user-facing functions here with easy to remember names to allow keymapping.
   Actual functions should be defined in controller.keycommands.keyfunctions."""


commands = {"up": kf.move_up,
            "down": kf.move_down,
            "left": kf.move_left,
            "right": kf.move_right,
            "quit": kf.end,
            "continue": kf.skip
            }
