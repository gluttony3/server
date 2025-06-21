import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
COLOR = (52, 235, 222)
window.fill(COLOR)
rect = pygame.Rect(0,0,100,100)
img = pygame.image.load("big_rock.png")
img = pygame.transform.scale(img, (500,100))
img2 = pygame.image.load("full_h_block.png")
img2 = pygame.transform.scale(img2, (500,100))

spisok =

for i in range(len(spisok)):
    window.blit(spisok[i], (x,y))
    x += 50
while True:
    pygame.draw.rect(window,(235, 171, 52), rect)
    window.blit(img,(5,20))

    pygame.display.update()


