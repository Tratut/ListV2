def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_rmstrchar(x, less):
    res = ''
    for i in range(ft_len(x)):
        if x[i] not in less:
            res += x[i]
    return res

# print(ft_rmstrchar(["a", "s", "d"], "s"))
