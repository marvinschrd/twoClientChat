
import socket
import threading

HOST_ADDR = "127.0.0.1"
HOST_PORT = 63000
client_name = " "
clients = []
clients_names = []


client1Data = " "
client2Data = " "





def StartServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)
    print("SERVER STARTED")
    while True:
        if len(clients) < 2:
            print("WAITING FOR CLIENT")
            client, addr = server.accept()
            clients.append(client)
            threading._start_new_thread(ReceiveClientMessage,(client,addr))
            print("CLIENT ACCEPTED")
       
    

def AcceptClients(server, a):
    while True:
        if len(clients) < 2:
            client, addr = server.accept()
            print("WAITING FOR CLIENT")
            clients.append(client)
            threading._start_new_thread(ReceiveClientMessage(clients,addr))
            print("CLIENT ACCEPTED" + client + " " + addr )

def ReceiveClientMessage(connectedClient, clientAddress):
    while True:
        data = (connectedClient.recv(4096)).decode("utf-8")
        if connectedClient == clients[0]:
            client1Data = data
            print("client1 said " + data)
            clients[1].send((data.encode("utf-8")))
        else:
            client2Data = data
            print("client2 said " + data)
            clients[0].send((data.encode("utf-8")))

def SendMessage(clientToSend,dataToSend):
    clientToSend.send((dataToSend).encode("utf-8"))

StartServer()
