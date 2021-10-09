"""
1导入进程包
import multiprocessing

2.Process进程类的说明
Process([group [, target [, name [, args [, kwargs]]]]])
·group：指定进程组，目前只能使用None
·target：执行的目标任务名(一个函数/一个方法)
·name：进程名字（一般不设置， 有默认名）
·args：以元组方式给执行任务传参
·kwargs：以字典方式给执行任务 传参Process创建的实例对象的常用方法：
·start()：启动子进程实例（创建子进程）
·join()：等待子进程执行结束
 terminate()：不管任务是否完成，立即终止子进程

Process创建的实例对象的常用属性：
name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
"""