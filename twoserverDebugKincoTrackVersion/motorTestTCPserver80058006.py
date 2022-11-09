import socket
import time
# 指定协议
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 让端口可以重复使用
# 绑定ip和端口
server1.bind(('0.0.0.0', 8005))
server2.bind(('0.0.0.0', 8006))
# 监听
server1.listen(1)
server2.listen(1)
# 等待连接
print("accepting!\n")
clientsocket1, address1 = server1.accept()
clientsocket2, address2 = server2.accept()
print("accepted!\n")
# 速度模式
print('step 1' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\xFF\xFF')
time.sleep(5)
print('step 2' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
time.sleep(1)
print('step 3' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\xFF\xFF')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\x00\x00')
time.sleep(10)
print('step 4' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
time.sleep(1)
print('step 5' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\xFF\xFF')
time.sleep(5)
print('step 6' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
time.sleep(1)
print('step 7' + time.strftime("%c"))
clientsocket1.send(b'\x08\x00\x00\x01\x41\x80\x00\x00\x00\x00\x00\x00\x00')
clientsocket2.send(b'\x08\x00\x00\x01\x41\x80\x00\x00\x00\x00\x00\x00\x00')
time.sleep(1)

clientsocket1.close()
clientsocket2.close()

server1.close()
server2.close()
