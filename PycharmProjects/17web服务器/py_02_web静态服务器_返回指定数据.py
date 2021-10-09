# 返回固定数据

import socket

if __name__ == '__main__':              # ipv4              TCP
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用， 程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(('', 8000))

    # 设置监听
    tcp_server_socket.listen(128)

    # 等待客户端连接请求

    # 循环等待客户端的连接请求
    while True:
        print('等待客户端连接')
        new_socket, ip_port = tcp_server_socket.accept()
        print(f'客户端连接！')
        # 代码执行到此说明成功建立连接

        # 接收客户端信息
        recv_data = new_socket.recv(4096)  # 浏览器一次性不会发送太大数据，一般4096就够用
        recv_content = recv_data.decode()
        print(f'用户请求为：{recv_content}')

        # 打开文件， 读取文件中的数据
        # 用with open文件就不用close了，系统会自动完成
        with open("static/index.html", "r") as file:  # 这里的file表示文件对象
            file_data = file.read()

        # !!把数据封装成http相应报文格式的数据！否则浏览器不能识别
        # 相应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 相应头
        response_header = "Server: PWB/1.0\r\n"   # 服务器是PWS/1.0
        # 空行
        # 相应体
        response_body = file_data

        response = response_line + response_line + "\r\n" + response_body

        response_data = response.encode("utf-8")

        # 发送给浏览器的相应报文数据
        new_socket.send(response_data)

        # 关闭服务器与浏览器的套接字
        new_socket.close()
