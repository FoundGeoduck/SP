import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Ожидаем подключения клиентов
server_socket.listen(2)
print('Ждём игроков...')

# Список игроков в лобби
lobby_players = []

# Функция для обработки игры между двумя игроками
def play_game(player1, player2):
    # Отправляем сообщение о начале игры обоим игрокам
    player1.sendall(b'Starting game...')
    player2.sendall(b'Starting game...')

    while True:
        # Получаем выбор первого игрока
        player1_choice = player1.recv(1024).decode()

        # Получаем выбор второго игрока
        player2_choice = player2.recv(1024).decode()

        # Определяем победителя
        if player1_choice == 'камень' and player2_choice == 'ножницы':
            winner = 'Игрок 1'
        elif player1_choice == 'ножницы' and player2_choice == 'бумага':
            winner = 'Игрок 1'
        elif player1_choice == 'бумага' and player2_choice == 'камень':
            winner = 'Игрок 1'
        elif player2_choice == 'камень' and player1_choice == 'ножницы':
            winner = 'Игрок 2'
        elif player2_choice == 'ножницы' and player1_choice == 'бумага':
            winner = 'Игрок 2'
        elif player2_choice == 'бумага' and player1_choice == 'камень':
            winner = 'Игрок 2'
        else:
            winner = 'Никто'

        # Отправляем результаты игры обоим игрокам
        player1.sendall(('Победил: ' + winner).encode())
        player2.sendall(('Победил: ' + winner).encode())

        # Если есть победитель, выходим из цикла
        if winner != 'Никто':
            break

    # Закрываем соединение с игроками
    player1.close()
    player2.close()

# Бесконечный цикл для ожидания подключений клиентов
while True:
    # Принимаем подключение нового клиента
    client_socket, client_address = server_socket.accept()

    # Добавляем игрока в лобби
    lobby_players.append(client_socket)

    # Если в лобби уже два игрока, начинаем игру между ними
    if len(lobby_players) == 2:
        # Получаем двух игроков из лобби и удаляем их из списка
        player1 = lobby_players.pop(0)
        player2 = lobby_players.pop(0)

        # Запускаем игру между двумя игроками
        play_game(player1, player2)
