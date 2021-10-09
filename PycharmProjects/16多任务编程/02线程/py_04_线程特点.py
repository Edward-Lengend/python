"""
线程的注意点介绍
1.线程之间执行是无序的,具体哪个线程决定是由CPU调度决定的
2.主线程会等待所的子线程执行结束再结束
sub_thread = threading.Thread(target=task, daemon=True)

3.线程之间共享全局变量
4.线程之间共享全局变量数据出现错误问题
"""