import pygame 
pygame.init()

screen = pygame.display.set_mode([500, 500])

# Create the game loop
running = True 
while running: 
    # Looks at events 
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    running = False
	
    # Clear the screen
    screen.fill((255, 255, 255))
    # Colored circles
    '''
    tomato = (255, 99, 71)
    orange = (255, 160, 0)
    yellow = (255, 225, 0)
    green = (152, 251, 152)
    blue = (135, 206, 250)

    position1 = (70, 70)
    position2 = (430, 70)
    position3 = (250, 250)
    position4 = (70, 430)
    position5 = (430, 430)
    pygame.draw.circle(screen, tomato, position1, 60)
    pygame.draw.circle(screen, orange, position2, 60)
    pygame.draw.circle(screen, yellow, position3, 60)
    pygame.draw.circle(screen, green, position4, 60)
    pygame.draw.circle(screen, blue, position5, 60)
    '''
    # Circle grid
    x = 0
    while x < 9:
        #first row
        positionx = 70
        positiony = 70

        while x <= 3:
            pygame.draw.circle(screen, (100, 100, 100), (positionx, positiony), 60)
            positionx += 180
            x += 1
        
        positiony += 180
        while x in range(4, 7):
            
            if positionx > 430:
                positionx = 70
            
            pygame.draw.circle(screen, (100, 100, 100), (positionx, positiony), 60)
            positionx += 180
            x += 1
        
        positiony += 180
        while x in range(7, 10):
            if positionx > 430:
                positionx = 70
            pygame.draw.circle(screen, (100, 100, 100), (positionx, positiony), 60)
            positionx += 180
            x += 1

        

    # Update the display
    pygame.display.flip()
