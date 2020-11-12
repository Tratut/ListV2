def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_rmstrspc(x):
    res = ''
    for i in range(ft_len(x)):
        res += x[i]
    return res

# print(ft_rmstrspc(["a", "s", "d"]))
