from __future__ import print_function


def set_zero(matrix):
    """O(m + n) space solution"""
    n = len(matrix)
    if not n:
        return
    m = len(matrix[0])
    row = [False for i in range(n)]  # `row` stores row indexes
    column = [False for i in range(m)]  # `column` stores column indexes

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(n):
        for j in range(m):
            if row[i] or column[j]:
                matrix[i][j] = 0


def set_zero2(matrix):
    """
    O(1) space solution that uses first row and column to store information
    """
    n = len(matrix)
    if not n:
        return
    m = len(matrix[0])
    first_row_zero = False  # Whether the first row contains zero
    first_column_zero = False  # Wether the first column contains zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    first_row_zero = True
                if j == 0:
                    first_column_zero = True
                matrix[0][j] = 0
                matrix[i][0] = 0
    # Traverse the matrix string from matrix[1][1]
    for i in range(1, n):
        for j in range(1, m):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if first_column_zero:
        for i in range(n):
            matrix[i][0] = 0
    if first_row_zero:
        for j in range(m):
            matrix[0][j] = 0


def _test():
    matrix = [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    matrix2 = [row[:] for row in matrix]  # Deep copy
    set_zero(matrix)
    set_zero2(matrix2)
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            assert matrix[i][j] == matrix[i][j]


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
