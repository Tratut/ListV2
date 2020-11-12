def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_sumlst(x):
    res = 0
    for i in range(ft_len(x)):
        res += x[i]
    return res
