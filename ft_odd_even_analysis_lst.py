def ft_kol_num(x):
    i = 0
    while x > 0:
        x //= 10
        i += 1
    return i


def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_odd_even_separator(x):
    res = [[], []]
    for i in range(ft_len(x)):
        if x[i] % 2 == 0:
            res[0].append(x[i])
        else:
            res[1].append(x[i])
    return res


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


def ft_odd_even_analysis_lst(x):
    tab = "\t"
    mas_first_part = []
    mas_sort = ft_odd_even_separator(x)

    str1 = ft_len("Количество четных чисел: {},".format(ft_len(mas_sort[0])))
    str2 = ft_len("Максимальная четная цифра: ") + ft_kol_num(max_lst(mas_sort[0])) + 1
    str3 = ft_len("Минимальная четная цифра: {},".format(ft_kol_num(min_lst(mas_sort[0]))))
    str4 = ft_len("Сумма четных чисел: {},".format(ft_kol_num(ft_sumlst(mas_sort[0]))))

    mas_first_part.append(str1)
    mas_first_part.append(str2)
    mas_first_part.append(str3)
    mas_first_part.append(str4)

    mst = max_lst(mas_first_part)

    print("Анализ списка:")
    print("Количество четных чисел: {},".format(ft_len(mas_sort[0])) +
          tab * 2 + "Количество нечетных чисел: {}".format(ft_len(mas_sort[1])))

    print("Максимальная четная цифра: {},".format(max_lst(mas_sort[0]))
          + tab * 2 +
          "Максимальная нечетная цифра: {}".format(max_lst(mas_sort[1])))

    print("Минимальная четная цифра: {},".format(min_lst(mas_sort[0])) + tab * 2 +
          "Минимальная нечетная цифра: {}".format(min_lst(mas_sort[1])))

    print("Сумма четных чисел: {},".format(ft_sumlst(mas_sort[0])) + tab * 2 +
          "Сумма нечетных чисел: {}".format(ft_sumlst(mas_sort[1])))


# ft_odd_even_analysis_lst([1, 2, 3, 4, 52334342222222222222, 6])
