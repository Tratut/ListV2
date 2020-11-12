def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_odd_even_separator_lst(x):
    res = [[], []]
    for i in range(ft_len(x)):
        if x[i] % 2 == 0:
            res[0].append(x[i])
        else:
            res[1].append(x[i])
    return res
