from __future__ import print_function


def rotate_matrix(matrix, n):

    # Layer index `i`
    for i in range(n // 2):
        start = i
        end = n - 1 - i
        # j = [start ... end - 1]
        for j in range(start, end):
            offset = j - start
            # Save top
            top = matrix[start][j]
            # Left to top
            matrix[start][j] = matrix[end - offset][start]
            # Bottom to left
            matrix[end - offset][start] = matrix[end][end - offset]
            # Right to bottom
            matrix[end][end - offset] = matrix[j][end]
            # Top to right
            matrix[j][end] = top


def _test():
    pass


def _print():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    # Assert NxN (square) matrix
    assert matrix
    h = len(matrix)
    w = len(matrix[0])
    assert h == w
    n = len(matrix)
    rotate_matrix(matrix, n)
    for r in matrix:
        print(r)

if __name__ == '__main__':
    _test()
    _print()
