import socket
if __name__ == '__main__':
    # 1.创建TCP服务端套接字对象
    # AF_INET表示ipv4协议, AF_INET6表示ipv6协议, socket.SOCK_STREAM表示TCP协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，表示的意思是服务端程序退出端口号立刻释放
    # SOL_SOCKET表示当前套接字
    # SO_REUSEADDR表示复用端口号选项
    # True确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号, 方便客户端连接
    # 参数为一个元组
    # 元组第一个数是服务端IP地址，一般不用指定， 表示本机的任何一个IP地址即可，
    # 元组第二个数为端口号
    tcp_server_socket.bind(("", 8080))

    # 3.设置监听
    #                最大等待建立连接的个数,最多可以128人排队，使用多任务可以不用排队
    tcp_server_socket.listen(128)

    # 4.等待接收客户端的连接请求
    # 当客户端和服务端建立连接成功，返回一个元组
    # 第一个数据是一个新的套接字, 每次返回的套接字都不一样
    # 第二个数据是客户端的ip和端口
    # tcp_server 只负责接收客户端的连接请求，收发消息都不使用该套接字
    new_client, ip_port = tcp_server_socket.accept()  # 阻塞 直到客户端连接
    # 代码执行到此说明连接成功
    print('客户端的端口号和ip为：', ip_port)

    # 5.接收客户端数据
    recv_data = new_client.recv(1024)
    recv_content = recv_data.decode('utf-8')
    print(f'接收到的客户端数据为:', recv_content)

    # 6.发送数据到客户端
    send_data = '问题正在处理中....'
    # 对字符串进行编码
    send_content = send_data.encode('utf-8')
    new_client.send(send_content)
    # 关闭服务与客户端套接字， 表示和客户端终止通信
    new_client.close()

    # 7.关闭套接字
    # 关闭服务端套接字， 表示服务端不再接受客户端的连接
    tcp_server_socket.close()