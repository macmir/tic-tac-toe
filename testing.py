import tictactoe

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY]]

board = initial_state()
if tictactoe.terminal(board) == True:
    print("Game is over!")
    print(f"The winner is: {tictactoe.winner(board)}")
    print(f"Utility = {tictactoe.utility(board)}")
else:
    print("Keep playing!")
    act = tictactoe.actions(board)
    print(act)
    print(tictactoe.result(board, (0, 0)))
    print(board)
