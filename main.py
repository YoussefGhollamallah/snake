import pygame, sys, random
from pygame.math import Vector2

pygame.init()

class SNAKE:
    def __init__(self):  # permet d'initialiser le serpent dans la fenêtre et d'uploader les variables d'affichage du corp du serpent
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('images/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('images/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('images/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('images/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('son/crunch.wav')

    def afficher_snake(self): # permet d'afficher le serpent
        self.update_head_graphics()
        self.update_corp_graphics()

        # boucle qui permet d'afficher les block du serpent tête corp et queue en fonction de la route prise
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect) 

            # x_pos = int(block.x * cell_size)
            # y_pos = int(block.y * cell_size)
            # block_rect = pygame.Rect(x_pos,y_pos, cell_size, cell_size)
            # pygame.draw.rect(screen,bleu, block_rect)

    def update_head_graphics(self): # permet de mettre a jour l'affichage de la tête
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_corp_graphics(self): # permet de mettre a jour l'affichage du corp
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down



    def move_snake(self):
        if self.new_block == True:
            corp_copier = self.body[:]
            corp_copier.insert(0,corp_copier[0]+ self.direction)
            self.body = corp_copier[:]
            self.new_block = False
        else:
            corp_copier = self.body[:-1]
            corp_copier.insert(0,corp_copier[0]+ self.direction)
            self.body = corp_copier[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def afficher_pomme(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size ), int(self.pos.y * cell_size), cell_size , cell_size)
        screen.blit(pomme, fruit_rect)
        

    def randomize(self): 
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number_heigth -1 )
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_colision()
        self.check_fail()
        

    def draw_elements(self):
        self.afficher_herbe()
        self.fruit.afficher_pomme()
        self.snake.afficher_snake()
        self.afficher_score()

    def check_colision(self): # fonction qui permet de vérifier que la pomme à étais mangé par le serpent et la replace aléatoirement sur l'écran
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

    def check_fail(self):
        # condition qui permet de vérifié et quitte le jeu si le serpent touche le bord de la fenêtre
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number_heigth:
           self.game_over()

        # condition qui permet de vérifié et quitte le jeu si le serpent touche une autre partie de sont corp
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()

    def afficher_herbe(self):
        grass_color = (165,209,61)
        for row in range(cell_number):
            if row % 2 == 0: 
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def afficher_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number_heigth - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = pomme.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(pomme,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

pygame.mixer.pre_init(44100,-16,2,512)


cell_size = 42
cell_number = 24
cell_number_heigth = 18

bg = (175, 215, 75) # background color
bleu = (0, 0, 205) 
rouge = (205, 0, 0)
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number_heigth))
pomme = pygame.image.load("images/apple.png").convert_alpha()
pygame.display.set_caption("Snake Game")
game_font = pygame.font.Font("Font/PoetsenOne-Regular.ttf",25)
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 200)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_z:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)


    
    screen.fill(bg)
    main_game.draw_elements()
    pygame.display.update() # Mise à jour de la boucle
    clock.tick(60)



############ LE CODE EN DESSOUS ETAIS UN TEST #############

# surface = pygame.Surface((100, 200))
# surface.fill(bleu)

# rectangle = surface.get_rect(topright = (300,250))

# x_pos = 300


    # x_pos += 1
    # pygame.draw.rect(screen,rouge,rectangle)
    # # rectangle.right +=1
    # screen.blit(surface, rectangle)