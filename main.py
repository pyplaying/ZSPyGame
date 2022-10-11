import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode()
w, h = screen.get_size()
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()