
from socket import *
players = {

}

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost",2118))

server.listen(5)
server.setblocking(False)

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