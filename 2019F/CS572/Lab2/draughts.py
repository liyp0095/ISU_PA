#!/bin/python
#-*- coding: utf8 -*-

import sys
import time
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
        # print(self.result(self.state, [(0, 0), (4, 4)]))
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
        jump_list = []
        move_list = []
        for pos, player in board.items():
            if player_to_move in player:
                jump_list.extend(self.can_jump(player, pos, board))
                move_list.extend(self.can_move(player, pos, board))
                # self.can_jump(player, pos, board)
        jump_list = [i for i in jump_list if len(i) > 1]
        if len(jump_list) == 0:
            moves = move_list
        else:
            moves = jump_list
        return moves


    def can_move(self, player, pos, board):
        action = []
        if "O" in player or "K" in player:
            if self.valid_move(player, pos, (pos[0] - 1, pos[1] + 1), board):
                action.append((pos, (pos[0] - 1, pos[1] + 1)))
            if self.valid_move(player, pos, (pos[0] - 1, pos[1] - 1), board):
                action.append((pos, (pos[0] - 1, pos[1] - 1)))
            # action.extend(self.valid_move(player, pos, (pos[0] - 1, pos[1] - 1), board))
            # action.extend(self.valid_move(player, pos, (pos[0] - 2, pos[1] + 2), board))
            # action.extend(self.valid_move(player, pos, (pos[0] - 2, pos[1] - 2), board))
        if "X" in player or "K" in player:
            if self.valid_move(player, pos, (pos[0] + 1, pos[1] + 1), board):
                action.append((pos, (pos[0] + 1, pos[1] + 1)))
            if self.valid_move(player, pos, (pos[0] + 1, pos[1] - 1), board):
                action.append((pos, (pos[0] + 1, pos[1] - 1)))
            # action.extend(self.valid_move(player, pos, (pos[0] + 1, pos[1] + 1), board))
            # action.extend(self.valid_move(player, pos, (pos[0] + 1, pos[1] - 1), board))
            # action.extend(self.valid_move(player, pos, (pos[0] + 2, pos[1] + 2), board))
            # action.extend(self.valid_move(player, pos, (pos[0] + 2, pos[1] - 2), board))
        return action


    def can_jump(self, player, pos, board):
        jump_list = []
        for i in [(1,1), (1,-1), (-1, -1), (-1, 1)]:
            if self.valid_move(player, pos, (pos[0]+2*i[0], pos[1]+2*i[1]), board):
                board1 = board.copy()
                del board1[(pos[0]+1*i[0], pos[1]+1*i[1])]
                board1[(pos[0]+2*i[0], pos[1]+2*i[1])] = board1[pos]
                del board1[pos]
                ujl = self.can_jump(player, (pos[0]+2*i[0], pos[1]+2*i[1]), board1)
                for l in ujl:
                    jump_list.append([pos]+l)
        if len(jump_list) == 0:
            return [[pos]]
        else:
            return jump_list


    def valid_move(self, player, s_pos, e_pos, board):
        mid_pos = ((s_pos[0] + e_pos[0])/2, (s_pos[1] + e_pos[1])/2)
        if s_pos[0] < 0 or s_pos[0] > 7:
            return False
        if s_pos[1] < 0 or s_pos[1] > 7:
            return False
        if e_pos[0] < 0 or e_pos[0] > 7:
            return False
        if e_pos[1] < 0 or e_pos[1] > 7:
            return False
        if e_pos in board.keys():
            return False

        if player == "O":
            if s_pos[0] - e_pos[0] == 1 and abs(s_pos[1] - e_pos[1]) == 1:
                return True
        if player == "X":
            if s_pos[0] - e_pos[0] == -1 and abs(s_pos[1] - e_pos[1]) == 1:
                return True
        if "K" in player:
            if abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1:
                return True

        if player == "O":
            if s_pos[0] - e_pos[0] == 2 and abs(s_pos[1] - e_pos[1]) == 2 and \
                mid_pos in board and "X" in board[mid_pos]:
                return True
        if player == "X":
            if s_pos[0] - e_pos[0] == -2 and abs(s_pos[1] - e_pos[1]) == 2 and \
                mid_pos in board and "O" in board[mid_pos]:
                return True
        if player == "OK":
            if abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2 and \
                mid_pos in board and "X" in board[mid_pos]:
                return True
        if player == "XK":
            if abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2 and \
                mid_pos in board and "O" in board[mid_pos]:
                return True
        return False


    def ai_move(self):
        self.update_state("X")
        if len(self.state.moves) == 0:
            return False
        start_time = time.time()
        a = alphabeta_cutoff_search(self.state, self, d=4, eval_fn=self.eval_fn)
        self.state = self.result(self.state, a)
        print("evaluation = " + str(self.eval_fn(self.state)))
        print("running time = " + str(time.time() - start_time))
        self.update_state("O")
        return True


    def eval_fn(self, state):
        # print(state)
        board = state.board
        X = []
        O = []
        XK = []
        OK = []
        for pos, piece in board.items():
            if piece == "X":
                X.append(pos)
            elif piece == "O":
                O.append(pos)
            elif piece == "OK":
                OK.append(pos)
            elif piece == "XK":
                XK.append(pos)
        # distance to opposite side
        valueX = 0
        valueO = 0
        for i in X:
            valueX += 1/(8-i[0])
        for i in O:
            valueO += 1/(8-i[0])
        value_distance = valueX - valueO

        # number of pieces
        value_number = (len(X) - len(O) + 5*len(XK) - 5*len(OK)) / 10

        value = value_number + value_distance
        # print(value)
        return value



    def update_state(self, player):
        # self.state.to_move = player
        to_move = player
        board = self.state.board
        moves = self.get_moves(player, self.state.board)
        if len(moves) != 0:
            utility = 0
        else:
            utility = 1
        self.state = GameState(to_move=to_move,
                        utility=(utility if "X" in player else -utility),
                        board=board, moves=moves)


    def actions(self, state):
        return state.moves


    def post_user_act(self, pos1, pos2):
        for move in self.state.moves:
            if move[-1] == pos2 and move[0] == pos1:
                self.state = self.result(self.state, move)
                break


    def result(self, state, move):
        # print("result")
        if move not in state.moves:
            return state
        board = state.board.copy()
        # print(board)
        # print(move)
        for i,m in enumerate(move):
            if i == 0:
                continue
            board[m] = board[move[i-1]]
            if abs(m[0] - move[i-1][0]) == 2:
                del board[((m[0]+move[i-1][0])/2,(m[1]+move[i-1][1])/2)]
            del board[move[i-1]]
        # print(board)
        for i in range(8):
            if (0, i) in board and board[(0, i)] == "O":
                board[(0, i)] = "OK"
            if (7, i) in board and board[(7, i)] == "X":
                board[(7, i)] = "XK"
        to_move=("O" if state.to_move == "X" else "X")
        return GameState(to_move=("O" if state.to_move == "X" else "X"),
                        utility=self.compute_utility(board, move, state.to_move),
                        board=board, moves=self.get_moves(to_move, board))


    def utility(self, state, player):
        return state.utility if player == "X" else -state.utility


    def compute_utility(self, board, move, player):
        return 1 if len(self.get_moves(player, board)) == 0 else 0


    def terminal_test(self, state):
        return len(state.moves) == 0


def main():
    d = Draughts()
    d.ai_move()


if __name__ == '__main__':
    main()
