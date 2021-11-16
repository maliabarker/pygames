# Import and initialize pygame
import pygame
import constants
from constants import clock, screen, bg, score, highscore, font
import sprites
from sprites import Apple, Strawberry, Bomb, Player, GameOver
'''
# class Star(GameObject):
#     def __init__(self):
#         super(Star, self).__init__(125, 50, 'imgs/star.png')
    
# class AnimatedObject(pygame.sprite.Sprite):
#     def __init__(self, x, y, files):
# 	    super(AnimatedObject, self).__init__()
# 	    self.x = x
# 	    self.y = y
# 	    self.images = []
# 	    self.index = 0
        
# 		# create a surface from each file in files and add a 
# 		# surface to the images list
#     def load_images(self):
#         for file in self.files:
#             surf = pygame.image.load(file)
#             rect = surf.get_rect()
#             self.images.append(rect)
#     def render(self, screen):
#         self.index += 1
#         if self.index == len(self.images):
#             self.index = 0
# 		# increment index 
# 		# if index is equal to the length of images 
# 		# set index to 0
# 		# blit the surface in images at the index to the screen

# class Star(AnimatedObject):
#     def __init__(self):
#         super(Star, self).__init__(125, 50, ['img/star.png', 'img/star_2.png', 'img/star_3.png', 'img/star_4.png', 'img/star_5.png'])
#         self.files = files
# Make an instance of GameObject
# star=Star()
# star.load_images()
# print(star.images)
'''

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
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.event.set_allowed(pygame.KEYDOWN)
            sprites.positive_move = constants.positive_move
            sprites.negative_move = constants.negative_move
            score = 0
            for entity in all_sprites:
                entity.reset()
                

    # Clear screen
    screen.blit(bg, (0, 0))

    # Move and render Sprites
    for entity in all_sprites:
	    entity.move()
	    entity.render(screen)

    # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
        sprites.positive_move += 0.2
        sprites.negative_move += 0.2
        
        score += 1
        if score > highscore:
            highscore = score
                
    # Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        # running = False
        for entity in all_sprites:
            if entity == player:
                pass
            else:
                entity.dx = 0
                entity.dy = 0

        pygame.event.set_blocked(pygame.KEYDOWN)

        game_over.render(screen)
        reset_surf = font.render('Click anywhere to restart', True, (0,0,0))
        reset_rect = reset_surf.get_rect(center=(250, 400))
        screen.blit(reset_surf, reset_rect)
    
    # TEXT
    score_surf = font.render(f'score: {score}', True, (0,0,0))
    highscore_surf = font.render(f'highscore: {highscore}', True, (0,0,0))
    # You can pass the center directly to the `get_rect` method.
    score_rect = score_surf.get_rect(center=(100, 30))
    highscore_rect = highscore_surf.get_rect(center=(200, 30))
    screen.blit(score_surf, score_rect)
    screen.blit(highscore_surf, highscore_rect)
                
    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)