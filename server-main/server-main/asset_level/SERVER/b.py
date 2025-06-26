from socket import socket, AF_INET, SOCK_STREAM
players = {}

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost",1234))

server.listen(5)

server.setblocking(False)
id_counter = 0
print("working...")


while True:
    try:
        conn , addr = server.accept()  # Принимаем подключение
        conn.setblocking(False)     # Устанавливаем неблокирующий режим
        print("подключился клиент->" , addr)
        id_counter += 1            # Увеличиваем счетчик ID
        
     
        
        players[conn] = {'id': id_counter, 'x': 0, 'y': 0, 'r': 20, 'name': None}
       
        conn.send(f"{id_counter},0,0,20".encode())
        
    except:
        pass
