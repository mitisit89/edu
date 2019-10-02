import pygame
pygame.init
win= pygame.display.set_mode((500,500))

pygame.display.set_caption('cube')

x=50
y=60
width=50
height=50
speed=5
run=True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==print.QUIT:
            run=False
    pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    pygame.display.update()
pygame.quit()
