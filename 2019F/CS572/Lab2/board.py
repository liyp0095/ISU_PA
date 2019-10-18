#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

from draughts import Draughts
import util

class Board(wx.Frame):

    def __init__(self, *args, **kw):
        super(Board, self).__init__(*args, **kw)
        self.draughts = Draughts()

        self.InitUI()

    def InitUI(self):
        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))
        # wx.MessageBox("You Win!", "Message" ,wx.OK | wx.ICON_INFORMATION)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

        self.SetTitle("Colours")
        self.Centre()
        self.SetSize(600, 400)
        self.select = False
        self.start = (0, 0)
        self.valid = set()


    def OnLeftDown(self, e):
        # dc = wx.PaintDC(self)
        dc = wx.ClientDC(self)
        dc.SetPen(wx.Pen('#04d4d4', 3, wx.SOLID))
        dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))

        row, col = util.get_pos(e.GetPosition(), self.GetSize())
        zero_x, zero_y, board_length, cell_length, radius = \
            util.get_paint_element(self.GetSize())
        if row < 0 or row > 7 or col < 0 or col > 7:
            return

        board = self.draughts.state.board

        if self.select:
            if (row, col) in self.valid:
                self.draughts.post_user_act(self.start, (row, col))

                self.Refresh()
                self.select = False

                if not self.draughts.ai_move():
                    wx.MessageBox("You Win!", "Message" ,wx.OK | wx.ICON_INFORMATION)
                    return
                if len(self.draughts.state.moves) == 0:
                    wx.MessageBox("You Lose!", "Message" ,wx.OK | wx.ICON_INFORMATION)
                    return
                self.Refresh()
            else:
                self.Refresh()
                self.select = False
            self.valid = set()
        else:
            if (row, col) not in board.keys():
                return
            self.start = (row, col)
            self.highlight(row, col)
            self.select = True
        # self.Refresh()

    def highlight(self, row, col):
        zero_x, zero_y, board_length, cell_length, radius = \
            util.get_paint_element(self.GetSize())
        # dc = wx.PaintDC(self)
        dc = wx.ClientDC(self)
        dc.SetPen(wx.Pen('#04d4d4', 3, wx.SOLID))
        dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))
        dc.DrawRectangle(zero_x+col*cell_length, zero_y+row*cell_length, cell_length, cell_length)
        dc.SetPen(wx.Pen('#0404d4', 3, wx.SOLID))
        for m in self.draughts.state.moves:
            if m[0] == (row, col):
                self.valid.add(m[-1])
                dc.DrawRectangle(zero_x+m[-1][1]*cell_length, zero_y+m[-1][0]*cell_length, cell_length, cell_length)


    def draw_piece(self, row, col, player):
        # dc = wx.PaintDC(self)
        dc = wx.ClientDC(self)
        zero_x, zero_y, board_length, cell_length, radius = \
            util.get_paint_element(self.GetSize())
        if player == "O":
            dc.SetBrush(wx.Brush('#050505'))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius)
        if player == "X":
            dc.SetBrush(wx.Brush('#d5d5d5'))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius)
        if player == "OK":
            dc.SetBrush(wx.Brush('#050505'))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius)
            dc.SetPen(wx.Pen('#d4f404', radius/10, wx.SOLID))
            dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius/2)
        if player == "XK":
            dc.SetBrush(wx.Brush('#d5d5d5'))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius)
            dc.SetPen(wx.Pen('#54d404', radius/10, wx.SOLID))
            dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))
            dc.DrawCircle(zero_x + cell_length * (col+0.5),
                        zero_y + cell_length * (row+0.5), radius/2)


    def OnSize(self, e):
        self.Refresh()


    def OnPaint(self, e):
        state = self.draughts.state
        board = state.board

        zero_x, zero_y, board_length, cell_length, radius = \
            util.get_paint_element(self.GetSize())

        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#d4d4d4'))

        dc.SetBrush(wx.Brush('#f0f0f0'))
        dc.DrawRectangle(zero_x, zero_y, board_length, board_length)

        dc.SetPen(wx.Pen('#dc4c4c'))
        dc.SetBrush(wx.Brush('#dc4c4c', wx.SOLID))
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    dc.DrawRectangle(zero_x+i*cell_length,
                                zero_y+j*cell_length,
                                cell_length, cell_length)

        dc.SetPen(wx.Pen('#050505'))
        dc.SetBrush(wx.Brush('#050505'))
        # dc.DrawCircle(30, 30, 10)
        for pos, player in board.items():
            self.draw_piece(pos[0], pos[1], player)


def main():

    app = wx.App()
    ex = Board(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
