try:
    print(num)
except NameError as result:
    print(result)

try:
    print(1/0)
except Exception as result:  # Exception 是所有程序异常类的父类
    print(result)