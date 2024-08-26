import pygame
from settings import *

pygame.init()
font = pygame.font.Font(None,40)
 
def Debug(info,y=10,x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info),True,TEXT_COLOR)
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface,BACK_COLOR,debug_rect)
    display_surface.blit(debug_surf,debug_rect)
