import socket
import threading

def handle_client_request(new_client_socket, ip, port):
    print(f'客户端已连接！ ip= {ip}， port = {port}')
    while True:
        recv_data = new_client_socket.recv(1024)

        if recv_data:
            recv_content = recv_data.decode('utf-8')
            print(f'接收到来自客户端的消息：{recv_content}， ip：{ip}')
            send_data = '服务端收到\n'
            send_content = send_data.encode('utf-8')
            new_client_socket.send(send_content)
        else:
            print(f'客户端{ip}断开连接！')
            break

    new_client_socket.close()

if __name__ == '__main__':
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 8080))

    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        ip, port = ip_port
        sub_thread = threading.Thread(target=handle_client_request,
                                      args=(new_client_socket, ip, port))
        sub_thread.setDaemon(True)
        sub_thread.start()



