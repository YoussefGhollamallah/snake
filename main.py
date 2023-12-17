import pygame
pygame.init()


width = 600
height = 500
bg = (175, 215, 75)
bleu = (0, 0, 205)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
surface = pygame.Surface((100, 200))
surface.fill(bleu)

run = True
while run:
    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(surface, (200, 250))
    pygame.display.update() # Mise à jour de la boucle
    clock.tick(60)

pygame.quit()