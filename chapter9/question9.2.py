from __future__ import print_function


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def get_num_paths(grid):
    if not grid:
        return 0
    if not grid[0]:
        return 0
    x = len(grid) - 1
    y = len(grid[0]) - 1
    return factorial(x + y) / (factorial(x) * factorial(y))


def get_path(x, y, path, t, grid):
    """Top-Down DP"""
    if (x, y) in t:
        return t[(x, y)]
    path.append((x, y))
    if x == 0 and y == 0:
        return True
    success = False
    if x >= 1 and grid[x - 1][y] != 1:
        success = get_path(x - 1, y, path, t, grid)
    if not success and y >= 1 and grid[x][y - 1] != 1:
        success = get_path(x, y - 1, path, t, grid)
    if not success:
        path.pop()
    t[(x, y)] = success
    return success


def _test():
    pass


def _print():
    print(factorial(3))
    print(factorial(4))
    grid = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    path = []
    t = {}
    y = len(grid) - 1
    x = len(grid[0]) - 1
    get_path(x, y, path, t, grid)
    print(path)


if __name__ == '__main__':
    _test()
    _print()
