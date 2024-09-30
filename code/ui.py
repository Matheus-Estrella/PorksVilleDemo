import time, sys
import pygame
from support import set_dictionary
from settings import RESOURCES_TYPES,UI_SETTINGS,COLORS_SETTINGS

class UI:
    def __init__(self):
        
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_SETTINGS['ui_font'],UI_SETTINGS['ui_font_size'])

        # bar setup
        self.health_bar_rect = pygame.Rect(10,10,UI_SETTINGS['health_bar_width'],UI_SETTINGS['bar_height'])
        self.energy_bar_rect = pygame.Rect(10,34,UI_SETTINGS['energy_bar_width'],UI_SETTINGS['bar_height'])

        # transformation, bag, weapon and magic position
        self.side_bar_positions = self.get_bar_side_positions(0,-30)

        # convert weapon dictionary
        resources_list = RESOURCES_TYPES             
        for resource in resources_list:
            setattr(self, f'{resource}_graphics', set_dictionary(resource))


    def show_bar(self,current,max_amount,bg_rect,color):
        #draw background
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_bg_color'],bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        # drawing the bar
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color'],bg_rect,3)

    def show_exp(self,exp):
        text_surf = self.font.render(str(int(exp)),False,COLORS_SETTINGS['text_color'])
        x = self.display_surface.get_size()[0] -20
        y = self.display_surface.get_size()[1] -20
        text_rect = text_surf.get_rect(bottomright = (x,y))
        
        #background for exp (behind attacks)
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_bg_color'],text_rect.inflate(20,20))
        self.display_surface.blit(text_surf,text_rect)
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color'],text_rect.inflate(20,20),3)

    # def end_game_prompt(self,end_game):
    #     if end_game:
    #         text_surf = self.font.render('PARABÉNS, VOCÊ SALVOU A NATUREZA HOJE', True, COLORS_SETTINGS['text_color'])
    #         screen_width = 1280
    #         screen_height = 720
    #         text_rect = text_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    #         box_width = text_rect.width + 20
    #         box_height = text_rect.height + 20
    #         box_rect = pygame.Rect((screen_width // 2) - (box_width // 2), (screen_height // 2) - (box_height // 2), box_width, box_height)

    #         pygame.draw.rect(self.display_surface, (0, 0, 0), box_rect)
    #         pygame.draw.rect(self.display_surface, (0, 0, 0), text_rect.inflate(40,40))  # Fundo branco
    #         pygame.draw.rect(self.display_surface, (0, 0, 0), text_rect.inflate(40,40), 3)  # Borda preta
    #         self.display_surface.blit(text_surf, text_rect)
            
    #         time.sleep(15)
    #         pygame.quit()
    #         sys.exit()

    def selection_box(self,left,top,has_switched):
        bg_rect = pygame.Rect(left,top,UI_SETTINGS['item_box_size'],UI_SETTINGS['item_box_size'])
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_bg_color'],bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color_active'],bg_rect,UI_SETTINGS['padding'])
        else:
            pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color'],bg_rect,UI_SETTINGS['padding'])
        return bg_rect

    def get_bar_side_positions(self, x_move, y_move):

        max_x = UI_SETTINGS['box_pos_x'] + x_move
        min_y = UI_SETTINGS['box_pos_y'] + y_move
        pad = UI_SETTINGS['padding']
        box_size = UI_SETTINGS['item_box_size']
        jump = pad + box_size

        magic = [max_x,min_y]
        weapon = [max_x,min_y-jump*1]
        bag = [max_x+1000,min_y-jump*2+1000,] # +1000 to stay out of the map
        transformation = [max_x+1000,min_y-jump*3+1000,] # +1000 to stay out of the map

        return {
        'transformation': transformation,
        'bag': bag,
        'weapon': weapon,
        'magic': magic
        }
    
    def resources_overlay(self, indexes, has_switchers):
        keys = RESOURCES_TYPES
        graphics_lists = [getattr(self, f'{key}_graphics') for key in keys]

        for i, key in enumerate(keys):
            if indexes[i] < len(graphics_lists[i]):
                bg_rect = self.selection_box(self.side_bar_positions[key][0],
                                            self.side_bar_positions[key][1], has_switchers[i])
                surf = graphics_lists[i][indexes[i]]
                rect = surf.get_rect(center=bg_rect.center)
                self.display_surface.blit(surf, rect)

    def display(self,player,end_game):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,COLORS_SETTINGS['health_color'])
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,COLORS_SETTINGS['energy_color'])

        self.show_exp(player.exp)
        
        keys = RESOURCES_TYPES
        indexes = [getattr(player, f'{key}_index') for key in keys]
        has_switchers = [not getattr(player, f'can_switch_{key}') for key in keys]
        
        self.resources_overlay(indexes, has_switchers)
        # self.end_game_prompt(end_game)
