import pygame, sys
pygame.init()


width = 600 # largeur
height = 500 #hauteur

bg = (175, 215, 75) # background color
# bleu = (0, 0, 205) 
# rouge = (205, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()



while True:
    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    pygame.display.update() # Mise à jour de la boucle
    clock.tick(60)

pygame.quit()





############ LE CODE EN DESSOUS ETAIS UN TEST #############

# surface = pygame.Surface((100, 200))
# surface.fill(bleu)

# rectangle = surface.get_rect(topright = (300,250))

# x_pos = 300


    # x_pos += 1
    # pygame.draw.rect(screen,rouge,rectangle)
    # # rectangle.right +=1
    # screen.blit(surface, rectangle)