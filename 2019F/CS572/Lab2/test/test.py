#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This program draws nine coloured rectangles
on the window.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx

class Action:
    def __init__():
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]


class Player:
    def __init__():
        self.action = []
        self.man


class State:
    def __init__():
        self.player = {}
        self.player["X"] = {}



class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        # wx.StaticText(self, label='x:', pos=(10,10))
        # wx.StaticText(self, label='y:', pos=(10,30))

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.SetTitle("Colours")
        self.Centre()
        self.SetSize(600, 400)


    def OnMove(self, e):
        pass


    def OnSize(self, e):
        self.Refresh()


    def OnPaint(self, e):

        state = [(1,2), (7,6), (4, 4)]
        x, y = self.GetSize()
        y = y - 33
        width = min(x, y)
        cell_width = width / 8

        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#d4d4d4'))

        dc.SetBrush(wx.Brush('#f0f0f0'))
        dc.DrawRectangle(max(0, (x-y)/2), max(0, (y-x)/2), width, width)

        dc.SetPen(wx.Pen('#dc4c4c'))
        dc.SetBrush(wx.Brush('#dc4c4c', wx.SOLID))
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    dc.DrawRectangle(max(0, (x-y)/2)+i*cell_width,
                                max(0, (y-x)/2)+j*cell_width,
                                cell_width, cell_width)

        dc.SetPen(wx.Pen('#050505'))
        dc.SetBrush(wx.Brush('#050505'))
        # dc.DrawCircle(30, 30, 10)
        r = cell_width / 2.8
        for p in state:
            dc.DrawCircle(max(0, (x-y)/2) + cell_width * (p[0]-0.5),
                        max(0, (y-x)/2) + cell_width * (p[1]-0.5), r)

        # dc.SetBrush(wx.Brush('#000000'))
        # dc.DrawRectangle(0.1*x, 0.1*y, 0.8*x, 0.8*y)

        # dc.SetBrush(wx.Brush('#c56c00'))
        # dc.DrawRectangle(0, 0, x, y)
        #
        # dc.SetBrush(wx.Brush('#c56c00'))
        # dc.DrawRectangle(0, 0, x, y)

        # dc.SetBrush(wx.Brush('#c56c00'))
        # dc.DrawRectangle(0.1*x, 15, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#1ac500'))
        # dc.DrawRectangle(130, 15, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#539e47'))
        # dc.DrawRectangle(250, 15, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#004fc5'))
        # dc.DrawRectangle(10, 105, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#c50024'))
        # dc.DrawRectangle(130, 105, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#9e4757'))
        # dc.DrawRectangle(250, 105, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#5f3b00'))
        # dc.DrawRectangle(10, 195, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#4c4c4c'))
        # dc.DrawRectangle(130, 195, 90, 60)
        #
        # dc.SetBrush(wx.Brush('#785f36'))
        # dc.DrawRectangle(250, 195, 90, 60)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
