# lambda表达式
# lambda 参数: 表达式
fn1 = lambda a, b: a + b
result = fn1(10, 20)
print(result)


# 可变参数 args
fn2 = lambda *args: args
print(fn2(10, 20))
print(fn2(20, 30, 40))

# 可变参数 **kwargs
fn3 = lambda ** kwargs: kwargs
print(fn3(name='zhangsan'))
print(fn3(age=30))

# 带判断的lambda
fn4 = lambda a, b: a if a > b else b
print(200, 100)

# 列表数据按照key排序
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Jerry', 'age': 10}
]
# 按照姓名升序
students.sort(key=lambda a: a['name'])
print(students)
# 按照姓名降序
students.sort(key=lambda a: a['name'], reverse=True)
print(students)
# 按age升序
students.sort(key=lambda x: x['age'])
print(students)
