import socket
import time
# 指定协议
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip和端口
# server1.bind(('192.168.1.11', 4001))
# server1.bind(('10.60.75.103', 4001))
# server1.bind(('192.168.0.110', 8003))
server1.bind(('0.0.0.0', 8003))
# 监听
server1.listen(1)
# 等待连接
print("accepting1!\n")
clientsocket1, address1 = server1.accept()
print("accepted1!\n")

# 等待连接
print("accepting3!\n")
print("accepted3!\n")
# 接收消息
# data = clientsocket1.recv(1024)
#不使能
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(0.2)
print("不使能")

#使能
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(0.2)
print("使能")

#清错
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x86\x00\x00\x00')
time.sleep(0.2)
print("清错")

#设为速度模式
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2F\x60\x60\x00\x03\x00\x00\x00')
print("设为速度模式")
time.sleep(0.2)

#设为速度为0
clientsocket1.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(0.2)
#使能
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(0.2)

#设置速度大小
clientsocket1.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x00\x04\x00\x00')
time.sleep(0.2)
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(5)

#设为速度为0
clientsocket1.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(0.2)
#使能
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(0.2)
#不使能
clientsocket1.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(0.2)
print("不使能")




# input("Press Enter to continue!\n")

clientsocket1.close()
server1.close()