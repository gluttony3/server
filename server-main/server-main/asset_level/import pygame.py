import pygame
pygame.init() # запускаем модули pygame
wind = pygame.display.set_mode((1000, 700)) # окно игри
clock = pygame.time.Clock() # часи для управления кадрами в секунду

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width # метод ширина
        self.height = height # метод длина
        self.color = color # метод цвет
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw2(self):
        pygame.draw.rect(wind, self.color, self.rect)

with open("r.txt", "r") as file: # откриваем файл, считиваем 
    data = file.readlines() # сохраняем

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

    def go(self): # движение шара
        self.x += self.speed_x
        self.rect.x = self.x
        self.y += self.speed_y
        self.rect.y = self.y
        if self.y > 670: # движение с учетом скорости
            self.speed_y *= -1
        if self.x > 970: # движение с учетом скорости
            self.speed_x *= -1
        if self.y < 0:
            self.speed_y *= -1
        if self.x < 0:
            self.speed_x *= -1



ball = Ball(200, 200 ,(0,200,100), 20) # создаем мяч 
CR2 = Ball(50, 150 ,(255,255,255), 20) # создаем мяч
platforma = Block(500,550 ,120,20 ,(255,80,60))

# Создаём блоки один раз, до цикла
blocks = []
for i, stroka in enumerate(data):
    for index , element in enumerate(stroka):
        if element == "#":
            block = Block(index*100, i*100, 50, 50, (121,77,62))
            blocks.append(block)

game = True # пока game = True цикл будет роботать
left = False
right = False
while game:
    wind.fill((0,0,0)) # очищаем екран черним цветом
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (1000, 0), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (0, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 700), (1000, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (1000, 0), (1000, 700), 5)

    # обработка собития для закрития окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_LEFT:
                left = True
    if right:
            platforma.x +=8
            platforma.rect.x +=8
    if left:
            platforma.x -=10
            platforma.rect.x -=10
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
                right = False
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
                left = False



    platforma.draw2()

    for b in blocks:
        if b.rect.colliderect(ball):
            blocks.remove(b)
            ball.speed_y*= -1
            ball.speed_x*= -1
        if b.rect.colliderect(CR2):
            blocks.remove(b)
            CR2.speed_y*= -1
            CR2.speed_x*= -1
        else:
            b.draw2()
    if len(blocks) == 0:
         wind.blit()
    
    if platforma.rect.colliderect(ball):
        ball.speed_y*= -1
    if platforma.rect.colliderect(CR2):
        CR2.speed_y*= -1


    ball.go() # двигаем мячик
    ball.draww() # рисуем мячик
    CR2.go()
    CR2.draww()

    

    pygame.display.update() # обновляем екран чтоби все отрисовалось
    clock.tick(60) # ограничиваем кадри в секунду

    # pygame.quit()
