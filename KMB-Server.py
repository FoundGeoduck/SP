import socket
import threading

# список подключенных клиентов
clients = []

# функция для обработки соединения с клиентом
def handle_client(client_socket, client_address):
    print(f"Подключился клиент {client_address}")
    # добавление клиента в список подключенных клиентов
    clients.append(client_socket)

    # игровой цикл для клиента
    while True:
        # получение выбора от клиента
        choice = client_socket.recv(1024).decode()
        # передача выбора другим клиентам
        for c in clients:
            if c != client_socket:
                c.send(f"Игрок {client_address[1]} выбрал {choice}".encode())

        # проверка, все ли клиенты сделали выбор
        all_choices = [c.recv(1024).decode() for c in clients]
        if "" in all_choices:
            continue

        # определение результата игры
        if len(set(all_choices)) == 1:
            result = "Ничья!"
        elif set(all_choices) == {"камень", "ножницы"} or set(all_choices) == {"ножницы", "бумага"} or set(all_choices) == {"бумага", "камень"}:
            result = "Выиграли все!"
        else:
            result = "Выиграли: "
            winners = []
            for i, c in enumerate(clients):
                if all_choices[i] == max(all_choices):
                    winners.append(str(client_address[1]))
            result += ", ".join(winners)

        # отправка результата клиентам
        for c in clients:
            c.send(result.encode())

        # очистка выборов
        for c in clients:
            c.send("".encode())

    # удаление клиента из списка подключенных клиентов
    clients.remove(client_socket)
    # закрытие соединения с клиентом
    client_socket.close()

# установка соединения
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.10', 8888))
server_socket.listen(5)

# игровой цикл
while True:
    # ожидание подключения клиента
    client_socket, client_address = server_socket.accept()
    # запуск нового потока для обработки соединения с клиентом
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

# закрытие серверного сокета
server_socket.close()