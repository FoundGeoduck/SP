import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 8888)

# Подключаемся к серверу
client_socket.connect(server_address)

# Получаем сообщение о начале игры
start_message = client_socket.recv(1024).decode()
print(start_message)

# Запрашиваем выбор камня, ножниц или бумаги у игрока
while True:
    choice = input('Сделайте свой выбор (камень/ножницы/бумага): ')

    # Отправляем выбор серверу
    client_socket.sendall(choice.encode())

    # Получаем результаты игры от сервера
    result_message = client_socket.recv(1024).decode()
    print(result_message)

    # Если есть победитель, выходим из цикла
    if 'Победил: Игрок' in result_message or 'Победил: Никто' in result_message:
        break

# Закрываем соединение с сервером
client_socket.close()
