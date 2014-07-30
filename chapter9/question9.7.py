from __future__ import print_function
import copy

"""
Implement the "paint fill" function that one might see on many image editing
programs. That is, given a screen (represented by a two-dimensional array of
colors), a point, and a new color, fill in the surrounding area until the
color changes from the original color.
"""


def paint_fill_aux(screen, x, y, old_color, new_color):
    if x < 0 or y < 0 or x >= len(screen[0]) or y >= len(screen):
        return
    elif screen[y][x] != old_color:
        return
    else:
        screen[y][x] = new_color
        paint_fill_aux(screen, x + 1, y, old_color, new_color)
        paint_fill_aux(screen, x, y + 1, old_color, new_color)
        paint_fill_aux(screen, x - 1, y, old_color, new_color)
        paint_fill_aux(screen, x, y - 1, old_color, new_color)


def paint_fill(screen, x, y, new_color):
    paint_fill_aux(screen, x, y, screen[y][x], new_color)


def get_adjacent(screen, x, y):
    """Get adjacent pixels of the same color"""
    res = []
    n = len(screen)
    m = len(screen[0])
    color = screen[y][x]
    if y > 0 and screen[y - 1][x] == color:
        res.append((x, y - 1))
    if y < n - 1 and screen[y + 1][x] == color:
        res.append((x, y + 1))
    if x > 0 and screen[y][x - 1] == color:
        res.append((x - 1, y))
    if x < m - 1 and screen[y][x + 1] == color:
        res.append((x + 1, y))
    return res


def paint_fill2(screen, x, y, new_color):
    queue = []
    visited = set()
    queue.append((x, y))
    visited.add((x, y))
    while queue:
        cur = queue.pop(0)
        cur_x = cur[0]
        cur_y = cur[1]
        for pixel in get_adjacent(screen, cur_x, cur_y):
            if pixel not in visited:
                queue.append(pixel)
                visited.add(pixel)
        screen[cur_y][cur_x] = new_color


def _test():
    pass


def _print():
    s1 = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
    ]
    s2 = copy.deepcopy(s1)
    paint_fill(s1, 1, 1, 2)
    for row in s1:
        print(row)
    print()
    paint_fill2(s2, 1, 1, 2)
    for row in s2:
        print(row)
    print()
    paint_fill2(s2, 5, 0, 8)
    for row in s2:
        print(row)


if __name__ == '__main__':
    _test()
    _print()
