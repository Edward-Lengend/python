"""
体验异常传递
需求：
1.尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可。
2.读取内容要求：尝试循环读取内容，无内容时循环读取，
    读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户。
"""


import time
try:
    f = open('111.txt', 'r')
    # 尝试循环读取内容
    try:
        while True:
            content = f.readline()
            if len(content) == 0:  # 读取完内容自动退出循环
                break
            time.sleep(2)  # 休眠2秒
            print(content)
    except:
        print("循环意外终止")
    finally:
        f.close()
        print("文件关闭")
except FileNotFoundError:
    print('文件不存在')

