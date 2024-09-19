import pygame
from settings import MAGIC_LIST,WEAPONS_LIST,UI_SETTINGS,COLORS_SETTINGS

class UI:
    def __init__(self):
        
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_SETTINGS['ui_font'],UI_SETTINGS['ui_font_size'])

        # bar setup
        self.health_bar_rect = pygame.Rect(10,10,UI_SETTINGS['health_bar_width'],UI_SETTINGS['bar_height'])
        self.energy_bar_rect = pygame.Rect(10,34,UI_SETTINGS['energy_bar_width'],UI_SETTINGS['bar_height'])

        # convert weapon dictionary
        self.weapon_graphics =[]
        for weapon in WEAPONS_LIST.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        # convert magic dictionary
        self.magic_graphics =[]
        for magic in MAGIC_LIST.values():
            path = magic['graphic']
            magic = pygame.image.load(magic['graphic']).convert_alpha()
            self.magic_graphics.append(magic)

        # convert bag dictionary -- for bag implementation

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

    def selection_box(self,left,top,has_switched):
        bg_rect = pygame.Rect(left,top,UI_SETTINGS['item_box_size'],UI_SETTINGS['item_box_size'])
        pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_bg_color'],bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color_active'],bg_rect,UI_SETTINGS['padding'])
        else:
            pygame.draw.rect(self.display_surface,UI_SETTINGS['ui_border_color'],bg_rect,UI_SETTINGS['padding'])
        return bg_rect

    def weapon_overlay(self,weapon_index,has_switched): # to show weapons on its box
        bg_rect = self.selection_box(UI_SETTINGS['box_pos_x'],
                                     UI_SETTINGS['box_pos_y'],has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surf,weapon_rect)

    def magic_overlay(self,magic_index,has_switched):
        bg_rect = self.selection_box(UI_SETTINGS['box_pos_x']+UI_SETTINGS['item_box_size']+UI_SETTINGS['padding'],
                                     UI_SETTINGS['box_pos_y'],has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)

        self.display_surface.blit(magic_surf,magic_rect)  

    # bag overlay -- for bag implementation

    # DEFINIR DEMAIS OVERLAYS NECESSÁRIOS

    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,COLORS_SETTINGS['health_color'])
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,COLORS_SETTINGS['energy_color'])

        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
        self.magic_overlay(player.magic_index,not player.can_switch_magic)
