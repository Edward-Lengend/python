# python中， 值是靠引用传递的

a = 1
b = a
if id(a) == id(b):  # id()可以查看变量的十进制地址
    print(f'id(a) = {id(a)}')
    print(f'id(b) = {id(b)}')
    print('a与b为同一段地址')
    print('int为不可变类型')

a = 2
print(f'b = {b}')
print(f'id(a) = {id(a)}')
print(f'id(b) = {id(b)}')
