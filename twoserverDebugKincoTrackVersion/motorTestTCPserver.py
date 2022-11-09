import socket
import time
# 指定协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 让端口可以重复使用
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip和端口
# server.bind(('192.168.1.11', 4001))
# server.bind(('10.60.75.103', 4001))
server.bind(('192.168.0.110', 8003))
# 监听
server.listen(1)
# 等待连接
clientsocket, address = server.accept()
# 接收消息
# data = clientsocket.recv(1024)






clientsocket.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(1)



clientsocket.close()
server.close()