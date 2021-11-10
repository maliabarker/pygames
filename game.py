# Import and initialize pygame
import pygame
pygame.init()
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

# Make an instance of GameObject
apple1 = GameObject(70, 70, 'imgs/apple.png')
strawberry1 = GameObject(250, 70, 'imgs/strawberry.png')
apple2 = GameObject(430, 70, 'imgs/apple.png')
strawberry2 = GameObject(70, 250, 'imgs/strawberry.png')
apple3 = GameObject(250, 250, 'imgs/apple.png')
strawberry3 = GameObject(430, 250, 'imgs/strawberry.png')
apple4 = GameObject(70, 430, 'imgs/apple.png')
strawberry4 = GameObject(250, 430, 'imgs/strawberry.png')
apple5 = GameObject(430, 430, 'imgs/apple.png')
# Creat the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))
    # Draw box
    apple1.render(screen)
    strawberry1.render(screen)
    apple2.render(screen)
    strawberry2.render(screen)
    apple3.render(screen)
    strawberry3.render(screen)
    apple4.render(screen)
    strawberry4.render(screen)
    apple5.render(screen)
    # Update the window
    pygame.display.flip()