from __future__ import print_function


def get_permutations1(s):
    """
    Append (or prepend) every character to each permutation of the
    string which does not contain the current character
    """
    if not s:
        return ['']
    else:
        res = []
        for i, c in enumerate(s):
            rest_s = s[:i] + s[i + 1:]
            rest_perms = get_permutations1(rest_s)
            for perm in rest_perms:
                res.append(perm + c)
        return res


def insert_at(s, c, i):
    return s[:i] + c + s[i:]


def get_permutations2(s):
    """
    Insert the first (or last) character to every spot of each permutation
    of the remaining string after this character
    """
    if not s:
        return ['']
    else:
        res = []
        c = s[0]
        rest_s = s[1:]
        rest_perms = get_permutations2(rest_s)
        for perm in rest_perms:
            for i in range(len(perm) + 1):
                ns = insert_at(perm, c, i)
                res.append(ns)
        return res


def get_permutations3_aux(s, cand, res):
    """Backtrack"""
    if not s:
        res.append(cand)
    else:
        for i, c in enumerate(s):
            get_permutations3_aux(s[:i] + s[i + 1:], cand + c, res)


def get_permutations3(s):
    res = []
    cand = ''
    get_permutations3_aux(s, cand, res)
    return res


def _test():
    pass


def _print():
    s1 = 'abc'
    r1 = get_permutations1(s1)
    r2 = get_permutations2(s1)
    r3 = get_permutations3(s1)
    r1.sort()
    r2.sort()
    r3.sort()
    print(r1)
    print(r2)
    print(r3)


if __name__ == '__main__':
    _test()
    _print()
