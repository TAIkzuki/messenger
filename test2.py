import socket
from flask import Flask, request, jsonify
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем адрес и порт, на котором будет работать сервер
server_address = ('localhost', 1757)

# Привязываем сокет к указанному адресу и порту
server_socket.bind(server_address)

# Начинаем прослушивать входящие соединения
server_socket.listen(1)

print("Сервер запущен и слушает порт 1757...")

while True:
    # Принимаем входящее соединение
    client_socket, client_address = server_socket.accept()

    print(f"Получено соединение с адреса {client_address}")

    # Обрабатываем данные
    data = client_socket.recv(1024)
    print(f"Получено: {data.decode()}")

    # Отправляем ответ обратно клиенту
    response = "Привет от сервера!"
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()

app = Flask(__name__)

@app.route('localhost', 1757)

def index():

    return "Hello, World!"

if __name__ == "__main__":

    app.run()
