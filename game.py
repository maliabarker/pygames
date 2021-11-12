# Import and initialize pygame
import pygame
from random import randint, choice
import random
pygame.init()
# Get the clock
clock = pygame.time.Clock()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
lanes = [93, 218, 343]
positive_move = (randint(0, 200) / 100) + 1
negative_move = ((randint(0, 200) / 100) + 1) * -1

# Create a new instance of Surface
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect() # add 

    def render(self, screen):
        self.rect.x = self.x # add
        self.rect.y = self.y # add
        screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
    def __init__(self):

        super(Apple, self).__init__(random.choice(lanes), 0, 'imgs/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here! 
        print(f'apple: {self.x},{self.y}')

    def move(self):

        self.x += self.dx
        self.y += self.dy
        
        # Check the y position of the apple
        if self.y >= 500 or self.y <= -64: 
            self.reset()


    def reset(self):
        self.x = random.choice(lanes)
        self.y = random.choice([-64, 500])
        if self.y == -64:
            self.dy = positive_move
        elif self.y == 500:
            self.dy = negative_move

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, random.choice(lanes), 'imgs/strawberry.png')
        self.dx = positive_move
        self.dy = 0
        self.reset()
        print(f'strawberry: {self.x},{self.y} {self.dx}, {self.dy}')

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= -64 or self.x >= 500:
            self.reset()
    
    def reset(self):
        self.x = random.choice([-64, 500])
        self.y = random.choice(lanes)
        if self.x == -64:
            self.dx = positive_move
        elif self.x == 500:
            self.dx = negative_move

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(93, 93, 'imgs/player.png')
        self.dx = 93
        self.dy = 93
        self.pos_x = 1 # new attribute
        self.pos_y = 1 # new attribute
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'imgs/bomb.png')
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= -64 or self.x >= 500 or self.y <= -64 or self.y >= 500:
            self.reset()

    def x_move(self):
        self.x = random.choice([-64, 500])
        self.y = random.choice(lanes)
        if self.x == -64:
            self.dx = positive_move
            self.dy = 0
        elif self.x == 500:
            self.dx = negative_move
            self.dy = 0

    def y_move(self):
        self.x = random.choice(lanes)
        self.y = random.choice([-64, 500])
        if self.y == -64:
            self.dy = positive_move
            self.dx = 0
        elif self.y == 500:
            self.dy = negative_move
            self.dx = 0

    def reset(self):
        list = [self.x_move, self.y_move]
        random.choice(list)()

class GameOver(GameObject):
    def __init__(self):
        super(GameOver, self).__init__(125, 177, 'imgs/game_over.png')
    def reset(self):
        self.x = -125

# Make an instance of GameObject
apple=Apple()
strawberry=Strawberry()
player=Player()
bomb=Bomb()
game_over=GameOver()
# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
# make a fruits Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)


# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                print('LEFT')
                player.left()
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
                player.right()
            elif event.key == pygame.K_UP:
                print('UP')
                player.up()
            elif event.key == pygame.K_DOWN:
                print('DOWN')
                player.down()

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render Sprites
    for entity in all_sprites:
	    entity.move()
	    entity.render(screen)

    # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
        positive_move += 0.2
        negative_move += 0.2
                
    # Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False
        game_over.render(screen)
        for entity in all_sprites:
            entity.dx = 0
            entity.dy = 0
        
    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)