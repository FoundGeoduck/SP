import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Write IP address of Client, IP: ')
ipc = input()
print ('Write port of Client ')
port = (int(input()))
sock.bind((ipc, port))
print ('Server is running, please, press ctrl+c to stop')
while True:
	conn,addr = sock.accept()
	print ('connected: ', addr)
	data = conn.recv(1024)
	print (str(data))
conn.close()
