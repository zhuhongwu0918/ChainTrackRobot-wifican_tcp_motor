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
server.bind(('0.0.0.0', 8001))
# 监听
server.listen(1)
# 等待连接
print("accepting!\n")
clientsocket, address = server.accept()
print("accepted!\n")
# 接收消息
# data = clientsocket.recv(1024)
#不使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(1)
print("不使能")

#使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(1)
print("使能")

#清错
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x86\x00\x00\x00')
time.sleep(1)
print("清错")

#设为速度模式
clientsocket.send(b'\x08\x00\x00\x06\x05\x2F\x60\x60\x00\x03\x00\x00\x00')
print("设为速度模式")
time.sleep(1)


#设为速度为0
clientsocket.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(1)
#使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
print("设速度为0并使能")
time.sleep(1)


#设置速度大小
clientsocket.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x22\x01\x00\x00')
time.sleep(1)
#使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
print("设置速度大小并使能")
time.sleep(8)



#设为速度为0
clientsocket.send(b'\x08\x00\x00\x06\x05\x23\xFF\x60\x00\x00\x00\x00\x00')
time.sleep(1)
#使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x0F\x00\x00\x00')
print("设速度为0并使能")
time.sleep(1)


#不使能
clientsocket.send(b'\x08\x00\x00\x06\x05\x2B\x40\x60\x00\x06\x00\x00\x00')
time.sleep(1)
print("不使能")


# input("Press Enter to continue!\n")
clientsocket.close()
server.close()