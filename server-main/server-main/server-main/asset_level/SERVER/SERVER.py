
from socket import *
from threading import Thread

players = {

}
id_counter = 0 
server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost",1234))

server.listen(5)
server.setblocking(False)


def m():
    while True:
        for s in list(players.keys()):
            try:
                data = s.recv(1024)
                if data:
                    parts = data.decode().strip("|").split(",")
                    if len(parts) == 3:
                        x, y, name = parts
                        players[s]["x"] = int(x)
                        players[s]["y"] = int(y)
                        players[s]["name"] = name
            except:
                pass


            pocket = ""
            for key, valuer in players.items():
                    if key != com :
                        line = f" {valuer["id"]}, {valuer["x"]}, {valuer["y"]}, {valuer["rad"]}"
                        pocket +=line + "|"
            s.send(pocket.encode())
Thread(target=m).start()       
                    

            # s.close()
            # del players[s]


while True:
    try:
        com, addr = server.accept()  # Принимаем подключение
        com.setblocking(False)     # Устанавливаем неблокирующий режим
        id_counter += 1            # Увеличиваем счетчик ID
        
        # Добавляем нового игрока
        players[com] = {"id": id_counter, "x": 0, "y": 0, "r": 20, "name": None}
        com.send(f"{id_counter},0,0,20".encode())
        
    except:
        pass
    
            

                    
    