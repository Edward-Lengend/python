# 线程之间共享全局变量数据出现错误问题会出问题

import threading
import time

g_num = 0


def testA():
    global g_num
    for i in range(10 ** 6):
        g_num += 1
    print('testA:', g_num)


def testB():
    global g_num
    for i in range(10 ** 6):
        g_num += 1
    print('testB:', g_num)


if __name__ == '__main__':
    testA_thread = threading.Thread(target=testA)
    testB_thread = threading.Thread(target=testB)

    testA_thread.start()
    # 线程等待，保证数据不会有问题
    testA_thread.join()  # 主线程等待这个线程执行完才会继续进行

    testB_thread.start()

"""
线程同步的两种方式：
1.线程等待
2.互斥锁
"""
