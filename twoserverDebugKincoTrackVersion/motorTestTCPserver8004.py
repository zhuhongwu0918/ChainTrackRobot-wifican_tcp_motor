import socket
import time
# 指定协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 让端口可以重复使用
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip和端口
# server.bind(('192.168.1.11', 4001))
# server.bind(('10.60.75.103', 4001))
# server.bind(('192.168.0.110', 8003))
server.bind(('0.0.0.0', 8004))
# 监听
server.listen(1)
# 等待连接
print("accepting!\n")
clientsocket, address = server.accept()
print("accepted!\n")
# 接收消息
# data = clientsocket.recv(1024)

# 速度模式
clientsocket.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
time.sleep(0.5)
# 0rpm
#clientsocket, address = server.accept()
#print("new accept!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(0.5)
# 150rpm
#clientsocket, address = server.accept()
# print("new accept!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
time.sleep(0.5)

# 使能
#clientsocket, address = server.accept()
#print("new accept!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(10)
# 不使能
#clientsocket, address = server.accept()
#print("new accept!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(0.5)


clientsocket.close()
server.close()