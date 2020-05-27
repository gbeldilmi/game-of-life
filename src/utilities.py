# -*- coding: utf-8 -*
import sys, os
def clear_screen():
    """Clear interpreter console"""
    if sys.platform.startswith('win32'): # for Windows
        os.system('cls')
    elif sys.platform.startswith('linux'): # for Linux
        os.system('clear')
    return