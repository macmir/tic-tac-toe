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
    cntX = 0
    cntO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                cntX += 1
            elif board[i][j] == O:
                cntO += 1
    if cntO > cntX:
        return X
    elif cntX > cntO:
        return O
    else:
        return X


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
    # else:
    #     raise NameError("Invalid move!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
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


def max_val(state):
    v = -999
    if terminal(state):
        return utility(state)

    for action in actions(state):
        v = max(v, min_val(result(state, action)))

    return v


def min_val(state):
    v = 999
    p = 0
    if terminal(state):
        return utility(state)

    for action in actions(state):
        v = min(v, max_val(result(state, action)))
        p += 1
    print(f'min val {p}')
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X and not terminal(board):
        moves = []
        score = []
        prev = 0
        for action in actions(board):
            moves.append(action)
            score.append(max_val(result(board, action)))
            if max_val(result(board, action)) >= prev:
                break
            prev = max_val(result(board, action))
        tot = list(zip(moves, score))
        print('minimax', prev)
        tot.sort(key=lambda x: x[1])
        return tot[0][0]

    if player(board) == O and not terminal(board):
        moves = []
        score = []
        prev = 0
        for action in actions(board):

            moves.append(action)
            score.append(min_val(result(board, action)))
            if min_val(result(board, action)) <= prev:
                break
            prev = min_val(result(board, action))

        tot = list(zip(moves, score))
        tot.sort(key=lambda x: x[1])
        return tot[0][0]
