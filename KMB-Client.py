import socket
import threading

# Функция для отправки сообщений на сервер
def send_message(sock):
    while True:
        message = input()
        sock.send(message.encode())

# Функция для получения сообщений от сервера
def receive_message(sock):
    while True:
        message = sock.recv(1024).decode()
        print(message)

# Создаем сокет и подключаемся к серверу
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.10', 8888))

# Запускаем потоки для отправки и получения сообщений
send_thread = threading.Thread(target=send_message, args=(sock,))
receive_thread = threading.Thread(target=receive_message, args=(sock,))
send_thread.start()
receive_thread.start()
