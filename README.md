# Ai-tictactoe
Tic tac toe game in Python. Try your luck against my AI

## How to run
`python3 runner.py`

## Tic-Tac-Toe Functions Overview

#### `player(board)`
- **Purpose**: Determines which player's turn it is (`X` or `O`).
- **Rules**:
  - `X` always moves first.
  - Players alternate turns.
  - If the board is in a **terminal** state (game over), any return value is acceptable.

---

#### `actions(board)`
- **Purpose**: Returns all **possible actions** on the current board.
- **Format**: A set of tuples `(i, j)` where:
  - `i` = row index (0, 1, or 2)
  - `j` = column index (0, 1, or 2)
- **Rule**: A cell is a valid move if it is **empty** (neither `X` nor `O`).
- **Note**: For terminal boards, any return value is acceptable.

---

#### `result(board, action)`
- **Purpose**: Returns the **new board state** after applying the action.
- **Constraints**:
  - Must **not** modify the original board.
  - Should raise an **exception** if the action is invalid.
- **Implementation Tip**: Use a **deep copy** of the board before making changes.

---

#### `winner(board)`
- **Purpose**: Returns the **winner** of the game, if there is one.
- **Return Values**:
  - `"X"` if X has won
  - `"O"` if O has won
  - `None` if there is no winner yet or it's a tie
- **Winning Conditions**:
  - Three in a row (horizontal, vertical, or diagonal)
- **Assumption**: At most **one winner** exists per board (no invalid states).

---

#### `terminal(board)`
- **Purpose**: Checks if the game is **over**.
- **Return**:
  - `True` if someone has won or the board is full (tie)
  - `False` if the game is still in progress

---

#### `utility(board)`
- **Purpose**: Returns the **utility value** of a terminal board.
- **Values**:
  - `1` if X has won
  - `-1` if O has won
  - `0` if the game is a tie
- **Assumption**: Only called if `terminal(board)` is `True`.

---

#### `minimax(board)`
- **Purpose**: Returns the **optimal move** `(i, j)` for the current player.
- **Behavior**:
  - Chooses the best possible move to **maximize utility**.
  - If multiple moves are equally optimal, any one may be returned.
  - Returns `None` if the board is terminal (no moves left).
