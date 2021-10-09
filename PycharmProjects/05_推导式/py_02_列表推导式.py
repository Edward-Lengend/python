# 列表推导式
# 需求：创建一个0-10的列表

# 不用推导式
list1 = []
# while
i = 0
while i <= 10:
    list1.append(i)
    i += 1
print(list1)

# for
list2 = []
for i in range(0, 11):
    list2.append(i)
print(list2)

# 列表推导式

list3 = [i for i in range(10)]
# 第一个i是列表的返回值

print(list3)