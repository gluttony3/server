from random import randint
import pygame
from socket import *
from threading import Thread

# подключаемся к серверу
client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 1234))
ac = client.recv(64).decode()
print(ac)

pygame.init()  # запускаем модули pygame
wind = pygame.display.set_mode((1000, 700))  # окно игры
clock = pygame.time.Clock()  # часы для управления кадрами в секунду

class Ball:  # класс шарики 
    def __init__(self , x, y, color, radius):  # конструктор параметров
        self.x = x  # сохраняем координаты шарика
        self.y = y  # сохраняем координаты шарика
        self.radius = radius  # сохраняем радиус
        self.color = color  # сохраняем цвет
        self.speed_x = 5  # устанавливаем скорость по горизонтали
        self.speed_y = 5  # устанавливаем скорость по вертикали
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.name = "PLAYER"  # имя по умолчанию

    def draww(self):  # рисует круг
        pygame.draw.circle(wind, self.color, (self.rect.x, self.rect.y), self.radius)
        if self.color == (0, 200, 100): 
            font = pygame.font.Font("OpenSans-Bold.ttf", 30)
            text = font.render(self.name, True, (255, 255, 255)) # создаем текст с именем игрока на поверхности
            wind.blit(text, (self.rect.x - 50, self.rect.y - 20))  # рисуем имя над игроком

dat = ac.split(",") # розбиваем строку с данными
my_id = int(dat[0]) # применяем int и сохраняем в переменные
my_x = int(dat[1])
my_y = int(dat[2])
my_rad = int(dat[3])

enemies = []
def priem():
    global enemies
    while True:
        try:
            data1 = client.recv(1024)  # получаем данные от сервера
            o = data1.decode().strip("|").split("|")  # декодируем и убираем лишние символы
            print(o) # виводим

            enemies = []
            for elementa in o:  # перебираємо кожен пакет ворога
                    dataenemies = elementa.split(",")  # розбиваємо рядок по частинах
                    if len(dataenemies) == 5:  
                        id_e = int(dataenemies[0])
                        x_e = int(dataenemies[1])
                        y_e = int(dataenemies[2])
                        r_e = int(dataenemies[3])
                        name_e = dataenemies[4]
                        enemies.append([id_e, x_e, y_e, r_e, name_e])  # додаємо в список

                    print(enemies)  # виводимо список ворогів

        
        except:
            pass
Thread(target=priem).start()       

# создаём еду
eats = []
for _ in range(3000):
    b = Ball(randint(-2000, 2000), randint(-2000, 2000),
             (randint(0,255), randint(0,255), randint(0,255)),
             randint(0,50))
    eats.append(b)

# создаем мяч игрока
ball = Ball(500, 350, (0, 200, 100), 50)

# ввод имени игрока
font = pygame.font.Font("OpenSans-Bold.ttf", 40)
input_rect = pygame.Rect(400, 20, 200, 40)  # поле для ввода текста
color_active = pygame.Color('lightskyblue3')
name_user = ""
game = True
input_active = True  # активный режим ввода

# вводим имя
while input_active:
    wind.fill((122, 230, 50))  # фон

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # удаляем символ
                name_user = name_user[:-1]
            elif event.key == pygame.K_RETURN:  # подтверждаем имя
                if name_user.strip() != "":
                    ball.name = name_user
                    input_active = False
            else:  
                name_user += event.unicode
        if event.type == pygame.QUIT:
            input_active = False
            game = False


    

    # рисуем поле ввода и текст
    pygame.draw.rect(wind, color_active, input_rect, border_radius=10)
    name_surface = font.render(name_user, True, (0, 0, 0))
    wind.blit(name_surface, (input_rect.x + 10, input_rect.y + 5))

    pygame.display.update()  # обновляем экран
    clock.tick(60)  # ограничиваем FPS

# основной игровой цикл
while game:
    wind.fill((122, 230, 50))  # фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события для закрытия окна
            game = False
    

    # движение игрока — двигаем фон (еду) игрок стоит на месте
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        for b in eats:
            b.rect.x -= 5
        my_x += 5
    if keys[pygame.K_LEFT]:
        for b in eats:
            b.rect.x += 5
        my_x -= 5
    if keys[pygame.K_DOWN]:
        for b in eats:
            b.rect.y -= 5
        my_y += 5
    if keys[pygame.K_UP]:
        for b in eats:
            b.rect.y += 5
        my_y -= 5
    
    try:
        client.send(f"{my_x},{my_y},{ball.name}".encode())
    except:
        pass

    for i in eats:
        i.draww()  # отрисовка еды

    ball.draww()  # отрисовка игрока

    # отрисовка врагов
    for enemy in enemies:
         if enemy[0] != my_id:  # исключаем самого себя
            pygame.draw.circle(wind, (255, 0, 0), (enemy[1], enemy[2]), enemy[3])
            font = pygame.font.Font("OpenSans-Bold.ttf", 20)
            text = font.render(enemy[4], True, (0, 0, 0))
            wind.blit(text, (enemy[1] - 30, enemy[2] - enemy[3] - 10))

    pygame.display.update()  # обновляем экран чтобы все отрисовалось
    clock.tick(60)  # ограничиваем кадры в секунду
