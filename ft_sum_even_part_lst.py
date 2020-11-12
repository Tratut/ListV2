def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_rmstrchar(x):
    res = 0
    for i in range(ft_len(x)):
        if x[i] % 2 == 0:
            res += x[i]
    return res
