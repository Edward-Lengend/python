"""
注意：
1.如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
2.一般try下方只放一行尝试执行的代码。
"""

# 错误类型: NameError
# print(num)

# 错误类型: ZeroDivisionError
# print(1/0)
try:
    print(num)
except NameError:
    print('有错误')

try:
    print(1/0)
except ZeroDivisionError:
    print('除数为0')