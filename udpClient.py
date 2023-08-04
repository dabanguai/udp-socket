import socket
import random
import time

# 创建 UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 客户端地址和端口
# client_address = ('localhost', 8888)
server_address = ('localhost', 8000)

seq_num = 0

# 等待 ACK，设置超时时间为 2 秒
client_socket.settimeout(2)

max_retry_times = 3
retry_time = 0
for i in range(10):
    # 发送数据包到服务器端
    message = f"Data packet {seq_num}"
    # 超时重传
    while retry_time < max_retry_times:
        try:
            client_socket.sendto(message.encode(), server_address)
            # 接收服务器 ack
            ack, address = client_socket.recvfrom(1024)
            ack = int.from_bytes(ack, byteorder='big')
            seq_num += 10
            # 成功
            print(f"server_Address:{address},Received ACK: {ack}")
            break
        except socket.timeout:
            print(f"Timeout: No ACK received for packet {i}. Resending...")
            retry_time += 1
            time.sleep(1)
    retry_time = 0
client_socket.close()
