import threading
# bibloteca care imi permite sa rulez serverul si clientul
# in acelasi timp pentru o simulare mai realista
import socket

def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 57777))
    serv.listen(2)
    client_socket, client_adress = serv.accept()
    client_socket.send(f"received?".encode())

    data = client_socket.recv(2048)
    answer = data.decode()

    if answer == "received":
        print("received.")
    else:
        print("failed.")

    client_socket.close()
    serv.close()

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 57777))
    data = client_socket.recv(2048)
    mesaj = data.decode()
    print("serverul transmite: " + mesaj)
    client_socket.send("received".encode())
    client_socket.close()


#main


server_thr = threading.Thread(target=server)
client_thr = threading.Thread(target=client)

server_thr.start()
client_thr.start()

server_thr.join()
client_thr.join()

# import socket
#
# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('0.0.0.0', 57777))
# serv.listen(2)
# # serverul asteapta conexiuni
#
# client_socket, client_adress = serv.accept()
# # serverul se conecteaza la un client
#
# client_socket.send(f"received?".encode())
# # serverul trimite mesaj clientului
#
# response = serv.recv(2048).decode()
# # clientul primeste mesaj de la serveer
#
# serv.send("received".encode())
# # clientul trimite mesaj catre server
#
# data = client_socket.recv(2048)
# answer = data.decode()
# # serverul primeste mesaj de la client
