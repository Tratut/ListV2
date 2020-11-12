def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_pos_neg_separator_lst(x):
    res = [[], [], []]
    for i in range(ft_len(x)):
        if x[i] < 0:
            res[0].append(x[i])
        elif x[i] > 0:
            res[2].append(x[i])
        else:
            res[1].append(x[i])
    return res
