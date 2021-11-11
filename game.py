# Import and initialize pygame
import pygame
from random import randint, choice
import random
pygame.init()
# Get the clock
clock = pygame.time.Clock()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

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
        x = [93, 218, 343]

        super(Apple, self).__init__(random.choice(x), 0, 'imgs/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here! 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500: 
            self.reset()


    def reset(self):
        x = [93, 218, 343]
        self.x = random.choice(x)
        self.y = -64

class Strawberry(GameObject):
    def __init__(self):
        y = [93, 218, 343]
        super(Strawberry, self).__init__(0, random.choice(y), 'imgs/strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()
    
    def reset(self):
        y = [93, 218, 343]
        self.x = -64
        self.y = random.choice(y)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(93, 93, 'imgs/player.png')
        self.dx = 93
        self.dy = 93
        self.reset()

    def left(self):
        if self.dx == 93:
            self.dx = self.dx
        else:
            self.dx -= 125


    def right(self):
        if self.dx == 343:
            self.dx = self.dx
        else:
            self.dx += 125

    def up(self):
        if self.dy == 93:
            self.dy = self.dy
        else:
            self.dy -= 125

    def down(self):
        if self.dy == 343:
            self.dy = self.dy
        else:
            self.dy += 125

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32
# Make an instance of GameObject
apple=Apple()
strawberry=Strawberry()
player=Player()

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
    # Draw apple
    apple.move()
    apple.render(screen)
    # Draw strawberry
    strawberry.move()
    strawberry.render(screen)
    # Draw player 
    player.move()
    player.render(screen)
    """
    apple1.x += 1
    apple1.render(screen)
    strawberry1.render(screen)
    apple2.render(screen)
    strawberry2.render(screen)
    apple3.render(screen)
    strawberry3.render(screen)
    apple4.render(screen)
    strawberry4.render(screen)
    apple5.render(screen)
    """

    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)