import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening for connections...")

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            break
        print(f"Client: {message}")
        response = input("You: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
