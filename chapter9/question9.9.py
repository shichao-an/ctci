from __future__ import print_function

BOARD_SIZE = 8


def is_valid(columns, row, col):
    """
    Check whether coordinate (`row`, `col`) is valid against
    already valid existing coordinates in `columns`
    """
    # `row` is the current row; check against all previous rows
    for r in range(row):
        c = columns[r]
        # Check column
        if c == col:
            return False
        # Check diagonal
        if abs(c - col) == row - r:
            return False
    return True


def place_queens_aux(row, columns, res):
    if row == BOARD_SIZE:
        res.append(columns[:])
    else:
        for col in range(BOARD_SIZE):
            if is_valid(columns, row, col):
                columns[row] = col
                place_queens_aux(row + 1, columns, res)


def place_queens():
    res = []
    columns = [-1 for i in range(BOARD_SIZE)]
    place_queens_aux(0, columns, res)
    return res


def _test():
    pass


def _print():
    res = place_queens()
    print(res)


if __name__ == '__main__':
    _test()
    _print()
