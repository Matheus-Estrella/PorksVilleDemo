import pygame
from settings import COLORS_SETTINGS

pygame.init()
font = pygame.font.Font(None, 40)

def Debug(info, x, y, text_color=None, duration=1500):
    global debug_start_time, debug_info, debug_x, debug_y, debug_text_color

    if 'debug_start_time' not in globals():
        debug_start_time = pygame.time.get_ticks()
        debug_info = info
        debug_x = x
        debug_y = y
        debug_text_color = text_color if text_color else COLORS_SETTINGS['text_color']
    elif pygame.time.get_ticks() - debug_start_time < duration:
        display_surface = pygame.display.get_surface()
        lines = debug_info.splitlines()
        y_offset = 0
        for line in lines:
            debug_surf = font.render(line, True, debug_text_color)
            debug_rect = debug_surf.get_rect(topleft=(debug_x, debug_y + y_offset))
            pygame.draw.rect(display_surface, COLORS_SETTINGS['back_color'], debug_rect)
            display_surface.blit(debug_surf, debug_rect)
            y_offset += debug_surf.get_height()
    else:
        del debug_start_time
        del debug_info
        del debug_x
        del debug_y
        del debug_text_color


""" PREVIOUS CODE RUNNING, IF NECESSARY
import pygame
from settings import COLORS_SETTINGS

pygame.init()
font = pygame.font.Font(None,40)
 
def Debug(info,x,y,text_color):
    display_surface = pygame.display.get_surface()
    if text_color == None:
        text_color = COLORS_SETTINGS['text_color']
    lines = info.splitlines()
    
    y_offset = 0
    for line in lines:
        debug_surf = font.render(line, True, text_color)
        debug_rect = debug_surf.get_rect(topleft=(x, y + y_offset))
        pygame.draw.rect(display_surface, COLORS_SETTINGS['back_color'], debug_rect)
        display_surface.blit(debug_surf, debug_rect)
        y_offset += debug_surf.get_height()
"""
