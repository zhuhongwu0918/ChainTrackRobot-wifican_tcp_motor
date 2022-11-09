import socket
import time

server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.bind(('192.168.0.110', 8001))
server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server1.listen(5)
clientsocket1, address1 = server1.accept()
# 速度模式
clientsocket1.send(b'\x08\x00\x00\x06\x01\x2F\x60\x60\x00\xFD\x00\x00\x00')
clientsocket1.close()
# 0rpm
clientsocket1, address1 = server1.accept()
clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x00\x00\x00')
clientsocket1.close()
# 150rpm
clientsocket1, address1 = server1.accept()
clientsocket1.send(b'\x08\x00\x00\x06\x01\x23\xFF\x60\x00\x00\x40\x06\x00')
clientsocket1.close()
# 使能
clientsocket1, address1 = server1.accept()
clientsocket1.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x0F\x00\x00\x00')
time.sleep(10)
clientsocket1.close()
# 不使能
clientsocket1, address1 = server1.accept()
clientsocket1.send(b'\x08\x00\x00\x06\x01\x2B\x40\x60\x00\x06\x00\x00\x00')
clientsocket1.close()
