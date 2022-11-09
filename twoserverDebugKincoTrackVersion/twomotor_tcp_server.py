import socket
import time

# 指定协议
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server1.bind(('192.168.0.110', 8001))
#server3.bind(('192.168.0.110', 8003))

#server1.bind(('192.168.0.100', 8001))
#server3.bind(('192.168.0.100', 8003))

server1.bind(('0.0.0.0', 8001))
server3.bind(('0.0.0.0', 8003))
# 监听1
server1.listen(5)
server3.listen(5)

# 等待连接
print("accepting1\n")
clientsocket1, address1 = server1.accept()
print("accepting3!\n")
clientsocket3, address3 = server3.accept()
print("Two connected!\n")

# 速度模式
for i in range(10):
    server3.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
    time.sleep(0.1)
    server1.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
    time.sleep(0.1)
    # clientsocket1.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
    # clientsocket3.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
    print("速度模式 sent!\n")

# # 0rpm
# for i in range(10):
#     clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
#     time.sleep(0.1)
#     clientsocket3.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
#     print("0rpm sent!\n")


# # 150rpm
# for i in range(10):
#     clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
#     time.sleep(0.1)
#     clientsocket3.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
#     print("150rpm sent!\n")

# # 150rpm
# for i in range(10):
#     clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
#     time.sleep(0.1)
#     clientsocket3.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
#     print("150rpm sent!\n")

# # 不使能
# for i in range(10):
#     clientsocket1.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
#     time.sleep(0.1)
#     clientsocket3.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
#     print("不使能 sent!\n")


clientsocket1.close()
clientsocket3.close()
server1.close()
server3.close()