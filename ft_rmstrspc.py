def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_strtlist(x):
    mass = []
    for i in range(ft_len(x)):
        aaa = x[i]
        mass.append(aaa)
    return mass


def ft_rmstrspc(xx):
    x = ft_strtlist(xx)
    res = ''
    for i in range(ft_len(x)):
        if x[i] != ' ':
            res += x[i]
    return res
