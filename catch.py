import pygame
import sys
from random import randint
from pygame.sprite import Sprite
# ~ from pygame import 

pygame.font.init()

width = 1200
height = 800


screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()

class Ball(Sprite):
    """Sprite class for ball"""
    def __init__(self, width):
        super(Ball, self).__init__()
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = 15
        self.rect.x = randint(1, width)
        
class Basket(Sprite):
    """Sprite class for basket"""
    def __init__(self, screen_rect):
        super(Basket, self).__init__()
        self.image = pygame.image.load('basket.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom

def collision(sprite_one, sprite_two):
    return pygame.sprite.collide_rect(sprite_one, sprite_two)
        
ball = Ball(width)
basket = Basket(screen_rect)
while True: 
    screen.fill((255, 255, 103))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                basket.rect.x += 40
            if event.key == pygame.K_LEFT:
                basket.rect.x -= 40
    
    ball.rect.y += 1
    if collision(basket, ball) or ball.rect.y >= height:
        ball.rect.y = 15
        ball.rect.x = randint(1, width)
    
    screen.blit(basket.image, basket.rect)    
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
