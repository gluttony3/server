import pygame
import socket
from random import randint

# Инициализация игры
pygame.init()
window = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

# Класс для шариков (игрока и еды)
class Ball:
    def __init__(self, x, y, color, radius, name="PLAYER"):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.name = name
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
    
    def draw(self):
        pygame.draw.circle(window, self.color, (self.rect.x, self.rect.y), self.radius)
        if self.color == (0, 200, 100):  # Только для игрока
            font = pygame.font.Font("OpenSans-Bold.ttf", 30)
            text = font.render(self.name, True, (255, 255, 255))
            window.blit(text, (self.rect.x - 50, self.rect.y - 20))

# Подключение к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 2118))

# Создаем много еды (3000 шариков)
food = []
for i in range(3000):
    food.append(Ball(
        randint(-2000, 2000),
        randint(-2000, 2000),
        (randint(0, 255), randint(0, 255), randint(0, 255)),
        randint(5, 15)
    ))

# Создаем игрока
player = Ball(500, 350, (0, 200, 100), 50)

# Ввод имени игрока
name = ""
input_active = True
input_rect = pygame.Rect(400, 20, 200, 40)
font = pygame.font.Font("OpenSans-Bold.ttf", 40)

while input_active:
    window.fill((122, 230, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            input_active = False
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if name.strip() != "":
                    player.name = name
                    input_active = False
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode
    
    # Рисуем поле ввода
    pygame.draw.rect(window, (173, 216, 230), input_rect, border_radius=10)
    text_surface = font.render(name, True, (0, 0, 0))
    window.blit(text_surface, (input_rect.x + 10, input_rect.y + 5))
    
    pygame.display.update()
    clock.tick(60)

# Основной игровой цикл
running = True
while running:
    window.fill((122, 230, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление - двигаем еду, игрок остается на месте
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        for item in food:
            item.rect.x -= 5
    if keys[pygame.K_LEFT]:
        for item in food:
            item.rect.x += 5
    if keys[pygame.K_UP]:
        for item in food:
            item.rect.y += 5
    if keys[pygame.K_DOWN]:
        for item in food:
            item.rect.y -= 5
    
    # Рисуем всю еду
    for item in food:
        item.draw()
    
    # Рисуем игрока
    player.draw()
    
    pygame.display.update()
    clock.tick(60)

client_socket.close()
pygame.quit()