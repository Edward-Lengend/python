"""
reduce（func，lst），其中func必须有两个参数
每次func计算的结果继续和序列的下一个元素做累积计算
"""
import functools  # 使用reduce需要模块

list1 = [1, 2, 3, 4, 5]


def func(a, b):
    return a + b


result = functools.reduce(func, list1)
print(result)