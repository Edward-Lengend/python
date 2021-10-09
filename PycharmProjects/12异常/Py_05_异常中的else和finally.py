try:
    print('1')
except Exception as result:
    print(result)
else:
    print('没有异常则执行else')


try:
    f = open('test.txt', 'r')
except FileNotFoundError:
    f = open('test.txt', 'w')
else:
    print('没有异常')
finally:  # 无论是否有异常都会执行
    f.close()
