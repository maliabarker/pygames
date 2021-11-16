# gameobject.py
import pygame

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