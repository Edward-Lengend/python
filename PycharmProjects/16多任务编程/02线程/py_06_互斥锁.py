"""
1.互斥锁的概念
互斥锁：对共享数据进行锁定，保证同一时刻只能有一个线程去操作。
注意：
·互斥锁是多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程需要等待，
等互斥锁使用完释放后，其它等待的线程再去抢这个锁。

3.互斥锁的使用
threading模块中定义了Lock变量，这个变量本质上是一个函数，通过调用这个函数可以获取一把互斥锁。
互斥锁使用步骤：

#创建锁
mutex=threading.Lock（）

#上锁
mutex.acquire（）
..这里编写代码能保证同一时刻只能有一个线程去操作，对共享数据进行锁定...

#释放锁
mutex.release（）

注意点：
·acquire和release方法之间的代码同一时刻只能有一个线程去操作
·如果在调用acquire方法的时候其他线程已经使用了这个互斥锁，
那么此时acquire方法会堵塞，直到这个互斥锁释放后才能再次上锁。
"""

import threading
import time

g_num = 0
# 创建互斥锁,Lock本质上是一个函数, 通过调用函数可以得到一把互斥锁
lock = threading.Lock()


def testA():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(10 ** 6):
        g_num += 1
    print('testA:', g_num)
    # 释放锁
    lock.release()
    # 线程执行完自动销毁


def testB():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(10 ** 6):
        g_num += 1
    print('testB:', g_num)
    # 释放锁
    lock.release()
    # 线程执行完自动销毁


if __name__ == '__main__':
    testA_thread = threading.Thread(target=testA)
    testB_thread = threading.Thread(target=testB)

    testA_thread.start()

    testB_thread.start()

    # 互斥绩可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
    # 线程等待和互斥锁都是把多任务改成单任务去执行，保证数据的准确性，但是执行性能会下降

