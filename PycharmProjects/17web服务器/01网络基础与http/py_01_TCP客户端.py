# 1.创建tcp客户端套接字

import socket

if __name__ == '__main__':
    # AF_INET表示ipv4协议, socket.SOCK_STREAM表示TCP协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.和服务端套接字建立连接    # 服务端地址        端口号
    tcp_client_socket.connect(("192.168.98.204", 8080))

    # 3.准备数据，并将数据转成二进制
    send_content = '你好，我是客户端'
    send_data = send_content.encode('utf -8')  # 对字符串进程编码成为二进制数据

    # 4.发送数据到服务端
    tcp_client_socket.send(send_data)
    # 5.接受服务端数据
    recv_data = tcp_client_socket.recv(1024)  # 1024表示每次接收的最大字节数
    # 对二进制数据进行转换
    recv_content = recv_data.decode('gbk')
    print(f'接收到的数据为:', recv_content)
    #
    tcp_client_socket.close()
