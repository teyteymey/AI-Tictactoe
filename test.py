import tictactoe as ttt

board = ttt.initial_state()

for action in ttt.actions(board):
    print(ttt.result(board, action))