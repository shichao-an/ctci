from __future__ import print_function


def has_won(board):
    """n x n board, 0 for empty, 1 for cross, and 2 for circle"""
    n = len(board)
    # Check rows
    for row in range(n):
        if board[row][0] != 0:
            flag = True
            for col in range(1, n):
                if board[row][col] != board[row][col - 1]:
                    flag = False
                    break
            if flag:
                return board[row][0]
    # Check columns
    for col in range(n):
        if board[0][col] != 0:
            flag = True
            for row in range(1, n):
                if board[row][col] != board[row - 1][col]:
                    flag = False
                    break
            if flag:
                return board[0][col]
    # Check diagonal
    if board[0][0] != 0:
        flag = True
        for i in range(1, n):
            if board[i][i] != board[i - 1][i - 1]:
                flag = False
                break
        if flag:
            return board[0][0]
    # Check reverse diagonal
    if board[0][n - 1] != 0:
        flag = True
        for i in range(1, n):
            if board[i][n - 1 - i] != board[i - 1][n - i]:
                flag = False
                break
        if flag:
            return board[0][n - 1]
    return 0  # Tie


def _test():
    pass


def _print():
    b1 = [
        [2, 1, 1, 1],
        [2, 2, 1, 1],
        [1, 1, 2, 1],
        [0, 2, 1, 1],
    ]
    print(has_won(b1))


if __name__ == '__main__':
    _test()
    _print()
