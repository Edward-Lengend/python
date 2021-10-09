a = 10
b = 20
print(f'a = {a}, b = {b}')
# 法一:通过第三个变量

c = a
a = b
b = c
print(f'a = {a}, b = {b}')

# 法二：
a, b = b, a
print(f'a = {a}, b = {b}')