import model.keyfunctions as kf
__author__ = 'Kellan Childers'
"""Compile all user-facing functions here with easy to remember names to allow keymapping.
   Actual functions should be defined in model.keyfunctions.py."""


commands = {"w": kf.move_up,
            "s": kf.move_down,
            "a": kf.move_left,
            "d": kf.move_right
            }
