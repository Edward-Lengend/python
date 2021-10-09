import multiprocessing
import time

# 定义全局变量列表
g_list = list()  # list() <=>  []


def add_data():
    for i in range(3):
        # 因为列表是可变类型， 可以在原有内存的基础上修改数据
        # 修改后内存地址不变， 所以不需要加上global关键字
        # global表示要修改全局变量的内存地址   
        g_list.append(i)
        print("add: ", i)
        time.sleep(0.2)
    print("添加完成！", g_list)
        
        
def read_data():
    print("read", g_list)


# 解决Windows无限递归创建子进程->通过判断是否是主模块解决
if __name__ == "__main__":  # Windows需要加上判断
    add_data_process = multiprocessing.Process(target=add_data)
    read_data_process = multiprocessing.Process(target=read_data)

    add_data_process.start()

    # 当前进程（主进程）等待add_data_process进程执行完，再往下执行
    add_data_process.join()

    read_data_process.start()

"""
结论， 进程之间不共享全局变量
原因：创建子进程是对主进程资源的拷贝
子进程是主进程的一个副本

提示：
对于Linux和Mac，主进程执行的代码不会拷贝，但是对于Windows系统，主进程执行的代码也会拷贝后执行
于是，对于Windows，创建子进程的代码，如果进行拷贝执行，相当于无限递归创建子进程，会报错
"""

