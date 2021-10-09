# 函数调用通过“key = value”形式， 可以不按照顺序传参

def user_info(name, age, gender):
    print(f'姓名：{name}, 年龄：{age}，性别：{gender}')


user_info('Rose', gender='女', age=18)
user_info(gender='女', age=18, name='Rose')
# 位置参数必须在关键字参数的前面
# ！ user_info(name='Tom', age=18, '女')  # 错误
