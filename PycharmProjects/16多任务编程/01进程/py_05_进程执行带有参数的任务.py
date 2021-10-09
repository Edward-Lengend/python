"""
1.进程执行带有参数的任务的介绍
使用进程执行的任务带有参数，如何给函数传参呢？
Process类执行任务并给任务传参数有两种方式：
·args 表示以元组的方式给执行任务传参
·kwargs 表示以字典方式给执行任务传参
"""

import multiprocessing

# 显示信息的任务
def show_info(name, age):
    print(f'name = {name}, age = {age}')


# 创建子进程
# args传元组
# sub_process = multiprocessing.Process(target=show_info, args=("李四", 20))
# kwargs传字典,字典中的key要和参数名保持一直， 无顺序要求
sub_process = multiprocessing.Process(target=show_info,
                                      kwargs={'name': "李四", 'age': 20})

# 启动进程
sub_process.start()