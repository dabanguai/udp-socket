import random
import socket

# 创建 UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#  绑定服务器地址和端口
server_address = ("localhost",8000)
server_socket.bind(server_address)
ack_num = 0
# 假定服务器端一直接收客户端发送的数据包
while True:
    # 接收客户端发送的数据包和地址信息
    data, client_address = server_socket.recvfrom(1024)
    # 模拟随机丢包
    if random.random() < 0.3:
        continue
    # 解析序列号
    seq_num = int(data.decode().split()[2])
    ack_num = seq_num + 1
    server_socket.sendto(ack_num.to_bytes(4, byteorder='big'), client_address)
    print(f"client_address:{client_address}\nReceived:{data.decode()}")

