import time, sys
import pygame
from support import set_dictionary
from settings import RESOURCES_TYPES,UI_SETTINGS,COLORS_SETTINGS
from onScreen import show_value

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
        text_size_factor = 0.80
        x_offset = -130
        y_pos = self.display_surface.get_size()[1] -80

        bg_color = (54, 54, 54)
        border_color = (98, 104, 54)

        # Criar as linhas de texto
        lines = {
            '0': [
                {'txt': 'Exp : ', 'color': (255, 255, 255)},  # Texto normal
                {'txt': str(exp), 'color': (143, 151, 88)}
            ], 
        }
        show_value(self, exp, lines, x_offset, y_pos,text_size_factor,bg_color,border_color)
    
    def show_goals(self, prop_counter, enemy_counter):
        counter_type = [prop_counter, enemy_counter]
        text_size_factor = 0.7
        x_offset = - 230
        y_pos = 20

        bg_color = (54, 54, 54)
        border_color = (98, 104, 54)

        # Criar as linhas de texto
        lines = {
            '0': [{'txt': 'Missões', 'color': (255, 255, 0)}],
            '1': [
                {'txt': 'Destruir ', 'color': (255, 255, 255)},  # Texto normal
                {'txt': str(counter_type[0]), 'color': (143, 151, 88)},    # Contador em amarelo
                {'txt': ' ervas daninhas', 'color': (255, 255, 255)}  # Texto normal
            ], 
            '2': [
                {'txt': 'Derrotar ', 'color': (255, 255, 255)},  # Texto normal
                {'txt': str(counter_type[1]), 'color': (143, 151, 88)},     # Contador em amarelo
                {'txt': ' porkos', 'color': (255, 255, 255)}     # Texto normal
            ]
        }
        show_value(self, counter_type, lines, x_offset, y_pos,text_size_factor,bg_color,border_color)

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

    def display(self,player,prop_counter,enemy_counter):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,COLORS_SETTINGS['health_color'])
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,COLORS_SETTINGS['energy_color'])

        self.show_exp(player.exp)
        
        keys = RESOURCES_TYPES
        indexes = [getattr(player, f'{key}_index') for key in keys]
        has_switchers = [not getattr(player, f'can_switch_{key}') for key in keys]
        
        self.resources_overlay(indexes, has_switchers)
        self.show_goals(prop_counter,enemy_counter)
        # self.end_game_prompt(end_game)
