
from socket import *
players = {

}

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost",2118))

server.listen(5)
server.setblocking(False)

while True:
    try:
        connect, ip = server.accept()
        connect.setblocking(False)
        print("working", ip)
        players[connect] =  {
            "id":id,
            "x":0,
            "y":0,
            "radius":20,
            "name": None
        }
        connect.send f"players{"id"}), f"players{"x"}, f"players{"y"}), f"players{"radius"}.encode())
        id +=1
    except:
        pass