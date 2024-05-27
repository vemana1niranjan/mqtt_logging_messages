import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('localhost', 9999))

while True:
    broker_message = server_socket.recv(1024).decode()
    print("Broker:", broker_message)

    message = input("Server message: ")
    server_socket.send(message.encode())
