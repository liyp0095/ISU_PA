#!/bin/python
#-*- coding: utf8 -*-

import sys
sys.path.append("../")
sys.path.append("../aima_python")
from copy import deepcopy

# import importlib
# Game = importlib.import_module("aima-python.games")
from aima_python.games import Game, GameState, alphabeta_search, alphabeta_cutoff_search

import wx

class Draughts(Game):
    def __init__(self):
        self.state = self.initState()
        pass
        # app = wx.App()
        # frame = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
	    #        | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
        # frame.Show()
        # app.MainLoop()

    def initState(self):
        board = {}
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 0:
                    # x_positions.append((i, j))
                    board[(i, j)] = "X"
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    # y_positions.append((i, j))
                    board[(i, j)] = "O"
        to_move = "O"
        moves = self.get_moves(to_move, board)
        return GameState(to_move=to_move, utility=0, board=board, moves=moves)


    def get_moves(self, player_to_move, board):
        moves = []
        for pos, player in board.items():
            # print(pos, player)
            if player_to_move in player:
                moves.extend(self.can_move(player, pos, board))
                # self.can_jump(player, pos, board)
        return moves


    def can_move(self, player, pos, board):
        action = []
        if "O" in player or "K" in player:
            action.extend(self.valid_move(player, pos, (pos[0] - 1, pos[1] + 1), board))
            action.extend(self.valid_move(player, pos, (pos[0] - 1, pos[1] - 1), board))
            action.extend(self.valid_move(player, pos, (pos[0] - 2, pos[1] + 2), board))
            action.extend(self.valid_move(player, pos, (pos[0] - 2, pos[1] - 2), board))
        if "X" in player or "K" in player:
            action.extend(self.valid_move(player, pos, (pos[0] + 1, pos[1] + 1), board))
            action.extend(self.valid_move(player, pos, (pos[0] + 1, pos[1] - 1), board))
            action.extend(self.valid_move(player, pos, (pos[0] + 2, pos[1] + 2), board))
            action.extend(self.valid_move(player, pos, (pos[0] + 2, pos[1] - 2), board))
        return action


    def can_jump(self, player, board):
        pass


    def valid_move(self, player, s_pos, e_pos, board):
        # print(s_pos, e_pos)
        if s_pos[0] < 0 or s_pos[0] > 7:
            return []
        if s_pos[1] < 0 or s_pos[1] > 7:
            return []
        if e_pos[0] < 0 or e_pos[0] > 7:
            return []
        if e_pos[1] < 0 or e_pos[1] > 7:
            return []
        if e_pos in board.keys():
            return []
        if player == "O":
            if (e_pos[0] == s_pos[0] - 1 and e_pos[1] == s_pos[1] - 1) \
                or (e_pos[0] == s_pos[0] - 1 and e_pos[1] == s_pos[1] + 1):
                return [(s_pos, e_pos)]
            if (e_pos[1] == s_pos[1] - 2 and e_pos[0] == s_pos[0] - 2 and \
                    (s_pos[0]-1, s_pos[1]-1) in board.keys() and \
                    board[(s_pos[0]-1, s_pos[1]-1)] == "X") or \
                (e_pos[1] == s_pos[1] - 2 and e_pos[0] == s_pos[0] + 2 and \
                    (s_pos[0]+1, s_pos[1]-1) in board.keys() and \
                    board[(s_pos[0]+1, s_pos[1]-1)] == "X"):
                return [(s_pos, e_pos)]
        if player == "X":
            if e_pos[0] == s_pos[0] + 1 and e_pos[1] == s_pos[1] - 1:
                # print(1)
                return [(s_pos, e_pos)]
            if e_pos[0] == s_pos[0] + 1 and e_pos[1] == s_pos[1] + 1:
                return [(s_pos, e_pos)]
            if (e_pos[1] == s_pos[1] + 2 and e_pos[0] == s_pos[0] - 2 and \
                    (s_pos[0]-1, s_pos[1]+1) in board.keys() and \
                    board[(s_pos[0]-1, s_pos[1]+1)] == "O") or \
                (e_pos[1] == s_pos[1] + 2 and e_pos[0] == s_pos[0] + 2 and \
                    (s_pos[0]+1, s_pos[1]+1) in board.keys() and \
                    board[(s_pos[0]+1, s_pos[1]+1)] == "O"):
                return [(s_pos, e_pos)]
        if "K" in player:
            if (e_pos[1] == s_pos[1] - 1 and e_pos[0] == s_pos[0] - 1) or \
                (e_pos[1] == s_pos[1] - 1 and e_pos[0] == s_pos[0] + 1) or \
                (e_pos[1] == s_pos[1] + 1 and e_pos[0] == s_pos[0] - 1) or \
                (e_pos[1] == s_pos[1] + 1 and e_pos[0] == s_pos[0] + 1):
                return [(s_pos, e_pos)]
            if (e_pos[1] == s_pos[1] - 2 and e_pos[0] == s_pos[0] - 2 and \
                    (s_pos[0]-1, s_pos[1]-1) in board.keys() and \
                    board[(s_pos[0]-1, s_pos[1]-1)] == "X") or \
                (e_pos[1] == s_pos[1] - 2 and e_pos[0] == s_pos[0] + 2 and \
                    (s_pos[0]+1, s_pos[1]-1) in board.keys() and \
                    board[(s_pos[0]+1, s_pos[1]-1)] == "X") or \
                (e_pos[1] == s_pos[1] + 2 and e_pos[0] == s_pos[0] - 2 and \
                    (s_pos[0]-1, s_pos[1]+1) in board.keys() and \
                    board[(s_pos[0]-1, s_pos[1]+1)] == "X") or \
                (e_pos[1] == s_pos[1] + 2 and e_pos[0] == s_pos[0] + 2 and \
                    (s_pos[0]+1, s_pos[1]+1) in board.keys() and \
                    board[(s_pos[0]+1, s_pos[1]+1)] == "X"):
                return [(s_pos, e_pos)]
        return []


    def ai_move(self):
        self.update_state("X")
        a = alphabeta_cutoff_search(self.state, self, eval_fn=self.eval_fn)
        self.state = self.result(self.state, a)
        self.update_state("O")
        # alphabeta_search(self.state, self)


    def eval_fn(self, state):
        board = state.board
        return 1


    def update_state(self, player):
        # self.state.to_move = player
        to_move = player
        board = self.state.board
        moves = self.get_moves(player, self.state.board)
        self.state = GameState(to_move=to_move, utility=0, board=board, moves=moves)


    def actions(self, state):
        return self.state.moves


    def post_user_act(self, pos1, pos2):
        for move in self.state.moves:
            if move[-1] == pos2 and move[0] == pos1:
                self.state = self.result(self.state, move)
                break


    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()
        for i,m in enumerate(move):
            if i == 0:
                continue
            board[m] = board[move[i-1]]
            if abs(m[0] - move[i-1][0]) == 2:
                print(m, move[i-1])
                del board[((m[0]+move[i-1][0])/2,(m[1]+move[i-1][1])/2)]
            del board[move[i-1]]
        to_move=("O" if state.to_move == "X" else "X")
        return GameState(to_move=("O" if state.to_move == "X" else "X"),
                        utility=self.compute_utility(board, move, state.to_move),
                        board=board, moves=self.get_moves(to_move, board))


    def utility(self, state, player):
        return state.utility if player == "X" else -state.utility


    def compute_utility(self, board, move, player):
        return 1 if len(self.get_moves(player, board)) == 0 else 0


    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0


def main():
    d = Draughts()
    d.ai_move()


if __name__ == '__main__':
    main()
