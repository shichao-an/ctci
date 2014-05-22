from __future__ import print_function

"""
Imagine a robot sitting on the upper left corner of an X by Y grid. The robot
can only move in two directions: right and down. How many possible paths are
there for the robot to go from (0,0) to (X, Y)?

FOLLOW UP

Imagine certain spots are "off limits", such that the robot cannot step on
them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""


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
    """Top-Down DP, O(mn)"""
    if (x, y) in t:
        return t[(x, y)]
    path.append((x, y))
    if x == 0 and y == 0:
        return True
    success = False
    if y >= 1 and grid[y - 1][x] != 1:
        success = get_path(x, y - 1, path, t, grid)
    if not success and x >= 1 and grid[y][x - 1] != 1:
        success = get_path(x - 1, y, path, t, grid)
    if not success:
        path.pop()
    t[(x, y)] = success
    return success


def get_path2(x, y, path, grid, m, n):
    """DFS, O(mn)"""
    if x > m - 1 or y > n - 1 or len(path) == m + n - 1:
        return
    else:
        if grid[y][x] != 1:
            path.append((x, y))
            get_path2(x + 1, y, path, grid, m, n)
            get_path2(x, y + 1, path, grid, m, n)


def get_paths_aux(x, y, path, grid, m, n, res):
    path.append((x, y))
    if x == m - 1 and y == n - 1:
        res.append(path[:])
    else:
        if x + 1 < m and grid[y][x + 1] != 1:
            get_paths_aux(x + 1, y, path, grid, m, n, res)
        if y + 1 < n and grid[y + 1][x] != 1:
            get_paths_aux(x, y + 1, path, grid, m, n, res)
    path.pop()


def get_paths(grid):
    path = []
    res = []
    m = len(grid[0])
    n = len(grid)
    get_paths_aux(0, 0, path, grid, m, n, res)
    return res


def _test():
    pass


def _print():
    grid = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]
    path1 = []
    t1 = {}
    y = len(grid) - 1
    x = len(grid[0]) - 1
    get_path(x, y, path1, t1, grid)
    print(get_num_paths(grid))
    print(path1)
    path2 = []
    get_path2(0, 0, path2, grid, len(grid[0]), len(grid))
    print(path2)
    print(get_paths(grid))


if __name__ == '__main__':
    _test()
    _print()
