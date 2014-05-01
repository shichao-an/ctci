from __future__ import print_function


def estimate(solution, guess):
    """Return a tuple of hits and pseudo-hits"""
    hits = {
        'R': 0,
        'Y': 0,
        'G': 0,
        'B': 0,
    }
    phits = {
        'R': 0,
        'Y': 0,
        'G': 0,
        'B': 0,
    }
    if len(solution) != len(guess):
        return None
    for i, e in enumerate(solution):
        if e == guess[i]:
            hits[e] += 1
        elif e in guess:
            phits[e] += 1
    h = 0
    p = 0
    for c in hits:
        h += hits[c]
    for c in phits:
        p += phits[c]
    return h, p


def _test():
    pass


def _print():
    r1 = estimate('RGBY', 'GGRR')
    print(r1)


if __name__ == '__main__':
    _test()
    _print()
