from __future__ import print_function


def generate_parens_aux(left, right, cand, res):
    """
    `left` and `right` are remaining left and right parens
    """
    if left > right or left < 0:
        return
    elif left == 0 and right == 0:
        res.append(cand)
    else:
        generate_parens_aux(left - 1, right, cand + '(', res)
        generate_parens_aux(left, right - 1, cand + ')', res)


def generate_parens(n):
    res = []
    cand = ''
    generate_parens_aux(n, n, cand, res)
    return res


def _test():
    pass


def _print():
    r1 = generate_parens(1)
    r2 = generate_parens(2)
    r3 = generate_parens(3)
    r4 = generate_parens(4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == '__main__':
    _test()
    _print()
