import socket
import time
# 指定协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
server.bind(('0.0.0.0', 8003))
# 监听
server.listen(1)
# 等待连接
print("accepting!\n")
clientsocket, address= server.accept()
print("accepted!\n")
# 速度模式
for i in range(10):
    print('step 1:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x80\xFF\xFF')
    time.sleep(5)
    print('step 2:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(1)
    print('step 3:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\xFF\xFF')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x80\x00\x00')
    time.sleep(10)
    print('step 4:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(1)
    print('step 5:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x80\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x80\xFF\xFF')
    time.sleep(5)
    print('step 6:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\xA2\x00\x00\x00\x00\x00\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\xA2\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(1)
    print('step 7:' + time.strftime("%c"))
    clientsocket.send(b'\x08\x00\x00\x01\x41\x80\x00\x00\x00\x00\x00\x00\x00')
    clientsocket.send(b'\x08\x00\x00\x01\x42\x80\x00\x00\x00\x00\x00\x00\x00')
    time.sleep(1)
    input('Please press Enter!\n')

clientsocket.close()

server.close()
