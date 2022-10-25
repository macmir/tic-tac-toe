import tictactoe

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[O, X, O],
            [X, O, X],
            [O, O, X]]

board = initial_state()

print(tictactoe.terminal(board))
