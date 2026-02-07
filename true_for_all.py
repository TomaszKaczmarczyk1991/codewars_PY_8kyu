def _all(seq, fun):
    if len(seq) == 0:
        return True

    for x in seq:
        if not fun(x):
            return False
    return True