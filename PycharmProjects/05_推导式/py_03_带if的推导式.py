# 需求：创建0-10的偶数列表
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 第二种方法： 加入if
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)