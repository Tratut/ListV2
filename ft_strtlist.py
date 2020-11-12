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

print(ft_strtlist("123456"))
