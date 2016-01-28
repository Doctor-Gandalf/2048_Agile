#!/usr/bin/python3
from controls.keycontroller import execute_command
__author__ = 'Kellan Childers'

if __name__ == "__main__":
    to_call = input("Wubalubbadubdub?")
    try:
        execute_command(to_call)
    except KeyError:
        print("Key not found")
