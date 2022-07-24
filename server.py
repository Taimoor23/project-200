from ipaddress import ip_address
from os import remove
import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
server.bind((ip_address,port))
server.listen()
clients=[]
nicknames=[]
print("The server is running...")

def clientsThread(conn,addr):
    conn.send("welcome to this CHAT ROOM".encode('utf-8'))
    while True:
        try:
            message=conn.recv(2048).decode('utf-8')
            if (message):
                print(message)
                broadcast(message,conn)
            else:
                remove(conn)
                remove(remove_nickname)
        except:
            continue
def broadcast(message,conn):
    for client in clients:
        if (clients!=conn):
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove(client)
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
def remove(conn):
    if (conn in clients):
        clients.remove(conn)
while True:
    conn,addr=server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname=conn.recv(2048).decode('utf-8')
    clients.append(conn)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message,conn)

    new_thread=Thread(target=clientsThread,args=(conn,nickname))
    new_thread.start()

