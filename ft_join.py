def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_join(x, se=" "):
    res = ''
    for i in range(ft_len(x)):
        if i == ft_len(x) - 1:
            res += x[i]
        else:
            res += x[i] + se
    return res

# print(ft_join(["a", "s", "d"], ", "))
