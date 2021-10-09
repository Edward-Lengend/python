# 死锁：一直等待对方释放锁的情景叫做死锁

# 需求：多线程同时根据下标在列表中取值，要保证同一时刻只能有一个线程去取值

import threading

lock = threading.Lock()


def get_value(index):
    # 上锁
    lock.acquire()
    my_list = [1, 4, 6]
    if index >= len(my_list):
        print('下标越界')
        return
        # 取值不成功， 也要释放互斥锁， 不要影响后面进程进行
        lock.release()
    else:
        print(f'value = {my_list[index]}')
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        value_thread = threading.Thread(target=get_value, args=(i,))
        value_thread.start()
