# abs()绝对值
# round() 四舍五入

# print(abs(-10))
# print(round(1.2))
# print(round(1.9))


def sum_num(a, b, f):
    return f(a) + f(b)


print(sum_num(-1, 2, abs))