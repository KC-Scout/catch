import pygame
import sys
from random import randint


length = 1200
width = 800


screen = pygame.display.set_mode((length, width))
screen_rect = screen.get_rect()


ball = pygame.image.load('ball.bmp')
ball_rect = ball.get_rect()
ball_rect.y = 15
ball_rect.x = randint(1, width)


while True: 
    screen.fill((255, 255, 103))
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    ball_rect.y += 1
    if ball_rect.y >= width:
        ball_rect.y = 15
        ball_rect.x = randint(1, width)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
