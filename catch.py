import pygame
import sys

length = 1200
width = 800


screen = pygame.display.set_mode((length, width))
screen_rect = screen.get_rect()


ball = pygame.image.load('ball.bmp')
ball_rect = ball.get_rect()
ball_rect.y = ball_rect.width
ball_rect.x = screen_rect.centerx


while True: 
    screen.fill((255, 255, 103))
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_rect.y += 15
    
    screen.blit(ball, ball_rect)
    pygame.display.flip()
