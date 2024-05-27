import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

while True:
    message = input("Client message: ")
    client_socket.send(message.encode())

    broker_message = client_socket.recv(1024).decode()
    print("Broker:", broker_message)
