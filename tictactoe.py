"""
Tic Tac Toe Player
"""
import copy
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
    if all(board):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i, j)
                possible_moves.append(action)
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        new_board = copy.deepcopy(board)
        move = player(board)
        i = action[0]
        j = action[1]
        new_board[i][j] = move
        return new_board
    else:
        raise NameError("Invalid move!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board) == True:
        j = 0
        while j < 3:
            if board[j][0] == board[j][1] and board[j][0] == board[j][2] == X:
                return X
            if board[j][0] == board[j][1] and board[j][0] == board[j][2] == O:
                return O
            else:
                j += 1
        j = 0
        while j < 3:
            if board[0][j] == board[1][j] and board[0][j] == board[2][j] == X:
                return X
            if board[0][j] == board[1][j] and board[0][j] == board[2][j] == O:
                return O
            else:
                j += 1

        if board[0][0] == board[1][1] and board[0][0] == board[2][2] == X:
            return X
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] == O:
            return O
        if board[2][0] == board[1][1] and board[2][0] == board[0][2] == X:
            return X
        if board[2][0] == board[1][1] and board[2][0] == board[0][2] == O:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    j = 0
    while j < 3:
        if board[j][0] == board[j][1] and board[j][0] == board[j][2] != EMPTY:
            return True
        else:
            j += 1
    j = 0
    while j < 3:
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] != EMPTY:
            return True
        else:
            j += 1

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] != EMPTY:
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] != EMPTY:
        return True

    empty = 0
    for k in range(3):
        for m in range(3):
            if board[k][m] == EMPTY:
                empty += 1

    if empty == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return 0
