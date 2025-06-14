from random import randint
import pygame
from socket import*
pygame.init() # запускаем модули pygame
wind = pygame.display.set_mode((1000, 700)) # окно игри
clock = pygame.time.Clock() # часи для управления кадрами в секунду

class Ball: # клас шарики 
    def __init__(self , x, y, color, radius): # конструктор параметри
        self.x = x # сохраняем координати шарика
        self.y = y # сохраняем координати шарика
        self.radius = radius # сохраняем радиус
        self.color = color # сохраняем цвет
        self.speed_x = 5 # устанавливаем скорость по горизонтали
        self.speed_y = 5 # устанавливаем скорость по вертикали
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
    def draww(self): # рисует круг
        pygame.draw.circle(wind, self.color, (self.rect.x, self.rect.y), self.radius)
        if self.color == (0, 200, 100): 
            font = pygame.font.Font("OpenSans-Bold.ttf", 30)
            text = font.render("PLAYER", True, (255, 255, 255))
            wind.blit(text, (self.rect.x - 50, self.rect.y - 20))

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 2118))
eats = []
for _ in range(3000):
    b = Ball(randint(-2000,2000), randint(-2000,2000),(randint(0,255),randint(0,255),randint(0,255)),randint(0,50))
    eats.append(b)

ball = Ball(500, 350 ,(0,200,100), 50) # создаем мяч 
wind.fill((122,230,50))

game = True

while game:
    wind.fill((122,230,50))
  # обработка собития для закрития окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_RIGHT]:
        for b in eats:
            b.rect.x -= 5
    if keys [pygame.K_LEFT]:
        for b in eats:
            b.rect.x += 5
    if keys [pygame.K_DOWN]:
        for b in eats:
            b.rect.y -= 5
    if keys [pygame.K_UP]:
        for b in eats:
            b.rect.y += 5
                    
    for i in eats:
        i.draww()

    ball.draww()

    pygame.display.update() # обновляем екран чтоби все отрисовалось
    clock.tick(60) # ограничиваем кадри в секунду