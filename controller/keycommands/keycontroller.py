import os
from json import load

from controller.keycommands.commanddict import commands

__author__ = 'Kellan Childers'


def execute_command(key):
    """Execute a preset command based on a changeable key binding.
    Key binding found in settings directory as keymap.config.

    :param key: the key to call the command.
    :return: the result of the command called.
    """
    # os.getcwd here returns the path of the whole app, not /controller.
    with open(os.path.join(os.getcwd(), 'settings/keymap.config'), 'r') as config_file:
        keymap = load(config_file)

    # The key needs to be in both the keymap and a valid function call.
    if key in keymap and keymap[key] in commands:
        return commands[keymap[key]]()
    else:
        raise KeyError("Invalid Command")
