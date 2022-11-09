import socket
import time
# 让端口可以重复使用
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 指定协议
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.bind(('192.168.0.110', 8001))
# 监听1
server1.listen(1)
# 等待连接
print("accepting1\n")
clientsocket1, address1 = server1.accept()
print("accepted1!\n")

# 指定协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.110', 8003))

# 监听
server.listen(1)
# 等待连接
print("accepting3!\n")
clientsocket, address = server.accept()
print("accepted3!\n")

# 速度模式
clientsocket1.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
clientsocket.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
time.sleep(0.5)
print("速度 send!\n")
clientsocket1.close()
clientsocket.close()


# 0rpm
server1.listen(1)
clientsocket1, address1 = server1.accept()
print("new accept1!\n")
server.listen(1)
clientsocket, address = server.accept()
print("new accept3!\n")
clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
clientsocket.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(0.5)
clientsocket1.close()
clientsocket.close()

# 150rpm
clientsocket1, address1 = server1.accept()
print("new accept1!\n")
clientsocket, address = server.accept()
print("new accept3!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
time.sleep(0.5)
clientsocket1.close()
clientsocket.close()

# 使能
clientsocket1, address1 = server1.accept()
print("new accept1!\n")
clientsocket, address = server.accept()
print("new accept3!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(10)
clientsocket1.close()
clientsocket.close()
# 不使能
clientsocket1, address1 = server1.accept()
print("new accept1!\n")
clientsocket, address = server.accept()
print("new accept3!\n")
clientsocket.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(0.5)
clientsocket1.close()
clientsocket.close()


clientsocket.close()
server.close()