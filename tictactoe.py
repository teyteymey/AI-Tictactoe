"""
Tic Tac Toe Player
"""

import math
import copy

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
    Returns player who has the next turn on a board (either X or O)
    """
    x_items = 0
    o_items = 0
    for row in board:
        x_items += row.count(X)
        o_items += row.count(O)

    print("items:")
    print(x_items)
    print(o_items)

    if (x_items == 0 and o_items == 0):
        return X
    elif x_items > o_items:
        return O
    elif x_items < o_items:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    players_turn = player(copied_board)
    if copied_board[action[0]][action[1]] != EMPTY:
        raise RuntimeError()
    
    copied_board[action[0]][action[1]] = players_turn
    return copied_board
    



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    copied_board = copy.deepcopy(board)
    
    #Gonna try flattening the board with list comprehensions
    flat_board = [value for row in copied_board for value in row]
    print(flat_board)
    #check rows
    for i in range(0, 9, 3):
        if (flat_board[i] is not None and flat_board[i] == flat_board[i+1] and flat_board[i+1] == flat_board[i+2]):
            return flat_board[i]
    
    print("here1")
    #check columns
    for i in range(3):
        if (flat_board[i] is not None and flat_board[i] == flat_board[i+3] and flat_board[i+3] == flat_board[i+6]):
            return flat_board[i]
    
    print("here2")

    #check diagonals
    if (flat_board[0] is not None and flat_board[0] == flat_board[4] and flat_board[4] == flat_board[8]):
            return flat_board[0]
    if (flat_board[0] is not None and flat_board[2] == flat_board[4] and flat_board[4] == flat_board[6]):
            return flat_board[2]
    print("here3")

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Finished if there is a winner or no more actions
    if (not actions(board) or winner(board) is not None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_result = winner(board)
    #Tried conditional comprehension, TODO: check if its correct hheeh
    return 0 if winner_result == None else 1 if winner_result == X else -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    player_turn = player(board)

    #player X wants to maximise, and player O wants to minimise
    best_action = None
    if player_turn == X:
        value = -math.inf
        for action in actions(board):
            resulting_value = maxvalue(result(board, action))
            if resulting_value > value:
                value = resulting_value
                best_action = action
    else:
        value = math.inf
        for action in actions(board):
            resulting_value = minvalue(result(board, action))
            if resulting_value < value:
                value = resulting_value
                best_action = action

    return best_action

def minvalue(board):
    value = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        value = min(value, maxvalue(result(board, action)))

    return value


def maxvalue(board):
    value = -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        value = max(value, minvalue(result(board, action)))

    return value

