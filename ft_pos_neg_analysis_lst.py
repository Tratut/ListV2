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


def ft_kol_num(x):
    i = 0
    while x > 0:
        x //= 10
        i += 1
    return i


def max_lst(x):
    maxx = x[0]
    for i in range(ft_len(x)):
        if maxx < x[i]:
            maxx = x[i]
    return maxx


def min_lst(x):
    minn = x[0]
    for i in range(ft_len(x)):
        if minn > x[i]:
            minn = x[i]
    return minn


def ft_sumlst(x):
    res = 0
    for i in range(ft_len(x)):
        res += x[i]
    return res


def ft_sred(x):
    res = ft_sumlst(x) // ft_len(x)
    return res


def ft_pos_neg_analysis_lst(x):
    tab = "\t"
    mas_sort = ft_pos_neg_separator_lst(x)

    print("Положительные:" + tab + "Отрицательные:")

    print("Количество чисел: {},".format(ft_len(mas_sort[2]))
          + tab + "Количество чисел: {}".format(ft_len(mas_sort[1])))

    print("Максимальная цифра: {},".format(max_lst(mas_sort[2]))
          + tab + "Максимальная цифра: {}".format(max_lst(mas_sort[0])))

    print("Минимальная цифра: {},".format(min_lst(mas_sort[2]))
          + tab + "Минимальная цифра: {}".format(min_lst(mas_sort[0])))

    print("Сумма чисел: {},".format(ft_sumlst(mas_sort[2]))
          + tab + "Сумма чисел: {}".format(ft_sumlst(mas_sort[0])))

    print("Среднее значение: {}".format(ft_sred(mas_sort[2]))
          + tab + "Среднее значение: {}".format(ft_sred(mas_sort[0])))

    print()

    print("Количество нулей:", ft_len(mas_sort[1]))
