
from socket import *
from threading import Thread
players = {
 
}

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost",2118))

server.listen(5)
server.setblocking(False)

def peredacha():
    for connect in list(players):
        try:
            daty = connect.recv(1024).decode()
            print(daty)
        except:
            pass

