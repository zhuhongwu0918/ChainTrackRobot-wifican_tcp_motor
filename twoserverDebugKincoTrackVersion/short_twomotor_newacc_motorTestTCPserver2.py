import socket
import time
# 让端口可以重复使用
# server3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 指定协议
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.bind(('192.168.0.110', 8001))
# 监听1
server1.listen(1)
# 等待连接1
print("accepting1\n")
clientsocket1, address1 = server1.accept()
print("accepted1!\n")

server3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server3.bind(('192.168.0.110', 8003))

# 监听3
server3.listen(1)
# 等待连接3
print("accepting3!\n")
clientsocket3, address = server3.accept()
print("accepted3!\n")

# 使能
clientsocket1.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
clientsocket3.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(10)
clientsocket1.close()
clientsocket3.close()



# 不使能
clientsocket1, address1 = server1.accept()
print("new accept1!\n")
clientsocket3, address = server3.accept()
print("new accept3!\n")
clientsocket3.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(0.5)
clientsocket1.close()
clientsocket3.close()


clientsocket3.close()
server3.close()