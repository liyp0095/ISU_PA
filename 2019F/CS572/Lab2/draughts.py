#!/bin/python
#-*- coding: utf8 -*-

import sys
sys.path.append("../")
sys.path.append("../aima_python")

# import importlib
# Game = importlib.import_module("aima-python.games")
from aima_python.games import Game

import wx

class Draughts:
    def __init__(self):
        app = wx.App()
        frame = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
	           | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
        frame.Show()
        app.MainLoop()

def main():
    d = Draughts()


if __name__ == '__main__':
    main()
