import threading
import socket
def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 57777))
    serv.listen(2)
    client_socket, client_adress = serv.accept() # Ne-am conectat la client
    mesaj = "Buna ziua! Aveti o urgenta medicala?"
    print (f'Robot: ' + mesaj)
    client_socket.send(mesaj.encode()) # Am trimis clientului primul mesaj
    data = client_socket.recv(2048)
    answer = data.decode() # Primim raspuns de la client
    if answer == "Da":
        print (f'Pacient: ' + answer)
        mesaj = "Numarul dvs. de telefonul a salvat. " \
                "O sa va contacteze un operator cat de devreme posibil."
        print (f'Server: ' + mesaj)
        client_socket.send(mesaj.encode())
        print (f'Conexiune inchisa.')
        client_socket.close() # Serverul inchide conexiunea cu clientul
        serv.close() # Serverul se inchide
    else:
        if answer == "Nu":
            mesaj = "Selectati specializarea dorita:" \
                  "Chirurgie. Parontologie."
            print (f'Robot: ' + mesaj)
            client_socket.send(mesaj.encode())
            data = client_socket.recv(2048)
            answer = data.decode()
            match answer:
                case "Chirurgie":
                    mesaj = "Doctorul se intoarce din concediu in data de 12.12.2023." \
                            " Reveniti cu un apel in data respectiva. Conexiune inchisa."
                    print(f'Robot: ' + mesaj)
                    client_socket.send(mesaj.encode())
                    client_socket.close()
                    serv.close()
                case "Parontologie":
                    mesaj = "Multumim pentru precizare. Va rog sa va introduceti numarul de telefon."
                    print(f'Robot: ' + mesaj)
                    client_socket.send(mesaj.encode())
                    data = client_socket.recv(2048)
                    answer = data.decode()
                    mesaj = "O sa fiti contactat de un operator cat de repede. O zi buna!"
                    print(f'Robot: ' + mesaj)
                    client_socket.send(mesaj.encode())
                    print(f'Conexiune inchisa.')
                    client_socket.close()
        else:
            mesaj = "Raspuns invalid. Conexiune inchisa."
            print(f'Robot: ' + mesaj)
            client_socket.send(mesaj.encode())
            client_socket.close()
            serv.close()
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 57777))
    data = client_socket.recv(2048)
    mesaj = data.decode() # Clientul a primit mesajul de la server
    print(f' \n Pacient: Nu')
    client_socket.send("Nu".encode())
    mesaj = data.decode()
    print(f' \n Pacient: Parontologie')
    client_socket.send("Parontologie".encode())
    mesaj = data.decode()
    print(f' \n Pacient: 0755666777')
    client_socket.send("0755666777".encode())
    client_socket.close() # Clientul inchide conexiunea

server_thr = threading.Thread(target=server)
client_thr = threading.Thread(target=client)
server_thr.start()
client_thr.start()
server_thr.join()
client_thr.join()

