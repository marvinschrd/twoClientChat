import socket
import threading

client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 63000

message = " "
messageReceived = " "

def ConnectToServer():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        threading._start_new_thread(ReceiveMessages,(client,"v"))
        print("Connected to server")
        print("Write to chat with the other client")
        while True:
            WriteMessage(client)

    except Exception as e:
        print(e)
        print("Cannot connect to host: " + HOST_ADDR + " on port: " + str(
            HOST_PORT) + " Server may be Unavailable. Try again later")


def ReceiveMessages(socket,g):
    while True:
        messageReceived = (socket.recv(4096)).decode("utf-8")
        print("\nother client say : "+ messageReceived )


def WriteMessage(client):
    message =input("You : ")
    #print("You said : " + message)
    client.send((message).encode("utf-8"))

ConnectToServer()
#WriteMessage(client)

