import socket
import threading

# 处理客户端请求
def handle_client_request(ip_port, new_client):
    # 循环接收客户端消息
    while True:
        print('有新的客户端连接！客户端的端口号和ip为：', ip_port)

        # 5.接收客户端数据
        recv_data = new_client.recv(1024)

        if recv_data:  # 如果数据长度不为0
            print(f'接收数据的长度为{len(recv_data)}')
            recv_content = recv_data.decode('utf-8')
            print(f'接收到的客户端数据为:', recv_content, ip_port)

            # 6.发送数据到客户端
            send_data = '问题正在处理中....'
            # 对字符串进行编码
            send_content = send_data.encode('utf-8')
            new_client.send(send_content)
        else:  # 如果容器类型数据为空，或没有数据，表示条件不成立
            # 客户端关闭连接，下线
            print(f'客户端已下线:{ip_port}')
            break
    # 关闭服务与客户端套接字， 表示和客户端终止通信
    new_client.close()



if __name__ == '__main__':
    # 1.创建TCP服务端套接字对象
    # AF_INET表示ipv4协议, AF_INET6表示ipv6协议, socket.SOCK_STREAM表示TCP协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，表示的意思是服务端程序退出端口号立刻释放
    # SOL_SOCKET表示当前套接字
    # SO_REUSEADDR表示复用端口号选项
    # True确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号
    # 参数为一个元组
    # 元组第一个数是服务端IP地址，一般不用指定， 表示本机的任何一个IP地址即可，
    # 元组第二个数为端口号
    tcp_server_socket.bind(("", 9090))

    # 3.设置监听
    #                最大等待建立连接的个数,最多可以128人排队，使用多任务可以不用排队
    tcp_server_socket.listen(128)

    # 4.等待接收客户端的连接请求
    # 当客户端和服务端建立连接成功，返回两个数据  第一个数据是一个新的套接字，
    # 第二个数据是客户端的ip和端口, 每次返回的套接字都不一样
    # tcp_server 只负责接收客户端的连接请求，收发消息都不使用该套接字
    # 循环等待接收客户端请求
    while True:
        new_client, ip_port = tcp_server_socket.accept()  # 阻塞 直到客户端连接
        # 代码执行到此说明连接成功
        # 当客户端和服务端连接成功，创建子线程，让子线程专门负责接收客户端消息
        sub_thread = threading.Thread(target=handle_client_request,
                                      args=(ip_port, new_client))

        # 设置守护主线程，主线程退出，子线程销毁
        sub_thread.setDaemon(True)
        # 启动子线程的任务
        sub_thread.start()

    # 7.关闭套接字
    # 关闭服务端套接字， 表示服务端不再接受客户端的连接
    # tcp_server_socket.close()  可以省略，因为服务端程序需要一直运行