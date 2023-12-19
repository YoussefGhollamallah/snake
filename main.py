import pygame, sys, random
from pygame.math import Vector2
pygame.init()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,bleu, block_rect)

    def move_snake(self):
        corp_copier = self.body[:-1]
        corp_copier.insert(0,corp_copier[0]+ self.direction)
        self.body = corp_copier[:]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number-1 )
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size ), int(self.pos.y * cell_size), cell_size,cell_size)
        pygame.draw.rect(screen,rouge, fruit_rect)


cell_size = 40
cell_number = 20

bg = (175, 215, 75) # background color
bleu = (0, 0, 205) 
rouge = (205, 0, 0)

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            snake.move_snake()


    screen.fill(bg)
    fruit.draw_fruit()
    snake.draw_snake()
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