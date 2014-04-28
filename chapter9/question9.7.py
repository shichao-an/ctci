from __future__ import print_function


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


def _test():
    pass


def _print():
    s1 = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
    ]
    paint_fill(s1, 1, 1, 2)
    for row in s1:
        print(row)


if __name__ == '__main__':
    _test()
    _print()
