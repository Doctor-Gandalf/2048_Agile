import os
from json import load
from os import chdir, getcwd
from os.path import dirname, realpath, join

from controller.keycommands.commanddict import commands

__author__ = 'Kellan Childers'


def execute_command(key):
    """Execute a preset command based on a changeable key binding.
    Key binding found in settings directory as keymap.config.

    :param key: the key to call the command.
    :return: the result of the command called.
    """
    # App has to change directories in case it was opened outside its folder.
    # Applying dirname multiple times goes one level back each time.
    chdir(dirname(dirname(dirname(realpath(__file__)))))

    # os.getcwd here returns the path of the whole app, not /controller.
    with open(join(getcwd(), 'settings/keymap.config'), 'r') as config_file:
        keymap = load(config_file)

    # The key needs to be in both the keymap and a valid function call.
    if key in keymap and keymap[key] in commands:
        return commands[keymap[key]]()
    else:
        raise KeyError("Invalid Command")
