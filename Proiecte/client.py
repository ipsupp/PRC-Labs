import socket
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('0.0.0.0', 57777))
    data = client_socket.recv(2048)
    mesaj = data.decode()
    print("serverul transmite:" + mesaj)
    client_socket.send("received.".encode())
    client_socket.close()

