# 1.导入进程包
import multiprocessing
from time import *


# 跳舞任务
def dance():
    for i in range(3):
        print('跳舞中')
        sleep(0.2)


# 唱歌任务
def sing():
    for i in range(3):
        print('唱歌中')
        sleep(0.2)


# 2.创建子进程（自己手动创建的叫子进程）
dance_process = multiprocessing.Process(group=None, target=dance)
sing_process = multiprocessing.Process(group=None, target=sing)
# group表示进程组，目前只能只用None， 一般不需要设置
# target 进程执行的目标任务(函数名)
# name  进程名， 不设置默认为Process-1，2....

# 3.启动进程对应的任务

dance_process.start()
sing_process.start()

# 主进程执行
# sing()

# 进程执行是无序的，具体哪个系统先执行，是由CPU决定的



