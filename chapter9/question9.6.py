from __future__ import print_function

"""
Implement an algorithm to print all valid (i.e. properly opened and closed)
combinations of n-pairs of parentheses.

"""


def generate_parens1_aux(left, right, cand, res):
    """
    Backtrack: prune branch return
    `left` and `right` are remaining left and right parens
    """
    if left > right or left < 0:
        return
    elif left == 0 and right == 0:
        res.append(cand)
    else:
        generate_parens1_aux(left - 1, right, cand + '(', res)
        generate_parens1_aux(left, right - 1, cand + ')', res)


def generate_parens1(n):
    res = []
    cand = ''
    generate_parens1_aux(n, n, cand, res)
    return res


def generate_parens2_aux(left, right, cand, res):
    """
    Backtrack: prune by conditional branch
    """
    if left == 0 and right == 0:
        res.append(cand)
    else:
        if left > 0:
            generate_parens2_aux(left - 1, right, cand + '(', res)
        if right > left:
            generate_parens2_aux(left, right - 1, cand + ')', res)


def generate_parens2(n):
    res = []
    cand = ''
    generate_parens2_aux(n, n, cand, res)
    return res


def _test():
    pass


def _print():
    for i in range(1, 5):
        res = generate_parens1(i)
        print(res)
    for i in range(1, 5):
        res = generate_parens2(i)
        print(res)


if __name__ == '__main__':
    _test()
    _print()
