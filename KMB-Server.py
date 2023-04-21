import socket
import threading

# Список клиентов
clients = []

# Функция для обработки подключения новых клиентов
def handle_connection(conn, addr):
    print(f'Новый игрок подключился: {addr}')
    clients.append(conn)

    while True:
        try:
            # Получаем выбор от клиента
            data = conn.recv(1024).decode()
            if not data:
                break

            # Отправляем выбор всем остальным клиентам
            for client in clients:
                if client != conn:
                    client.send(data.encode())

            # Определяем результат игры и отправляем его всем клиентам
            choices = [c.recv(1024).decode() for c in clients]
            if len(choices) == len(clients):
                result = determine_winner(choices)
                for client in clients:
                    client.send(result.encode())

        except ConnectionResetError:
            break

    # Удаляем клиента из списка при отключении
    clients.remove(conn)
    print(f'Клиент отключился: {addr}')

# Функция для определения победителя
def determine_winner(choices):
    # Результаты игры
    results = []

    # Определяем победителя для каждой пары игроков
    for i in range(len(choices)):
        for j in range(i+1, len(choices)):
            result = determine_round_winner(choices[i], choices[j])
            results.append(result)

    # Определяем общего победителя
    player1_wins = results.count('игрок1')
    player2_wins = results.count('игрок2')
    if player1_wins > player2_wins:
        return 'игрок1 выиграл'
    elif player2_wins > player1_wins:
        return 'игрок2 выиграл'
    else:
        return 'ничья'

# Функция для определения победителя в отдельном раунде
def determine_round_winner(choice1, choice2):
    if choice1 == choice2:
        return 'ничья'
    elif choice1 == 'камень' and choice2 == 'ножницы':
        return 'игрок1'
    elif choice1 == 'ножницы' and choice2 == 'бумага':
        return 'игрок1'
    elif choice1 == 'бумага' and choice2 == 'камень':
        return 'игрок1'
    else:
        return 'игрок2'

# Создаем сокет и начинаем прослушивание порта
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.0.10', 8888))
sock.listen()

print('Сервер запущен')

# Обрабатываем подключения новых клиентов в отдельных потоках
while True:
    conn, addr = sock.accept()
    thread = threading.Thread(target=handle_connection, args=(conn, addr))
    thread.start()