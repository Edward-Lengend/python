"""
获取进程编号

1.获取进程编号的目的
获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的。

获取进程编号的两种操作
·获取当前进程编号
·获取当前父进程编号

2.获取当前进程编号
os.getpid()表示获取当前进程编号

3.获取当前父进程编号
os.getppid()表示获取当前父进程编号

如果父进程等于子进程编号， 则这个子进程由父进程创建

"""

import multiprocessing
from time import *
import os


# 跳舞任务
def dance():
    # 获取当前进程（子进程）编号
    dance_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing.current_process()
    print("dance_process_id:", dance_process_id, multiprocessing.current_process())
    # 获取当前进程父进程编号
    dance_process_parent_process_id = os.getppid()
    print(f'dance_process_parent_process的父进程编号{dance_process_parent_process_id}')

    for i in range(3):
        print('跳舞中')
        sleep(0.2)
        # 扩展：根据进程编号，kill指定进程
        os.kill(dance_process_id, 9)  # 9是强制杀死进程


# 唱歌任务
def sing():
    sing_process_id = os.getpid()
    print("sing_process_id:", sing_process_id, multiprocessing.current_process())
    # 获取当前进程父进程编号
    sing_process_parent_process_id = os.getppid()
    print(f'sing_process_parent_process的父进程编号{sing_process_parent_process_id}')
    for i in range(3):
        print('唱歌中')
        sleep(0.2)


# 获取当前进程编号
main_process_id = os.getpid()  # 当前进程是主进程
print(f'main_process_id = {main_process_id}')
# 获取当前进程对象，查看当前代码是由哪个进程执行的:multiprocessing.current_process()
print(f'multiprocessing.current_process() = {multiprocessing.current_process()}')


# 创建子进程
dance_process = multiprocessing.Process(group=None, target=dance)
print("dance_process:", dance_process)
sing_process = multiprocessing.Process(group=None, target=sing)
print("sing_process:", sing_process)

# 3.启动进程对应的任务

dance_process.start()
sing_process.start()
