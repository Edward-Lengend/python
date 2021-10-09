name = input("输入你的名字： ")
print("你好， 我的名字叫%s，请多多关照" % name)

student_id = 1
print("学生的学号为%06d" % student_id)

# price = 8.5
# weight = 7.5
# print("苹果价格： %.2f， 苹果重量: %.2f" % (price, weight))

print("我的名字是%s, 学号是%d" % (name, student_id))
print("我的名字是%s, 学号是%s" % (name, student_id))

# f格式化字符串
# 语法 ： f'{表达式}'
print(f'我的名字是{name}, 学号是{student_id}')
