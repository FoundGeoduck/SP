import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
print ('Write IP of Server, ip =')
ips = input ()
print ('Wtite port of Server')
port = (int(input ()))
sock.connect((ips, port))  # подключемся к серверному сокету
print ('Write the massage you need to send')
ms = input ()
sock.send(bytes(ms,encoding = 'UTF-8'))  # отправляем сообщение
#data = sock.recv(1024)  # читаем ответ от серверного сокета
sock.close()  # закрываем соединение
#print(data)
