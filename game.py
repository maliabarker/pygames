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
    # self.surf = pygame.Surface((width, height))
    # self.surf.fill((255, 0, 255))
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
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


# Make an instance of GameObject
apple=Apple()
strawberry=Strawberry()
player=Player()
bomb=Bomb()
# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

"""
apple1 = GameObject(70, 70, 'imgs/apple.png')
strawberry1 = GameObject(250, 70, 'imgs/strawberry.png')
apple2 = GameObject(430, 70, 'imgs/apple.png')
strawberry2 = GameObject(70, 250, 'imgs/strawberry.png')
apple3 = GameObject(250, 250, 'imgs/apple.png')
strawberry3 = GameObject(430, 250, 'imgs/strawberry.png')
apple4 = GameObject(70, 430, 'imgs/apple.png')
strawberry4 = GameObject(250, 430, 'imgs/strawberry.png')
apple5 = GameObject(430, 430, 'imgs/apple.png')
"""

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

    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)