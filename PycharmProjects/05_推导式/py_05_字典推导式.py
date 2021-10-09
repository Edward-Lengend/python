# 需求1：创建一个字典， key 是1-5的数字， value 是这个数字的2次方
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1)

# 需求2
list1 = ['name', 'age', 'gender']
list2 = ['Tom', '20', 'man']
# 将上面两个列表合并成一个字典

dict1 = {list1[i]:list2[i] for i in range(0,len(list1))}
print(dict1)