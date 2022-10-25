"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if not board:
        return "X"
    else:
        return "Y"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    j = 0
    while j < 3:
        if board[j][0] == board[j][1] and board[j][0] == board[j][2]:
            return True
        else:
            j += 1
    j = 0
    while j < 3:
        if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            return True
        else:
            j += 1

    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
