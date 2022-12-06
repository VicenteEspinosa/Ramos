def sum_n(n):
    Profile.record('sum_n', [n])
    if n > 0:
        if n == 1:
            return 1
        else:
            return n + sum_n(n - 1)
    else:
        return None