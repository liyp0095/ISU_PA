#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_pos(pos, size):
    zero_x, zero_y, board_length, cell_length, radius = \
        get_paint_element(size)
    col = (pos[0] - zero_x) / cell_length
    row = (pos[1] - zero_y) / cell_length
    return int(row), int(col)


def get_paint_element(size):
    x, y = size
    y = y - 33
    board_length = min(x, y)
    cell_length = board_length / 8
    zero_x = max(0, (x-y)/2)
    zero_y = max(0, (y-x)/2)
    return zero_x, zero_y, board_length, cell_length, cell_length / 2.8
