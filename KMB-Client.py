import socket
import time

# установка соединения с сервером
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.10', 8888))

# оповещение о подключении
print('Вы успешно подключились к серверу!')

# установка времени на принятие решения
decision_time = 10  # время в секундах
start_time = time.time()

# получаем список игроков в лобби
lobby_size = int(client_socket.recv(1024).decode())
print(f'В лобби {lobby_size} игроков:')
lobby_players = []
for i in range(lobby_size):
    player = client_socket.recv(1024).decode()
    print(player)
    lobby_players.append(player)

# выбираем игрока для подключения
while True:
    # проверяем, не истекло ли время на принятие решения
    if time.time() - start_time > decision_time:
        print('Время на выбор игрока истекло.')
        player_choice = 'выход'
        break

    player_choice = input(
        f'Введите имя игрока, к которому хотите подключиться (или "все" для случайного подбора). Осталось времени: {int(decision_time - (time.time() - start_time))} секунд. ')
    if player_choice == client_socket.getsockname()[0]:
        print('Нельзя выбрать самого себя.')
    elif player_choice == 'все':
        break
    elif player_choice not in lobby_players:
        print('Игрок не найден в лобби.')
    else:
        break

# игровой цикл
while True:
    # ввод выбора
    choice = input("Введите камень, ножницы или бумагу (или 'выход' для завершения игры): ")
    if choice == 'выход':
        break
    # отправка выбора на сервер
    client_socket.send(choice.encode())
    # получение результата от сервера
    result = client_socket.recv(1024).decode()
    # вывод результата
    print(result)

# закрытие соединения
client_socket.close()