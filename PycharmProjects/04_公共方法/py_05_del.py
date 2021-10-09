str1 = 'abcdefgh'
t1 = (100, 200, 300, 400)
list1 = [10, 20, 30, 40]
dict1 = {'name': 'python', 'age': 30}

del str1
# print(str1)
# del(list1)  # del 空格 或 括号 都可以
# print list1
del list1[0]
print(list1)

del dict1['name']
print(dict1)