import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Write IP address of Server: ')
ips = input ()
print ('Write Port of Server: ')
port = (int(input()))
sock.connect((ips, port))
print ('Write the massage you want to send: ')
ms = input()
sock.send(bytes(ms, encoding = 'UTF-8'))
sock.close()
