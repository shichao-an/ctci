from __future__ import print_function


def get_subsets1_aux(s, k):
    if k == 0:
        return [[]]
    else:
        res = [[]]
        for i in range(len(s)):
            rest_subsets = get_subsets1_aux(s[i + 1:], k - 1)
            for subset in rest_subsets:
                subset.insert(0, s[i])
            res += rest_subsets
        return res


def get_subsets1(s):
    n = len(s)
    return get_subsets1_aux(s, n)


def get_subsets2_aux(s, i):
    if len(s) == i:
        return [[]]
    else:
        res = []
        rest_subsets = get_subsets2_aux(s, i + 1)
        more_subsets = []
        for subset in rest_subsets:
            new_subset = subset[:]
            new_subset.insert(0, s[i])
            more_subsets.append(new_subset)
        res = rest_subsets + more_subsets
        return res


def get_subsets2(s):
    return get_subsets2_aux(s, 0)


def get_subsets3_aux(s, subset, res):
    """Combinatorics/Backtrack"""
    if not s:
        res.append(subset[:])
    else:
        subset.append(s[0])
        get_subsets3_aux(s[1:], subset, res)
        subset.pop()
        get_subsets3_aux(s[1:], subset, res)


def get_subsets3(s):
    subset = []
    res = []
    get_subsets3_aux(s, subset, res)
    return res


def get_subsets4_aux(s, subset, res):
    """Backtrack"""
    res.append(subset[:])
    for i, c in enumerate(s):
        subset.append(c)
        get_subsets4_aux(s[i + 1:], subset, res)
        subset.pop()


def get_subsets4(s):
    subset = []
    res = []
    get_subsets4_aux(s, subset, res)
    return res


def _test():
    pass


def _print():
    s1 = [1, 2, 3]
    r1 = get_subsets1(s1)
    print(s1)
    r2 = get_subsets2(s1)
    r3 = get_subsets3(s1)
    r4 = get_subsets4([1, 2, 3])

    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == '__main__':
    _test()
    _print()
