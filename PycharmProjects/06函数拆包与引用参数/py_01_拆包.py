# 元组拆包、

def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)
print(num2)


# 字典拆包
dict1 = {'name': 'Tom', 'aeg': 18}
a, b = dict1
print(a)  # 拿到key值
print(b)
print(dict1[a])
print(dict1[b])