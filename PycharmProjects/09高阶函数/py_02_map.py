"""
map（func，lst），将传入的函数变量func作用到lst变量的每个元素中
并将结果迭代器（Python3）返回。

"""

# 需求：计算1ist1序列中各个数字的2次方。

list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list1)
print(result)
print(list(result))