import pygame

pygame.init()

width = 600
height = 500
bg = (25, 35, 55)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(bg)
    pygame.display.flip()

pygame.quit()