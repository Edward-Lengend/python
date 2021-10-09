import numpy as np


a = np.array([[80, 86],
                [82, 80],
                [85, 78],
                [90, 90],
                [86, 82],
                [82, 90],
                [78, 80],
                [92, 94]])

b = np.array([[0.7], [0.3]])

# 矩阵乘法api  :matmul和dot, 区别在于dot可以将矩阵和数字相乘
score_array = np.matmul(a, b)
# print(score_array)

# dot
print(np.dot(a, 10))