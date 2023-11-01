import socket
def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 57777))
    serv.listen(2)
    client_socket, client_adress = serv.accept()
    client_socket.send(f"received?".encode())

    data = client_socket.recv(2048)
    answer = data.decode()

    if answer == "received.":
        print("successful")
    else:
        print("unsuccessful")

    client_socket.close()
    serv.close()