import pygame
import sys



while True: 
    screen = pygame.display.set_mode((1200, 800))
    screen.fill((255, 255, 103))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball = pygame.image.load(
    
    pygame.display.flip()
